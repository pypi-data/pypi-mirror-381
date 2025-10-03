# -*- coding:utf-8 -*-
# Created by xupingmao on 2017/03/15
# @modified 2021/11/07 14:14:15
"""Xnote的数据库配置(此模块已经废弃)
    考虑到持续运行的维护，增加表结构需要非常慎重
    考虑清楚你需要的是数据还是配置，如果是配置建议通过扩展脚本配置xconfig
"""
import os
import threading
import xutils
import web.db
from xnote.core import xconfig
from xutils import dbutil
from xutils.dbutil import interfaces
from xutils.sqldb import TableManagerFacade as TableManager
from xutils.sqldb import TableProxy, TableConfig
from xutils import fsutil
from xutils.dateutil import DEFAULT_DATE, DEFAULT_DATETIME

class MySqliteDB(web.db.SqliteDB):
    _lock = threading.RLock()
    _instances = set() # type: set[MySqliteDB]
    dbpath = ""

    def __init__(self, db=""):
        super().__init__(db=db)
        with self._lock:
            MySqliteDB._instances.add(self)

    def __del__(self):
        with self._lock:
            MySqliteDB._instances.remove(self)

    def __hash__(self):
        return id(self)

class DBPool:
    # TODO 池化会导致资源无法释放

    sqlite_pool = {} # type: dict[str, MySqliteDB]
    mysql_instance = None # type: web.db.MySQLDB|None

    @classmethod
    def get_sqlite_db(cls, dbpath=""):
        # type: (str) -> MySqliteDB
        assert dbpath != ""
        db = cls.sqlite_pool.get(dbpath)
        if db is None:
            db = MySqliteDB(db=dbpath)
            db.query("pragma journal_mode = %s" % xconfig.DatabaseConfig.sqlite_journal_mode)
            if xconfig.DatabaseConfig.sqlite_page_size != 0:
                db.query("pragma page_size = %s" % xconfig.DatabaseConfig.sqlite_page_size)
            cls.sqlite_pool[dbpath] = db
        return db

def create_table_manager_with_dbpath(table_name="", dbpath="", **kw):
    assert table_name != ""
    assert dbpath != ""
    db = get_db_instance(dbpath)
    kw["db_type"] = xconfig.DatabaseConfig.db_driver_sql
    kw["dbpath"] = dbpath
    return TableManager(table_name, db=db, mysql_database=xconfig.DatabaseConfig.mysql_database, **kw)

def create_table_manager_with_db(table_name="", db=None, **kw):
    assert isinstance(db, web.db.DB)
    kw["db_type"] = xconfig.DatabaseConfig.db_driver_sql
    return TableManager(table_name, db=db, mysql_database=xconfig.DatabaseConfig.mysql_database, **kw)

def create_record_table_manager(table_name=""):
    """默认使用 record.db 文件"""
    return create_table_manager_with_dbpath(table_name, xconfig.FileConfig.record_db_file)

def create_default_table_manager(table_name="", pk_name="id", dbpath="", **kw):
    kw["pk_name"] = pk_name
    if dbpath == "":
        dbpath = xconfig.FileConfig.record_db_file
    return create_table_manager_with_dbpath(table_name, dbpath=dbpath, **kw)

def get_default_db_instance():
    return get_db_instance(xconfig.FileConfig.record_db_file)

def get_db_instance(dbpath=""):
    db_driver_sql = xconfig.DatabaseConfig.db_driver_sql
    if db_driver_sql == "mysql":
        if DBPool.mysql_instance == None:
            db_host = xconfig.get_system_config("mysql_host")
            db_name = xconfig.get_system_config("mysql_database")
            db_user = xconfig.get_system_config("mysql_user")
            db_pw = xconfig.get_system_config("mysql_password")
            db_port = xconfig.get_system_config("mysql_port")

            if xconfig.DatabaseConfig.mysql_cloud_type == "sae":
                db_host = os.environ["MYSQL_HOST"]
                db_user = os.environ["MYSQL_USER"]
                db_pw = os.environ["MYSQL_PASS"]
                db_name = os.environ["MYSQL_DB"]

            db = web.db.MySQLDB(host=db_host, database=db_name,
                                user=db_user, pw=db_pw, port=db_port)
            db.dbname = "mysql"
            DBPool.mysql_instance = db
        return DBPool.mysql_instance
    assert dbpath != ""
    # db = MySqliteDB(db=dbpath)
    db = DBPool.get_sqlite_db(dbpath=dbpath)
    db.dbpath = dbpath
    return db

def is_table_exists(table_name=""):
    """判断表是否存在"""
    table_info = TableManager.get_table_info(table_name)
    return table_info != None

def get_table_by_name(table_name=""):
    # type: (str) -> TableProxy
    """通过表名获取操作代理"""
    table_info = TableManager.get_table_info(table_name)
    if table_info is None:
        raise Exception("table not found: %s" % table_name)
    db = get_db_instance(dbpath=table_info.dbpath)
    return TableProxy(db, table_name)

def get_all_tables(is_deleted=False):
    # type: (bool) -> list[TableProxy]
    """获取所有的sql-数据库代理实例"""
    result = []
    table_dict = TableManager.get_table_info_dict()
    for table_name in table_dict:
        table_info = table_dict[table_name]
        if is_deleted != table_info.is_deleted:
            continue
        proxy = get_table_by_name(table_name)
        result.append(proxy)
    return result


################################################
#  表定义
################################################

def init_test_table():
    """测试数据库"""
    table_name = "test"
    with create_record_table_manager(table_name) as manager:
        manager.add_column("int_value", "int", default_value=0)
        manager.add_column("float_value", "float", default_value=0.0)
        manager.add_column("text_value", "text", default_value="")
        manager.add_column("name", "text", default_value="test")
        manager.add_column("uuid", "varchar(32)", default_value="")
        manager.add_index("name")
        manager.add_index("uuid", is_unique=True)


def init_note_index_table():
    comment = "笔记索引"
    with create_default_table_manager("note_index", comment=comment) as manager:
        manager.add_column("name", "varchar(255)", "")
        # 文本内容长度
        manager.add_column("size", "bigint", 0)
        # 子节点数量
        manager.add_column("children_count", "bigint", 0)
        # 修改版本
        manager.add_column("version", "int", 0)
        # 类型, md, post, checklist, gallery, table
        manager.add_column("type", "varchar(32)", "")
        # 上级目录
        manager.add_column("parent_id", "bigint", 0)
        # 创建时间ctime
        manager.add_column("ctime", "datetime", DEFAULT_DATETIME)
        # 修改时间mtime
        manager.add_column("mtime", "datetime", DEFAULT_DATETIME)
        # 访问时间atime
        manager.add_column("atime", "datetime", default_value=DEFAULT_DATETIME)
        # 删除时间
        manager.add_column("dtime", "datetime", default_value=None, not_null=False)
        manager.add_column("is_deleted", "tinyint", 0, comment="逻辑删除标记")
        manager.add_column("is_public", "tinyint", 0, comment="是否是公开的笔记")
        
        # 创建者
        manager.add_column("creator", "varchar(64)", "", comment="创建者用户名快照")
        manager.add_column("creator_id", "bigint", 0)
        manager.add_column("level", "tinyint", 0)
        manager.add_column("tag_str", "varchar(255)", "")
        manager.add_column("visit_cnt", "bigint", 0, comment="访问次数")
        manager.add_column("order_type", "tinyint", 0, comment="排序方式")

        # 各种索引
        manager.add_index("parent_id")
        manager.add_index(["creator_id", "mtime"])
        manager.add_index(["creator_id", "ctime"])
        manager.add_index(["creator_id", "atime"])
        manager.add_index(["creator_id", "type"])

def init_note_history_index():
    comment = "笔记历史索引"
    with create_default_table_manager("note_history_index", comment=comment) as manager:
        manager.add_column("name", "varchar(255)", default_value="")
        manager.add_column("note_id", "bigint", default_value=0)
        manager.add_column("version", "int", default_value=0)
        manager.add_column("mtime", "datetime", default_value=DEFAULT_DATETIME)
        manager.add_column("creator_id", "bigint", default_value=0)

        manager.add_index("note_id")
        manager.add_index(["creator_id", "mtime"])


def init_note_relation_table():
    comment = "笔记关系"
    pk_name = "relation_id"
    with create_default_table_manager("note_relation", comment=comment, pk_name=pk_name) as manager:
        manager.add_column("ctime", "datetime", default_value=DEFAULT_DATETIME)
        manager.add_column("mtime", "datetime", default_value=DEFAULT_DATETIME)
        manager.add_column("user_id", "bigint", default_value=0)
        manager.add_column("relation_name", "varchar(50)", default_value="")
        manager.add_column("relation_note_id", "bigint", default_value=0, comment="关系名称对应的笔记ID")
        manager.add_column("note_id", "bigint", default_value=0, comment="源笔记ID")
        manager.add_column("target_id", "bigint", default_value=0, comment="目标笔记ID")

        manager.add_index("note_id")
        manager.add_index("target_id")

def init_share_info_table():
    comment = "分享记录"
    table_name = "share_info"
    with create_default_table_manager(table_name, comment=comment) as manager:
        manager.add_column("ctime", "datetime", DEFAULT_DATETIME, comment="创建时间")
        # 分享类型 {note_public, note_to_user, note_to_group}
        manager.add_column("share_type", "varchar(16)", "", comment="分享类型")
        manager.add_column("target_id", "bigint", 0, comment="被分享的对象ID")
        manager.add_column("from_id", "bigint", 0, comment="分享人ID")
        manager.add_column("to_id", "bigint", 0, comment="接收人ID")
        manager.add_column("visit_cnt", "bigint", 0, comment="访问次数")

        # 索引
        manager.add_index(["share_type", "ctime"])
        manager.add_index(["share_type", "visit_cnt"])
        manager.add_index("target_id")
        manager.add_index("from_id")
        manager.add_index("to_id")

def init_user_table():
    # 2017/05/21
    # 简单的用户表
    comment = "用户信息"
    with create_default_table_manager("user", comment=comment) as manager:
        manager.add_column("name", "varchar(64)", "")
        manager.add_column("password", "varchar(64)", "") # 始终为空
        manager.add_column("password_md5", "varchar(64)", "")
        manager.add_column("mobile", "varchar(32)", "")
        manager.add_column("salt", "varchar(64)", "")
        manager.add_column("ctime", "datetime", DEFAULT_DATETIME)
        manager.add_column("mtime", "datetime", DEFAULT_DATETIME)
        manager.add_column("token", "varchar(32)", "")
        manager.add_column("login_time", "datetime", DEFAULT_DATETIME)
        manager.add_column("status", "tinyint", 0)
        
        # 索引
        manager.add_index("name", is_unique=True)
        manager.add_index("token")
        # 删除的字段
        manager.drop_column("privileges", "text", "")


def init_user_session():
    # 2025/06/29
    # 用户会话信息
    comment = "用户会话信息"
    table_name = "user_session"
    with create_default_table_manager(table_name, comment=comment) as manager:
        manager.add_column("user_name", "varchar(64)", "")
        manager.add_column("user_id", "bigint", default_value=0)
        manager.add_column("sid", "varchar(50)", "")
        manager.add_column("token", "varchar(50)", "")
        manager.add_column("mobile", "varchar(32)", "")
        manager.add_column("login_time", "datetime", default_value=DEFAULT_DATETIME)
        manager.add_column("login_ip", "varchar(50)", "")
        manager.add_column("expire_time", "datetime", default_value=DEFAULT_DATETIME)

        # 索引
        manager.add_index("sid", is_unique=True)
        manager.add_index("user_id")
    
    TableConfig.disable_binlog(table_name)

def init_user_op_log_table():
    # 2023/07/15 用户操作日志，从kv迁移到sql
    with create_default_table_manager("user_op_log") as manager:
        manager.add_column("user_name", "varchar(64)", "")
        manager.add_column("ctime", "datetime", DEFAULT_DATETIME)
        manager.add_column("ip", "varchar(32)", "")
        manager.add_column("type", "varchar(32)", "")
        manager.add_column("detail", "text", "")


def init_message_table():
    """
    用来存储比较短的消息,消息和资料库的主要区别是消息存储较短的单一信息
    - 消息支持状态
    - 2017/05/29
    """
    table_name = "message"
    with create_table_manager_with_dbpath(table_name) as manager:
        manager.add_column("ctime", "datetime", DEFAULT_DATETIME)
        manager.add_column("mtime", "datetime", DEFAULT_DATETIME)
        manager.add_column("user",  "varchar(64)", "")
        # 用一个状态可以拍成一排
        # 消息的状态 0关注 50挂起 100已完成
        manager.add_column("status", "int", 0)
        manager.add_column("content", "text", "")
        # IP地址
        manager.add_column("ip", "varchar(32)", "")
        # 地址信息
        manager.add_column("location", "varchar(255)", "")
        # 索引
        manager.add_index(["user", "ctime", "status"])
        manager.add_index(["user", "status"])


def init_record_table():
    # 日志记录
    dbpath = xconfig.FileConfig.record_db_file
    comment = "通用日志记录"
    with create_table_manager_with_dbpath("record", dbpath=dbpath, comment=comment) as manager:
        manager.add_column("ctime", "datetime", DEFAULT_DATETIME)
        # 添加单独的日期，方便统计用，尽量减少SQL函数的使用
        manager.add_column("cdate", "date", "1970-01-01")
        manager.add_column("type",  "varchar(64)", "")
        # 自己把所有条件都组装到key里
        manager.add_column("key",  "varchar(100)", "")
        manager.add_column("value", "text", "")
        # 索引
        manager.add_index(["type", "ctime"])


def init_dict_table():
    """词典，和主库隔离
    @since 2018/01/14
    """
    comment = "词典"
    with create_default_table_manager("dictionary", comment=comment) as manager:
        manager.add_column("ctime", "datetime", DEFAULT_DATETIME)
        manager.add_column("mtime", "datetime", DEFAULT_DATETIME)
        manager.add_column("dict_type", "tinyint", default_value=1, comment="词典类型")
        manager.add_column("user_id", "bigint", 0, comment="用户ID")
        manager.add_column("key", "varchar(100)", "")
        manager.add_column("value", "text", "")
        manager.add_index(["dict_type", "user_id", "key"])

def init_note_tag_rel_table():
    """笔记标签绑定关系
    @since 2023/07/01
    """
    table_name = "note_tag_rel"
    comment = "笔记标签绑定关系(废弃)"
    with create_default_table_manager(table_name, is_deleted=True, comment=comment) as manager:
        manager.add_column("ctime", "datetime", DEFAULT_DATETIME)
        manager.add_column("user_id", "bigint", 0)
        manager.add_column("note_id", "varchar(32)", "")
        manager.add_column("tag_code", "varchar(32)", "")
        manager.add_index(["user_id", "tag_code"])

def init_tag_info_table():
    """标签信息
    @since 2023/09/09
    """
    table_name = "tag_info"
    comment = "标签信息"
    pk_name = "tag_id"
    with create_default_table_manager(table_name, comment=comment, pk_name=pk_name) as manager:
        manager.add_column("ctime", "datetime", default_value=DEFAULT_DATETIME)
        manager.add_column("mtime", "datetime", default_value=DEFAULT_DATETIME)
        manager.add_column("user_id", "bigint", default_value=0)
        manager.add_column("tag_type", "tinyint", default_value=0, comment="一级类型")
        manager.add_column("second_type", "tinyint", default_value=0, comment="二级类型")
        manager.add_column("tag_code",  "varchar(32)", default_value="")
        manager.add_column("score", "double", default_value=0.0)
        manager.add_column("amount", "bigint", default_value=0, comment="标签关联的对象数量")
        manager.add_column("visit_cnt", "bigint", default_value=0, comment="访问次数")
        manager.add_column("category_id", "bigint", default_value=0, comment="标签类别")
        manager.add_index("user_id")


def init_tag_bind_table():
    """标签绑定关系
    @since 2023/09/09
    """
    table_name = "tag_bind"
    comment = "标签绑定关系"
    with create_default_table_manager(table_name, comment=comment) as manager:
        manager.add_column("ctime", "datetime", DEFAULT_DATETIME)
        manager.add_column("user_id", "bigint", 0)
        manager.add_column("tag_type", "tinyint", default_value=0, comment="一级类型")
        manager.add_column("second_type", "tinyint", default_value=0, comment="二级类型,用于状态等字段")
        manager.add_column("tag_code",  "varchar(32)", default_value="")
        manager.add_column("target_id", "bigint", default_value=0)
        manager.add_column("sort_value", "varchar(50)", default_value="")
        manager.add_index(["user_id", "tag_code", "sort_value"])
        manager.add_index(["user_id", "target_id"])


def init_tag_category_table():
    """标签类别
    @since 2025/03/02
    """
    table_name = "tag_category"
    pk_name = "category_id"
    comment = "标签类别"
    with create_default_table_manager(table_name, comment=comment, pk_name=pk_name) as manager:
        manager.add_column("ctime", "datetime", default_value=DEFAULT_DATETIME)
        manager.add_column("mtime", "datetime", default_value=DEFAULT_DATETIME)
        manager.add_column("user_id", "bigint", default_value=0)
        manager.add_column("name", "varchar(100)", default_value="")
        manager.add_column("description", "text", default_value="")
        manager.add_column("sort_order", "int", default_value=0)
        manager.add_column("tag_amount", "int", default_value=0)


def init_file_info():
    """文件信息
    - 用户上传的文件都是只读的
    - 不同的file_info对象可以指向同一个文件path
    @since 2023/05/26
    """
    table_name = "file_info"
    comment = "文件索引信息"
    with create_default_table_manager(table_name, comment=comment) as manager:
        manager.add_column("ctime", "datetime", DEFAULT_DATETIME)
        manager.add_column("mtime", "datetime", DEFAULT_DATETIME)
        manager.add_column("fpath", "text", "")
        manager.add_column("ftype", "varchar(16)", "")
        manager.add_column("fsize", "bigint", 0)
        manager.add_column("user_id", "bigint", 0)
        manager.add_column("sha256", "varchar(100)", default_value="", comment="SHA256哈希值")
        manager.add_column("remark", "text", default_value="", comment="备注信息,比如上传的原始文件名")

        manager.add_index("user_id")
        manager.add_index("fpath(100)")
        manager.add_index(["ftype", "fpath(100)"])
        manager.add_index("sha256(30)")


def init_site_visit_log():
    """站点访问日志
    @since 2023/05/28
    """
    table_name = "site_visit_log"
    comment = "站点访问统计"
    with create_default_table_manager(table_name, comment=comment) as manager:
        manager.add_column("date", "date", "1970-01-01")
        manager.add_column("site", "varchar(64)", "")
        manager.add_column("ip", "varchar(64)", "")
        manager.add_column("count", "bigint", 0)
        manager.add_index(["date", "ip"])
    
    # 日志数据, 关闭profile
    TableConfig.disable_profile(table_name)
    TableConfig.disable_binlog(table_name)

def init_page_visit_log():
    """页面访问日志
    @since 2024/02/14
    """
    table_name = "page_visit_log"
    comment = "页面访问统计"
    with create_default_table_manager(table_name, comment=comment) as manager:
        manager.add_column("visit_time", "datetime", DEFAULT_DATETIME)
        manager.add_column("visit_cnt", "bigint", 0)
        manager.add_column("user_id", "bigint", 0)
        manager.add_column("url", "varchar(100)", "")
        manager.add_column("args", "text", "")
        manager.add_index(["user_id", "url"])
    
    # 日志数据, 关闭profile
    TableConfig.disable_profile(table_name)
    TableConfig.disable_binlog(table_name)

def init_job_table():
    """系统任务
    @since 2024/03/10
    """
    table_name = "t_job" # 避免关键字冲突
    comment = "系统任务"
    with create_default_table_manager(table_name, comment=comment) as manager:
        manager.add_column("ctime", "datetime", DEFAULT_DATETIME)
        manager.add_column("mtime", "datetime", DEFAULT_DATETIME)
        manager.add_column("job_type", "varchar(30)", "")
        manager.add_column("job_status", "tinyint", 0, comment="日志状态,0-初始化,1-执行中,2-执行成功,3-执行失败")
        manager.add_column("job_params", "text", "")
        manager.add_column("job_result", "text", "")
        manager.add_index(["job_type", "mtime"])

def init_lock_table():
    """分布式锁的表
    @since 2024/04/03
    """
    table_name = "t_lock" # 避免和关键字冲突
    comment = "系统锁"
    with create_default_table_manager(table_name, comment=comment) as manager:
        manager.add_column("ctime", "datetime", default_value=DEFAULT_DATETIME)
        manager.add_column("mtime", "datetime", default_value=DEFAULT_DATETIME)
        manager.add_column("lock_key", "varchar(128)", default_value="")
        manager.add_column("lock_token", "varchar(36)", default_value="", comment="锁的token")
        manager.add_column("timeout_time", "bigint", default_value=0, comment="锁超时时间,毫秒时间戳")
        manager.add_index("lock_key", is_unique=True)
    TableConfig.disable_binlog(table_name)


def init_system_sync_token_table():
    """数据同步从节点
    @since 2024/06/30
    """
    table_name = "system_sync_token"
    comment = "系统同步令牌"
    with create_default_table_manager(table_name, comment=comment) as manager:
        manager.add_column("ctime", "datetime", default_value=DEFAULT_DATETIME)
        manager.add_column("mtime", "datetime", default_value=DEFAULT_DATETIME)
        manager.add_column("token_holder", "varchar(128)", default_value="token的持有者")
        manager.add_column("token", "varchar(36)", default_value="", comment="访问令牌")
        manager.add_column("expire_time", "datetime", default_value=DEFAULT_DATETIME, comment="令牌有效期")
        manager.add_index("token_holder")
        manager.add_index("token")

def init_system_info_table():
    """系统信息表"""
    table_name = "system_info"
    comment = "系统信息"
    with create_default_table_manager(table_name, comment=comment) as manager:
        manager.add_column("ctime", "datetime", default_value=DEFAULT_DATETIME)
        manager.add_column("mtime", "datetime", default_value=DEFAULT_DATETIME)
        manager.add_column("info_key", "varchar(100)", default_value="", comment="")
        manager.add_column("info_value", "text", comment="")
        manager.add_column("version", "int", default_value=0, comment="版本号")
        manager.add_index("info_key", is_unique=True)

def init_msg_index_table():
    """随手记索引"""
    table_name = "msg_index"
    comment = "随手记索引"
    with create_default_table_manager(table_name, comment=comment) as manager:
        # 展示创建时间
        manager.add_column("ctime", "datetime", DEFAULT_DATETIME, comment="创建时间")
        # 实际创建时间
        manager.add_column("ctime_sys", "datetime", DEFAULT_DATETIME, comment="系统创建时间")
        # 修改时间
        manager.add_column("mtime", "datetime", DEFAULT_DATETIME, comment="修改时间")
        manager.add_column("user_id", "bigint", 0)
        manager.add_column("user_name", "varchar(64)", "")
        # 短信息的类型
        manager.add_column("tag", "varchar(16)", "")
        manager.add_column("date", "date", default_value=DEFAULT_DATE)
        # 状态变更的时间,比如task的完成时间
        manager.add_column("change_time", "datetime", DEFAULT_DATETIME, comment="状态变更时间")
        manager.add_column("sort_value", "varchar(50)", default_value="", comment="【废弃】排序字段")

        manager.add_index(["user_id", "ctime"])
        manager.add_index(["user_id", "mtime"])
        manager.add_index(["user_id", "tag", "change_time"])

        # 删除的索引
        manager.drop_index(["user_id", "sort_value"])
        manager.drop_index(["user_id", "tag", "sort_value"])

def init_msg_history_index():
    """随手记历史索引"""
    table_name = "msg_history_index"
    comment = "随手记历史索引"
    with create_default_table_manager(table_name, comment=comment) as manager:
        # 展示创建时间
        manager.add_column("ctime", "datetime", DEFAULT_DATETIME)
        manager.add_column("user_id", "bigint", 0)
        manager.add_column("msg_id", "bigint", 0)
        manager.add_column("msg_version", "bigint", 0)
        manager.add_index(["msg_id"])

def init_kv_store_table():
    kw = dict()
    kw["pk_name"] = "key"
    kw["pk_type"] = "varbinary(100)"
    kw["debug"] = xconfig.DatabaseConfig.db_debug
    kw["comment"] = "kv存储"
    dbpath = xconfig.FileConfig.kv_db_file
    with create_table_manager_with_dbpath("kv_store", dbpath=dbpath, **kw) as manager:
        manager.add_column("value", "longblob", default_value="")
        manager.add_column("version", "int", default_value=0)

def init_kv_zset_table(db=None):
    """使用关系型数据库模拟redis的zset结构"""
    comment = "模拟redis的zset"
    with create_table_manager_with_db("kv_zset", db=db, comment=comment) as manager:
        manager.add_column("key", "varchar(512)", "")
        manager.add_column("member", "varchar(512)", "")
        manager.add_column("score", "bigint", default_value=0)
        manager.add_column("version", "int", default_value=0)
        manager.add_index(["key(32)", "member(100)"], is_unique=True)
        manager.add_index(["key(32)", "score"])

def init_comment_index_table():
    """评论索引"""
    table_name = "comment_index"
    comment = "评论索引"
    with create_default_table_manager(table_name, comment=comment) as manager:
        # 展示创建时间
        manager.add_column("ctime", "datetime", DEFAULT_DATETIME)
        # 修改时间
        manager.add_column("mtime", "datetime", DEFAULT_DATETIME)
        manager.add_column("type", "varchar(16)", default_value="", comment="评论类型")
        manager.add_column("user_id", "bigint", 0, comment="用户ID")
        manager.add_column("target_id", "bigint", 0, comment="关联的对象ID")
        manager.add_column("pin_level", "tinyint", default_value=0, comment="置顶级别,0-普通,1-置顶")
        
        manager.add_index(["user_id", "ctime"])
        manager.add_index("target_id")


def init_user_note_log():
    """用户笔记日志, 从kv数据迁移过来
    @since 2023/10/22
    """
    table_name = "user_note_log"
    comment = "笔记用户日志"
    with create_default_table_manager(table_name, comment=comment) as manager:
        manager.add_column("note_id", "bigint", 0)
        manager.add_column("user_id", "bigint", 0)
        manager.add_column("atime", "datetime", DEFAULT_DATETIME)
        manager.add_column("visit_cnt", "bigint", 0)
        manager.add_index(["user_id", "note_id"], is_unique=True)

def init_user_op_log():
    """用户操作日志, 从kv数据迁移过来
    @since 2024/02/14
    """
    table_name = "user_op_log"
    comment = "笔记操作日志"
    with create_default_table_manager(table_name, comment=comment) as manager:
        manager.add_column("user_id", "bigint", 0)
        manager.add_column("ctime", "datetime", DEFAULT_DATETIME)
        manager.add_column("type", "varchar(64)", "")
        manager.add_column("detail", "varchar(256)", "")
        manager.add_column("ip", "varchar(64)", "")
        manager.add_index(["user_id", "ctime"])

def init_month_plan_index():
    """月度计划索引
    @since 2023/11/05
    """
    table_name = "month_plan_index"
    comment = "月度计划索引"
    with create_default_table_manager(table_name, comment=comment) as manager:
        manager.add_column("user_id", "bigint", default_value=0)
        manager.add_column("month", "varchar(20)", default_value="")
        manager.add_index("user_id")
    TableConfig.disable_binlog(table_name)

def init_txt_info_index():
    """txt文件索引
    @since 2023/11/18
    """
    table_name = "txt_info_index"
    comment = "txt文件索引"
    with create_default_table_manager(table_name, comment=comment) as manager:
        manager.add_column("user_id", "bigint", default_value=0)
        manager.add_column("path", "varchar(255)", default_value="")
        manager.add_index("user_id")
    TableConfig.disable_binlog(table_name)        

def init_search_history_table():
    """搜索记录
    @since 2024/10/26
    """
    table_name = "search_history"
    comment = "搜索记录"
    with create_default_table_manager(table_name, comment=comment) as manager:
        manager.add_column("ctime", "datetime", default_value=DEFAULT_DATETIME, comment="创建时间")
        manager.add_column("user_id", "bigint", default_value=0)
        manager.add_column("cost_time_ms", "bigint", default_value=0, comment="毫秒耗时")
        manager.add_column("search_type", "varchar(20)", default_value="")
        manager.add_column("search_key", "varchar(100)", default_value="")
        manager.add_index("user_id")

def DBWrapper(dbpath, tablename):
    db = MySqliteDB(db=dbpath)
    return TableProxy(db, tablename)


def get_file_table():
    return get_table_by_name("file")


def get_note_table():
    return get_file_table()


def get_note_history_table():
    dbpath = xconfig.FileConfig.record_db_file
    return DBWrapper(dbpath, "note_history")


def get_note_content_table():
    return DBWrapper(xconfig.DB_PATH, "note_content")


def get_file_tag_table():
    return DBWrapper(xconfig.DB_PATH, "file_tag")


def get_schedule_table():
    return DBWrapper(xconfig.DB_PATH, "schedule")


def get_user_table():
    return get_table_by_name("user")


def get_message_table():
    return get_table_by_name("message")


def get_record_table():
    return get_table_by_name("record")


def get_dict_table():
    return get_table_by_name("dictionary")


get_dictionary_table = get_dict_table


def get_file_info_table():
    return get_table_by_name("file_info")


def init_backup_table(tablename, db, dbpath=""):
    table_info = TableManager.get_table_info(tablename)
    if table_info == None:
        raise Exception("table not defined: %s" % tablename)
    pk_name = table_info.pk_name
    with TableManager(tablename, db=db, is_backup=True, dbpath = dbpath, pk_name=pk_name) as manager:
        for col in table_info.columns:
            manager.add_column(col.name, *col.args, **col.kw)

        for args, kw in table_info.indexes:
            manager.add_index(*args, **kw)

    proxy = TableProxy(db, tablename)
    proxy.enable_binlog = False
    return proxy


def get_table(table_name, dbpath=None):
    """获取数据库表，表的创建和访问不必在xtables中定义
    @since 2019/04/11
    """
    return get_table_by_name(table_name)

def move_sqlite_to_backup(db_name=""):
    source_path = xconfig.FileConfig.get_db_path(db_name)
    if not os.path.exists(source_path):
        return
    target_path = xconfig.FileConfig.get_backup_db_path(db_name)
    fsutil.mvfile(source_path, target_path, rename_on_conflict=True)

class DBProfileLogger(interfaces.ProfileLogger):

    def __init__(self):
        self.db = dbutil.get_table("sys_log")
        self.db.binlog_enabled = False

    def log(self, log):
        self.db.insert(log, id_type="timeseq")


@xutils.log_init_deco("xtables")
def init():
    TableManager.clear_table_dict()
    web.db.config.debug_sql = xconfig.DatabaseConfig.db_debug

    TableConfig.enable_binlog = xconfig.DatabaseConfig.binlog
    TableConfig.enable_auto_ddl = xconfig.DatabaseConfig.db_auto_ddl

    if xconfig.DatabaseConfig.db_profile_table_proxy:
        dbutil.register_table("sys_log", "系统日志")
        TableProxy.profile_logger = DBProfileLogger()
        TableProxy.log_profile = True
    
    init_dict_table()    
    init_record_table()
    init_user_table()
    init_user_session()
    init_file_info()
    
    # 持久化任务表
    init_job_table()
    # 分布式锁表
    init_lock_table()
    # 数据同步
    init_system_sync_token_table()
    init_system_info_table()
    
    # 统计信息
    init_site_visit_log()
    init_page_visit_log()
    
    # 标签相关
    init_note_tag_rel_table() # 已删除, 占位防止冲突
    init_tag_info_table()
    init_tag_bind_table()
    init_tag_category_table()

    # 评论相关
    init_comment_index_table()

    # 随手记
    init_msg_index_table()
    init_msg_history_index()
    
    # 笔记索引
    init_note_index_table()
    init_note_history_index()
    init_note_relation_table()

    init_user_note_log()
    init_user_op_log()
    init_month_plan_index()
    init_txt_info_index()

    # 通用的分享记录
    init_share_info_table()
    
    # KV表
    init_kv_store_table()
    init_search_history_table()

