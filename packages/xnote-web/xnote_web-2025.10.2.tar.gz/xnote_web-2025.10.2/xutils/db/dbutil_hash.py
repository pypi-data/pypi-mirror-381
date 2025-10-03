# -*- coding:utf-8 -*-
# @author xupingmao
# @since 2021/12/04 15:35:23
# @modified 2022/04/05 21:15:18
# @filename dbutil_hash.py

from xutils import Storage
from xutils import textutil
from xutils.db import dbutil_base
from xutils.db.dbutil_base import (
    db_get, db_put, db_delete, 
    check_table_name, 
    get_table_info, TableInfo, 
    count_table, prefix_iter
)
from xutils.db.encode import encode_str, decode_str
from xutils.db import filters
from xutils import interfaces

class KvHashTable:
    """基于Kv存储的哈希表结构
    注: LdbTable可以覆盖 KvHashTable 的功能, 如果不考虑极致的性能, 建议使用 LdbTable+索引 的方式
    put -> LdbTable.update_by_id
    get -> LdbTable.get_by_id
    """

    def __init__(self, table_name = "", user_name = None, key_name = "_key", 
                 cache = interfaces.empty_cache, cache_expire=60):
        first_table = table_name.split(":")[0]
        check_table_name(first_table)

        table_info = get_table_info(first_table)
        assert isinstance(table_info, TableInfo)
        
        self.table_name = table_name
        self.key_name = key_name
        self.user_name = user_name
        self.prefix = table_name
        self.first_table = first_table
        self.cache = cache
        self.cache_expire = cache_expire

        if user_name != None and user_name != "":
            self.prefix += ":" + encode_str(user_name)
        
        if table_info.check_user:
            assert user_name != None
            assert user_name != ""

        if self.prefix[-1] != ":":
            self.prefix += ":"
    
    def with_user(self, user_name):
        """请使用 sub_table 方法
        """
        assert user_name != ""
        assert user_name != None
        assert self.user_name == None

        return KvHashTable(self.table_name, user_name = user_name)

    def sub_table(self, sub_table=""):
        assert sub_table != ""
        return KvHashTable(self.table_name + ":" + encode_str(sub_table))

    def _check_key(self, key):
        if not isinstance(key, str):
            raise Exception("KvHashTable_param_error: expect str key")

    def _check_value(self, obj):
        pass

    def build_key(self, key):
        return self.prefix + encode_str(key)

    def put(self, key, value, batch = None):
        """通过key来设置value，这个key是hash的key，不是ldb的key
        @param {string} key hash的key
        @param {object} value hash的value
        """
        self._check_key(key)
        self._check_value(value)

        row_key = self.build_key(key)
        
        if batch != None:
            batch.put(row_key, value)
        else:
            db_put(row_key, value)
        
        self.cache.delete(key)

    def get(self, key, default_value = None):
        """通过key来查询value，这个key是hash的key，不是ldb的key
        @param {string} key hash的key
        @param {object} default_value 如果值不存在，返回默认值
        """
        cache_value = self.cache.get(key)
        if cache_value != None:
            return cache_value
        row_key = self.build_key(key)
        result = db_get(row_key, default_value)
        if result != None:
            self.cache.put(key, result, expire=self.cache_expire)
        return result

    def iter(self, offset = 0, limit = 20, reverse = False, filter_func = None, where=None):
        """hash表的迭代器
        @yield key, value
        """

        if where != None:
            filter_func = filters.create_func_by_where(where, filter_func)

        prefix_len = len(self.prefix)
        for key, value in prefix_iter(self.prefix, filter_func = filter_func, 
                offset = offset, limit = limit, reverse = reverse, include_key = True):
            yield decode_str(key[prefix_len:]), value

    def list(self, *args, **kw):
        return list(self.iter(*args, **kw))

    def dict(self, *args, **kw):
        result = Storage()
        for key, value in self.iter(*args, **kw):
            result[key] = value
        return result

    def delete(self, key, batch = None):
        row_key = self.build_key(key)

        if batch != None:
            batch.delete(row_key)
        else:
            db_delete(row_key)
        
        self.cache.delete(key)
    
    def batch_delete(self, keys=[]):
        if len(keys) == 0:
            return
        db_keys = []
        for key in keys:
            db_keys.append(self.build_key(key))
        dbutil_base.db_batch_delete(db_keys)

        self.cache.batch_delete(keys)

    def count(self, prefix = None):
        if prefix != None:
            key_prefix = self.prefix + encode_str(prefix)
        else:
            key_prefix = self.prefix

        return count_table(key_prefix)
    
    def first(self, where = None):
        # type: (None|dict) -> tuple[str|None, object]
        records = self.list(limit=1, where = where)
        if len(records) > 0:
            return records[0]
        return None, None
    
    def last(self):
        # type: () -> tuple[str|None, object]
        records = self.list(limit = 1, reverse = True)
        if len(records) > 0:
            return records[0]
        else:
            return None, None

class LdbHashTable(KvHashTable):
    pass


class LargeKeyHashTable:
    """针对大key优化的hashtable,使用md5哈希后的值作为数据库的key"""
    
    def __init__(self, table_name=""):
        check_table_name(table_name)
        self.table_name = table_name
        self.prefix = table_name + ":"

    def build_key(self, key):
        return self.prefix + textutil.md5_hex(key)
    
    def _check_key(self, key):
        if not isinstance(key, str):
            raise Exception("KvHashTableV2_param_error: expect str key")

    def _check_value(self, value):
        pass

    def get(self, key, default_value = None):
        """通过key来查询value，这个key是hash的key，不是ldb的key
        @param {string} key hash的key
        @param {object} default_value 如果值不存在，返回默认值
        """
        row_key = self.build_key(key)
        item_dict = db_get(row_key)
        if item_dict == None:
            return default_value
        assert isinstance(item_dict, dict)
        return item_dict.get(key, default_value)
    
    def get_row_dict(self, row_key=""):
        item_dict = db_get(row_key)
        if item_dict == None:
            return None
        assert isinstance(item_dict, dict)
        return item_dict

    def put(self, key, value, batch = None):
        """通过key来设置value，这个key是hash的key，不是ldb的key
        @param {string} key hash的key
        @param {object} value hash的value
        """
        self._check_key(key)
        self._check_value(value)

        row_key = self.build_key(key)
        item_dict = self.get_row_dict(row_key)
        if item_dict == None:
            item_dict = {}
        item_dict[key] = value

        if batch != None:
            batch.put(row_key, item_dict)
        else:
            db_put(row_key, item_dict)


    def delete(self, key, batch = None):
        row_key = self.build_key(key)
        item_dict = self.get_row_dict(row_key)
        if item_dict == None:
            return
        if len(item_dict) == 0:
            return
        
        item_dict.pop(key, None)

        if len(item_dict) > 0:
            if batch != None:
                batch.put(row_key, item_dict)
            else:
                db_put(row_key, item_dict)
        else:
            if batch != None:
                batch.delete(row_key)
            else:
                db_delete(row_key)
