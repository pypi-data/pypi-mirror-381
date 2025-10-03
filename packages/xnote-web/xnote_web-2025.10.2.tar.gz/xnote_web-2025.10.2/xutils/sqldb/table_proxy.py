# -*- coding:utf-8 -*-
"""
@Author       : xupingmao
@email        : 578749341@qq.com
@Date         : 2023-04-28 21:09:40
@LastEditors  : xupingmao
@LastEditTime : 2024-08-31 20:38:37
@FilePath     : /xnote/xutils/sqldb/table_proxy.py
@Description  : SQL表查询代理
"""
import time
import xutils
import web.db

from web.db import SQLQuery, sqlparam
from xutils.sqldb import table_manager
from xutils.sqldb.table_config import TableConfig
from xutils.interfaces import ProfileLog, ProfileLogger, SQLDBInterface
from xutils.db.binlog import BinLog, BinLogOpType



class TableProxy(SQLDBInterface):
    """基于web.db的装饰器
    SqliteDB是全局唯一的, 它的底层使用了连接池技术, 每个线程都有独立的sqlite连接
    """
    log_profile = False
    enable_binlog = False
    writable = True
    profile_logger = ProfileLogger()

    def __init__(self, db: web.db.DB, tablename: str):
        # SqliteDB 内部使用了threadlocal来实现，是线程安全的，使用全局单实例即可
        assert isinstance(db, web.db.DB)
        self.table_name = tablename
        self.db = db
        table_info = table_manager.TableManagerFacade.get_table_info(tablename)
        assert table_info != None
        self.table_info = table_info
        self.db_type = table_info.db_type
        self.enable_binlog = TableConfig.enable_binlog and table_info.enable_binlog

    @property
    def tablename(self):
        return self.table_name

    def fix_sql_keywords(self, values):
        # 兼容关键字
        if isinstance(values, dict):
            new_result = {}
            for key in values:
                value = values[key]
                if "`" not in key:
                    new_result[f"`{key}`"] = value
                else:
                    new_result[key] = value
            return new_result
        return values
    
    def handle_result_set(self, result_set):
        # TODO 转换类型用于序列化
        result = []
        for item in result_set:
            # for attr in item:
            #     value = item.get(attr)
            result.append(item)
        return result
    
    def check_write_state(self):
        if not self.writable:
            raise Exception("当前状态不能写入")

    def insert(self, seqname=None, _test=False, **values):
        assert len(values) > 0
        self.check_write_state()
        values = self.fix_sql_keywords(values)
        start_time = time.time()
        try:
            new_id = self.db.insert(self.tablename, seqname, _test, **values)
            self.add_insert_binlog(new_id, _test=_test)
            return new_id
        except Exception as e:
            del self.db.ctx.db # 尝试重新连接
            raise e
        finally:
            cost_time = time.time() - start_time
            self._add_profile_log(cost_time, "insert")
        
    def select(self, vars=None, what='*', where=None, order=None, group=None,
               limit=None, offset=None, _test=False):
        if limit != None:
            assert limit > 0
        if offset != None:
            assert offset >= 0
        where = self.fix_sql_keywords(where)
        result_set = self.db.select(self.tablename, vars=vars, what=what, where=where, order=order, group=group,
                              limit=limit, offset=offset, _test=_test)
        records = list(result_set) # type: ignore
        return records
    
    def select_first(self, *args, **kw):
        if "limit" not in kw:
            kw["limit"] = 1
        records = self.select(*args, **kw)
        if len(records) > 0:
            return records[0]
        return None

    def query(self, *args, **kw):
        return list(self.db.query(*args, **kw)) # type:ignore
    
    def raw_query(self, *args, **kw):
        return self.db.query(*args, **kw)

    def count(self, where=None, sql=None, vars=None) -> int:
        where = self.fix_sql_keywords(where)
        if sql is None:
            return self.select_first(what="COUNT(1) AS amount", where=where, vars=vars).amount # type:ignore
        return self.db.query(sql, vars=vars).first().amount # type: ignore

    def update(self, where, vars=None, _test=False, _skip_binlog=False, _skip_profile=False, **values):
        assert len(values) > 0
        self.check_write_state()
        where = self.fix_sql_keywords(where)
        values = self.fix_sql_keywords(values)
        
        start_time = time.time()
        try:
            result = self.db.update(self.tablename, where, vars=vars, _test=_test, **values)
            if not _skip_binlog:
                self._add_update_binlog(where=where, vars=vars, _test=_test)
            return result
        except Exception as e:
            del self.db.ctx.db # 尝试重新连接
            raise e
        finally:
            cost_time = time.time() - start_time
            self._add_profile_log(cost_time, "update", _skip_profile=_skip_profile)

    def delete(self,  where, using=None, vars=None, _test=False):
        self.check_write_state()
        if _test:
            # delete为了记录binlog会转换成按照主键删除的sql, 所以这里单独处理下_test场景
            return self.db.delete(self.tablename, where, using=using, vars=vars, _test=True)
        
        where = self.fix_sql_keywords(where)

        start_time = time.time()
        try:
            if self.enable_binlog:
                return self._delete_with_binlog(where=where, vars=vars)
            else:
                return self.db.delete(self.tablename, where=where, using=using, vars=vars)
        except Exception as e:
            del self.db.ctx.db # 尝试重新连接
            raise e
        finally:
            cost_time = time.time() - start_time
            self._add_profile_log(cost_time, "delete")

    def _delete_with_binlog(self, where, vars):
        pk_name = self.table_info.pk_name
        pk_list = []

        for row in self.select(what=pk_name, where=where, vars=vars):
            pk_value = row.get(pk_name)
            pk_list.append(pk_value)
        
        if len(pk_list) > 0:
            new_where = f"`{pk_name}` in $pk_list"
            new_vars = dict(pk_list=pk_list)
            result = self.db.delete(self.tablename, where=new_where, vars=new_vars)
            self._add_delete_binlog(pk_list)
            return result
    
    def transaction(self):
        return self.db.transaction()
    
    def iter(self, where="", vars=None):
        for records in self.iter_batch(where=where, vars=vars):
            for record in records:
                yield record


    def iter_batch(self, batch_size=20, where="", vars=None):
        assert isinstance(where, str)
        
        pk_name = self.table_info.pk_name
        last_id = 0
        while True:
            this_vars = dict(last_id = last_id)
            if vars != None:
                this_vars.update(vars)
            records = self.select(where = f"{pk_name} > $last_id " + where, vars = this_vars, limit = batch_size, order=pk_name)
            if len(records) == 0:
                break
            yield records
            last_id = records[-1].get(pk_name)
    
    def get_table_info(self) -> table_manager.TableInfo:
        return self.table_info

    def filter_record(self, record):
        # type: (dict) -> dict
        result = {}
        table_info = self.get_table_info()
        for colname in table_info.column_names:
            col_value = record.get(colname)
            if col_value != None:
                result[colname] = col_value
        
        pk_name = table_info.pk_name
        result[pk_name] = record.get(pk_name)
        return result

    def _add_row_binlog(self, row):
        if not self.enable_binlog:
            return
        if row == None:
            return
        
        if self.table_name in TableConfig._disable_binlog_tables:
            return
        
        pk_name = self.table_info.pk_name
        pk_value = row.get(pk_name)

        BinLog.get_instance().add_log(BinLogOpType.sql_upsert, pk_value, table_name=self.tablename)

    def add_insert_binlog(self, new_id, _test=False):
        if _test:
            return
        if not self.enable_binlog:
            return
        
        if self.table_name in TableConfig._disable_binlog_tables:
            return
        
        pk_name = self.table_info.pk_name
        where = {
            pk_name: new_id
        }
        row = self.select_first(where=where)
        self._add_row_binlog(row)

    def _add_update_binlog(self, where=None, vars=None, _test=False):
        if _test:
            return
        if not self.enable_binlog:
            return
        if self.table_name in TableConfig._disable_binlog_tables:
            return
                
        for row in self.select(where=where, vars=vars):
            self._add_row_binlog(row)

    def _add_delete_binlog(self, pk_list=[]):
        if not self.enable_binlog:
            return

        if self.table_name in TableConfig._disable_binlog_tables:
            return
        
        for pk_value in pk_list:
            BinLog.get_instance().add_log(BinLogOpType.sql_delete, pk_value, table_name=self.tablename)
        

    def get_column_names(self):
        return self.table_info.column_names

    def replace(self, seqname=None, _test=False, **values):
        """XXX: 测试中
        执行replace into操作
        """
        assert len(values)>0
        tablename = self.table_name
        def q(x):
            return "(" + x + ")"
        
        sorted_values = sorted(values.items(), key=lambda t: t[0])

        _keys = SQLQuery.join(map(lambda t: t[0], sorted_values), ", ") # type: ignore
        _values = SQLQuery.join(
            [sqlparam(v) for v in map(lambda t: t[1], sorted_values)], ", " # type: ignore
        )
        sql_query = (
            "REPLACE INTO %s " % tablename + q(_keys) + " VALUES " + q(_values)
        )

        return self.db.query(sql_query)

    def _new_profile_log(self):
        log = ProfileLog()
        log.ctime = xutils.format_datetime()
        log.table_name = self.tablename
        log.type = "db_profile"
        return log
    
    def _add_profile_log(self, cost_time=0.0, op_type="", _skip_profile=False):
        if _skip_profile:
            return
        if not self.log_profile:
            return
        if not self.table_info.log_profile:
            return
        if self.table_name in TableConfig._disable_profile_tables:
            return
        
        profile_log = self._new_profile_log()
        profile_log.cost_time = cost_time
        profile_log.op_type = op_type
        self.profile_logger.log(profile_log)

    def check_is_unique(self, update_pk = None, **where_kw):
        """检查是否是唯一的
        Arguments:
        - update_pk: 更新场景的主键, 可选参数
        - where_kw: 检查的键值对, 必选参数
        """
        assert len(where_kw) > 0, "where_kw can not be empty"
        pk_name = self.table_info.pk_name
        old = self.select_first(what = pk_name, where = where_kw)
        if old is None:
            return True
        if update_pk != None:
            return old.get(pk_name) == update_pk
        return False


class TempTableProxy(TableProxy):

    def __init__(self, db: web.db.DB, tablename: str):
        # super().__init__(db, tablename)
        self.table_info = None
        self.db_type = "empty"
        self.table_name = tablename
        self.db = db