# -*- coding:utf-8 -*-
"""
@Author       : xupingmao
@email        : 578749341@qq.com
@Date         : 2022-02-12 18:13:41
@LastEditors  : xupingmao
@LastEditTime : 2024-07-01 01:59:14
@FilePath     : /xnote/handlers/system/system_sync/node_leader.py
@Description  : 描述
"""


import threading
import time
import xutils
import logging
import os

from xnote.core import xauth, xconfig, xtables

from xutils import dateutil
from xutils import textutil
from xutils import Storage
from xutils import webutil
from xutils import dbutil
from xutils import fsutil
from xutils.db.binlog import BinLog, BinLogOpType, BinLogRecord

from .node_base import NodeManagerBase, convert_follower_dict_to_list
from .node_base import get_system_port
from .models import LeaderStat
from .models import SystemSyncToken
from .models import FileIndexInfo
from .models import FollowerInfo
from .models import LeaderBaseInfo
from .dao import ClusterConfigDao
from .dao import SystemSyncTokenDao
from .config import MAX_FOLLOWER_SIZE
from handlers.fs.fs_helper import FileInfoDao
from .system_sync_indexer import count_fs_index
from . import system_sync_indexer

class Leader(NodeManagerBase):

    _lock = threading.RLock()
    FOLLOWER_DICT = dict() # type: dict[str, FollowerInfo]
    binlog = BinLog.get_instance()
    log_debug = False

    def get_follower_url(self, node_id="", port=""):
        client_ip = webutil.get_client_ip()
        url = "{ip}:{port}#{node_id}".format(
            ip=client_ip, port=port, node_id=node_id)
        return url

    def get_follower_info(self, client_id: str):
        client_info = self.FOLLOWER_DICT.get(client_id)
        if client_info == None:
            client_info = FollowerInfo()
            client_info.init()
            client_info.client_id = client_id
            client_info.update_connect_info()
        return client_info

    def check_follower_count(self, client_id):
        if client_id not in self.FOLLOWER_DICT:
            return len(self.FOLLOWER_DICT) <= MAX_FOLLOWER_SIZE
        return True

    def update_follower_info(self, client_info: FollowerInfo):
        url = client_info.url
        self.FOLLOWER_DICT[url] = client_info

    def get_follower_list(self):
        follower_dict = self.FOLLOWER_DICT
        return convert_follower_dict_to_list(follower_dict)

    def get_follower_dict(self):
        return self.FOLLOWER_DICT

    def get_leader_url(self):
        return "http://127.0.0.1:%s" % get_system_port()

    def get_leader_node_id(self):
        return self.get_node_id()

    def get_leader_token(self):
        token = ClusterConfigDao.get_leader_token()
        if token is None or token == "":
            token = textutil.create_uuid()
            ClusterConfigDao.put_leader_token(token)

        return token

    def get_node_id(self):
        return xconfig.get("system.node_id")

    def get_ip_whitelist(self):
        return ClusterConfigDao.get_follower_whitelist()

    def sync_for_home_page(self):
        pass

    def get_fs_index_count(self):
        return count_fs_index()

    def get_system_version(self):
        return xconfig.SystemConfig.get_str("version")

    def remove_expired_followers(self):
        for key in self.FOLLOWER_DICT.copy():
            info = self.FOLLOWER_DICT[key]
            if info.is_expired():
                del self.FOLLOWER_DICT[key]

    def get_leader_info(self):
        return LeaderBaseInfo(token=self.get_leader_token(),
                    node_id=self.get_node_id(),
                    fs_index_count=self.get_fs_index_count(),
                    system_version=self.get_system_version(),
                    binlog_last_seq=self.binlog.last_seq)

    def get_stat(self, port=""):
        admin_info = xauth.get_user_by_name("admin")
        assert admin_info != None
        admin_token = admin_info.token
        fs_index_count = self.get_fs_index_count()

        result = LeaderStat()
        result.code = "success"
        result.timestamp = int(time.time())
        result.system_version = self.get_system_version()
        result.admin_token = admin_token
        result.fs_index_count = fs_index_count
        result.fs_max_index = FileInfoDao.get_max_id()

        node_id = xutils.get_argument_str("node_id")

        url = self.get_follower_url(node_id=node_id, port=port)
        with self._lock:
            if not self.check_follower_count(url):
                result.code = "403"
                result.message = "Too many connects"
                return result

            follower = self.get_follower_info(url)
            follower.update_ping_info()
            follower.fs_sync_offset = xutils.get_argument_str("fs_sync_offset")
            follower.fs_index_count = fs_index_count
            follower.admin_token = admin_token
            follower.node_id = node_id
            follower.url = url

            self.update_follower_info(follower)
            self.remove_expired_followers()

        result.follower_dict = self.get_follower_dict()
        result.leader = self.get_leader_info()

        return result

    def skip_db_sync(self, key):
        # type: (str|int) -> bool
        if isinstance(key, int):
            return False
        skipped_prefix_tuple = ("_binlog:", "_index$", "cluster_config:",
                                "fs_index:", "fs_sync_index:", "fs_sync_index_copy:", "sys_log:")
        table_name = key.split(":", 1)[0]
        if table_name.find("$")>=0:
            return True
        return key.startswith(skipped_prefix_tuple)

    def list_binlog(self, last_seq=0, limit=20, include_req_seq=True):
        """列出指定条件的binlog
        include_req_seq: 是否包含请求的seq对应的binlog
        """
        sync_diff = self.binlog.last_seq - last_seq
        binlog_size = self.binlog.count_size()
        out_of_sync = sync_diff > self.binlog.count_size()
        is_broken = False
        broken_reason = ""

        if last_seq <= 0:
            broken_reason = "sync_broken: last_seq<=0"
            is_broken = True
        if last_seq > self.binlog.last_seq:
            broken_reason = "sync_broken: last_seq=%s, binlog.last_seq=%s" % (last_seq, self.binlog.last_seq)
            is_broken = True
        if out_of_sync:
            broken_reason = "sync_broken: sync_diff=%s, binlog_size=%s"% (sync_diff, binlog_size)
            is_broken = True
        
        if is_broken:
            return webutil.FailedResult(code="sync_broken", message="同步中断，请重新同步: %s" % broken_reason)

        def map_func(key, value):
            record_key = value.get("key")
            if self.skip_db_sync(record_key):
                return None
            table_name, seq = key.split(":")
            value["seq"] = self.binlog._unpack_id(seq)
            return value

        data_list = []
        # 预读一位 用于获取下一个key
        binlogs = self.binlog.list(last_seq, limit + 1, map_func=map_func)
        if self.log_debug:
            logging.debug("binlogs:%s", binlogs)

        for log in binlogs:
            assert isinstance(log, Storage)
            if not include_req_seq and log.seq == last_seq:
                continue
            
            log = self.process_log(log)
            if log != None:
                data_list.append(log)

        return webutil.SuccessResult(data_list[:limit])
    
    def process_file_log(self, log):
        value_dict = log.value
        value = FileIndexInfo(**value_dict)

        fpath = value.fpath
        if os.path.isdir(fpath):
            value.ftype = "dir"
        else:
            value.ftype = fsutil.get_file_ext(fpath)
        value.exists = os.path.exists(fpath)
        value.sha1_sum = fsutil.get_sha1_sum(fpath)
        
        log.value = value
        return log
    
    def process_log(self, log: BinLogRecord):
        # TODO 补充单元测试
        optype = log.optype
        if optype in (BinLogOpType.sql_upsert, BinLogOpType.sql_delete):
            table_name = log.table_name
            table_info = xtables.TableManager.get_table_info(table_name)
            if table_info == None:
                # 无效的binlog
                return None
            table = xtables.get_table_by_name(table_name)
            pk_name = table_info.pk_name
            pk_value = log.key
            db_record = table.select_first(where={pk_name: pk_value})
            log.value = db_record
            if db_record == None:
                log.optype = BinLogOpType.sql_delete
        elif optype in (BinLogOpType.file_upload, BinLogOpType.file_rename, BinLogOpType.file_delete):
            return self.process_file_log(log)
        elif optype == BinLogOpType.put:
            key = log.key
            log.value = dbutil.get(key)
            if log.value == None:
                log.optype = BinLogOpType.delete
        
        return log

    def list_db(self, last_key, limit=20):
        def filter_func(key, value):
            if self.skip_db_sync(key):
                return False
            return True

        result = []
        for key, value in dbutil.prefix_list("", key_from=last_key,
                                             limit=limit,
                                             include_key=True,
                                             scan_db=True,
                                             filter_func=filter_func):
            record = dict(key=key, value=value)
            result.append(record)
        return dict(binlog_last_seq=self.binlog.last_seq, rows=result)

    def refresh_token(self, leader_token="", node_id="", port=""):
        if node_id == "":
            return webutil.FailedResult(code="404", message="node_id 为空")
        if port == "":
            return webutil.FailedResult(code="404", message="port为空")
        
        follower_name = self.get_follower_url(node_id=node_id, port=port)
        if leader_token == self.get_leader_token():
            # build token
            token_info = SystemSyncTokenDao.get_by_holder(follower_name)
            if token_info == None:
                token_info = SystemSyncToken()
                token_info.token_holder = follower_name
            
            unixtime = dateutil.get_seconds()
            token_info.expire_time = dateutil.format_datetime(unixtime + 3600)
            token_info.token = textutil.create_uuid()
            SystemSyncTokenDao.upsert(token_info)
            return webutil.SuccessResult(data=token_info)
        else:
            return webutil.FailedResult(code="403", message="无效的token")
        

    def list_files(self, last_id=0):
        return system_sync_indexer.list_files(last_id=last_id)