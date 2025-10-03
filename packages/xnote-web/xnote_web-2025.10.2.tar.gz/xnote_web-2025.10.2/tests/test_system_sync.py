# -*- coding:utf-8 -*-
"""
@Author       : xupingmao
@email        : 578749341@qq.com
@Date         : 2022-05-28 22:28:31
@LastEditors  : xupingmao
@LastEditTime : 2024-06-30 17:02:14
@FilePath     : /xnote/tests/test_system_sync.py
@Description  : 描述
"""

import os
import re

from .a import *
from urllib.parse import urlparse, parse_qs, unquote

from xutils import dbutil, fsutil
from xutils import textutil
from xutils import netutil
from xutils import dateutil
from xutils import jsonutil
from xutils import webutil
from xnote.core import xauth
from xnote.core import xconfig
from xnote.core import xnote_event
from xnote.service.system_info_service import SystemInfoService

from . import test_base
from handlers.system.system_sync.node_follower import DBSyncer
from handlers.system.system_sync.dao import ClusterConfigDao
from handlers.system.system_sync.models import LeaderStat
from handlers.system.system_sync import system_sync_proxy

app = test_base.init()
json_request = test_base.json_request
request_html = test_base.request_html
BaseTestCase = test_base.BaseTestCase

DBSyncer.MAX_LOOPS = 5
DBSyncer.FULL_SYNC_MAX_LOOPS = 5

def get_test_access_token(readonly=False):
    from handlers.system.system_sync.models import SystemSyncToken
    from handlers.system.system_sync.dao import SystemSyncTokenDao
    follower_name = "test"
    token_info = SystemSyncTokenDao.get_by_holder(follower_name)
    if token_info == None:
        token_info = SystemSyncToken()
        token_info.token_holder = follower_name

    if readonly:
        return token_info.token

    token_info.token = textutil.create_uuid()
    unixtime = dateutil.get_seconds()
    token_info.expire_time = dateutil.format_datetime(unixtime+3600)
    SystemSyncTokenDao.upsert(token_info)
    return token_info.token

class LeaderNetMock:

    def http_get(self, url, charset=None, params=None):
        print("url:{url}, params:{params}".format(**locals()))
        access_token = ""

        if params != None:
            url = netutil._join_url_and_params(url, params)
            access_token = params.get("token", "")

        if access_token == "":
            struct_url = netutil.parse_url(url)
            access_token = struct_url.get_single_param("token")

        if "get_stat" in url:
            assert access_token == get_test_access_token(readonly=True)
            return self.http_get_stat()

        if "list_db" in url:
            assert access_token == get_test_access_token(readonly=True)
            return self.http_list_db(url)

        if "list_binlog" in url:
            assert access_token == get_test_access_token(readonly=True)
            return self.http_list_binlog(url)
        
        if "refresh_token" in url:
            return self.refresh_token(url)

        raise Exception("unsupported url:%s" % url)

    def refresh_token(self, url):
        from handlers.system.system_sync.dao import SystemSyncTokenDao
        follower_name = "test"
        token_info = SystemSyncTokenDao.get_by_holder(follower_name)
        result = webutil.SuccessResult(token_info)
        return jsonutil.tojson(result)

    def http_get_stat(self):
        leader_stat = LeaderStat()
        leader_stat.access_token = get_test_access_token(readonly=True)
        return textutil.tojson(leader_stat)

    def http_list_db(self, url):
        result = urlparse(url)
        params = parse_qs(result.query)
        last_key = params.get("last_key")

        if last_key != None:
            last_key = last_key[0]
            last_key == unquote(last_key)

        if last_key == "my_config:test:key2":
            result = dict(code="success",
                          data=dict(
                              binlog_last_seq=2345,
                              rows=[]
                          ))
        else:
            result = dict(code="success",
                          data=dict(
                              binlog_last_seq=1234,
                              rows=[
                                  {
                                      "key": "my_config:test:key1",
                                      "value": "value1"
                                  },
                                  {
                                      "key": "my_config:test:key2",
                                      "value": "value2"
                                  }
                              ]))
        return textutil.tojson(result)

    def http_list_binlog(self, url):
        result = urlparse(url)
        params = parse_qs(result.query)
        last_seq = params.get("last_seq")[0]

        print("[NetMock] last_seq=%s" % last_seq)

        if last_seq == "2346":
            return """
            {
                "code": "success",
                "data": [
                    {
                        "optype": "put",
                        "seq": 2346,
                        "key": "my_table:1",
                        "value": {"name":"Ada", "age":20}
                    }
                ]
            }
            """

        return """
        {
            "code": "success",
            "data": [
                {
                    "optype": "delete",
                    "seq": 2345,
                    "key": "my_table:2"
                },
                {
                    "optype": "put",
                    "seq": 2346,
                    "key": "my_table:1",
                    "value": {"name":"Ada", "age":20}
                }
            ]
        }
        """


class TestSystemSync(BaseTestCase):

    def get_access_token(self):
        return get_test_access_token()
    
    def get_leader_token(self):
        token = textutil.create_uuid()
        ClusterConfigDao.put_leader_token(token)
        return token
    
    def init_leader_config(self):
        token = textutil.create_uuid()
        ClusterConfigDao.put_leader_token(token)
        ClusterConfigDao.put_leader_host("http://127.0.0.1:3333")

    def test_system_sync(self):
        access_token = self.get_access_token()
        self.check_OK("/system/sync?p=home")
        self.check_OK("/system/sync?p=get_stat&token=" + access_token)

    def test_system_get_stat(self):
        self.init_leader_config()
        admin_token = self.get_access_token()
        resp = json_request("/system/sync?p=get_stat&token=" + admin_token)

        print("get_stat resp:{resp}".format(resp=resp))
        self.assertEqual("success", resp["code"])
        self.assertIsNotNone(resp["leader"])
        self.assertIsNotNone(resp["follower_dict"])

    def test_system_ping(self):
        netutil.set_net_mock(LeaderNetMock())
        try:
            self.init_leader_config()
            admin_token = self.get_access_token()
            resp = json_request("/system/sync?p=ping&token=" + admin_token)
            print("ping resp:{resp}".format(resp=resp))
            self.assertEqual("success", resp["code"])
            self.assertIsNotNone(resp["data"])
        finally:
            netutil.set_net_mock(None)

    def test_system_sync_db_full(self):
        from handlers.system.system_sync.system_sync_controller import FOLLOWER
        netutil.set_net_mock(LeaderNetMock())

        try:
            self.get_access_token()
            self.init_leader_config()

            FOLLOWER._debug = True
            db_syncer = FOLLOWER.db_syncer
            db_syncer.debug = True
            db_syncer.put_db_sync_state("full")
            
            # 全量同步
            FOLLOWER.sync_db_from_leader()

            self.assertEqual(db_syncer.get_db_sync_state(), "binlog")
            self.assertEqual(db_syncer.get_binlog_last_seq(), 1234) # 全量同步不会更新 last_seq
        finally:
            netutil.set_net_mock(None)

    def test_system_sync_db_binlog(self):
        from handlers.system.system_sync.system_sync_controller import FOLLOWER
        netutil.set_net_mock(LeaderNetMock())

        try:
            self.get_access_token()
            self.init_leader_config()

            FOLLOWER._debug = True
            db_syncer = FOLLOWER.db_syncer
            db_syncer.debug = True
            db_syncer.put_db_sync_state("binlog")
            db_syncer.put_binlog_last_seq(1234)
            
            # 增量同步
            FOLLOWER.sync_db_from_leader()

            self.assertEqual(db_syncer.get_db_sync_state(), "binlog")
            self.assertEqual(db_syncer.get_binlog_last_seq(), 2346)
        finally:
            netutil.set_net_mock(None)


    def test_system_sync_db_broken(self):
        from handlers.system.system_sync.system_sync_controller import FOLLOWER
        admin_token = self.get_access_token()
        self.init_leader_config()

        class MockedClient(system_sync_proxy.HttpClient):
            def __init__(self, **kw):
                pass
            
            def list_binlog(self, last_seq):
                return dict(code="sync_broken")
            
            def list_db(self, last_key=""):
                return """{
                    "code": "success",
                    "data": {
                        "binlog_last_seq": 1234,
                        "rows": []
                    }
                }
                """

        FOLLOWER._debug = True
        FOLLOWER.db_syncer.put_db_sync_state("binlog")
        result = FOLLOWER.db_syncer.sync_by_binlog(MockedClient())
        self.assertEqual(result, "sync_by_full")
        self.assertEqual(1234, FOLLOWER.db_syncer.get_binlog_last_seq())
    
    def test_is_token_active(self):
        from handlers.system.system_sync.system_sync_controller import FOLLOWER
        result = """
        {
            "code": "success",
            "timestamp": 1654227462,
            "system_version": "v2.9-dev-2022.06.03",
            "admin_token": "fake-token",
            "fs_index_count": 10960,
            "follower_dict": {
                "127.0.0.1:2222#follower": {
                    "ping_time_ts": 1654227411.8821118,
                    "client_id": "127.0.0.1:2222#follower",
                    "connected_time": "2022-06-03 11:20:16",
                    "connected_time_ts": 1654226416.2453492,
                    "ping_time": "2022-06-03 11:36:51",
                    "fs_sync_offset": "00000001654174803260#/data/path/to/file.txt",
                    "fs_index_count": 10960,
                    "admin_token": "fake-token",
                    "node_id": "follower",
                    "url": "127.0.0.1:2222#follower"
                }
            }
        }
        """
        result_dict = textutil.parse_json(result)
        result_obj = LeaderStat.from_dict(result_dict)
        assert result_obj != None
        result_obj.access_token = self.get_access_token()
        FOLLOWER.update_ping_result(result_obj)
        self.assertTrue(FOLLOWER.is_token_active())

    def test_build_fs_sync_index(self):
        self.check_OK("/system/sync?p=build_index")
    
    def test_list_files(self):
        from handlers.system.system_sync import system_sync_indexer

        testfile_1 = os.path.join(xconfig.UPLOAD_DIR, "fs_sync_test_01.txt")
        testfile_2 = os.path.join(xconfig.UPLOAD_DIR, "fs_sync_test_02.txt")
        fsutil.touch(testfile_1)
        fsutil.touch(testfile_2)

        manager = system_sync_indexer.FileSyncIndexManager()
        manager.build_full_index()
        result = manager.list_files(last_id=0)
        self.assertTrue(len(result) > 0)
    
    def test_leader_list_binlog(self):
        from handlers.system.system_sync.system_sync_controller import LEADER
        from xutils.db.binlog import BinLog
        binlog = BinLog.get_instance()
        binlog.set_max_size(1000)
        binlog.set_enabled(True)

        for i in range(20):
            binlog.add_log("put", "test", i)
        last_seq = binlog.last_seq - 10
        result = LEADER.list_binlog(last_seq=last_seq, limit=20)
        assert result.success == True

    def test_leader_list_file_binlog(self):
        from handlers.system.system_sync.system_sync_controller import LEADER
        from handlers.system.system_sync.system_sync_indexer import on_fs_upload, FileIndexCheckManager
        from xutils.db.binlog import BinLog, BinLogOpType
        binlog = BinLog.get_instance()
        binlog.set_max_size(1000)
        binlog.set_enabled(True)

        fsutil.touch("./tmp/a.txt")

        upload_event = xnote_event.FileUploadEvent()
        upload_event.fpath = "./tmp/a.txt"
        upload_event.user_id = 0
        on_fs_upload(upload_event)

        last_seq = binlog.last_seq
        result = LEADER.list_binlog(last_seq=last_seq, limit=20)
        assert result.success == True
        assert isinstance(result.data, list)
        assert len(result.data) == 1
        assert result.data[0].optype == BinLogOpType.file_upload
        assert result.data[0].value["fpath"] == upload_event.fpath
        assert result.data[0].value["ftype"] == "txt"

        check_manager = FileIndexCheckManager()
        check_manager.run_step()

    def test_system_info(self):
        info_key = "config.test"
        SystemInfoService.save_info(info_key, "1")
        value = SystemInfoService.get_info_value(info_key)
        assert value == "1"
        SystemInfoService.save_info(info_key, "2")
        value = SystemInfoService.get_info_value(info_key)
        assert value == "2"