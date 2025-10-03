# -*- coding:utf-8 -*-
"""
@Author       : xupingmao
@email        : 578749341@qq.com
@Date         : 2021/11/29 22:48:26
@LastEditors  : xupingmao
@LastEditTime : 2024-08-03 10:39:34
@FilePath     : /xnote/handlers/system/system_sync/system_sync_proxy.py
@Description  : 网络代理
"""

import os
import time
import logging
import typing

import xutils
from xnote.core import xconfig

from xutils import Storage
from xutils import netutil
from xutils import textutil
from xutils import dateutil
from xutils import fsutil
from xutils import dbutil
from xutils import jsonutil
from xutils.mem_util import log_mem_info_deco
from xutils.netutil import HttpFileNotFoundError, HttpError
from .models import FileIndexInfo
from .models import LeaderStat
from .models import SystemSyncToken
from .system_sync_indexer import build_index_by_fpath

RETRY_INTERVAL = 60
MAX_KEY_SIZE = 511

def print_debug_info(*args):
    new_args = [dateutil.format_time(), "[system_sync_http]"]
    new_args += args
    print(*new_args)

class HttpClient:

    def __init__(self, host, token="", admin_token=""):
        self.follower_name = ""
        self.host = host
        self.token = token # leader_token
        self.admin_token = admin_token
        self.access_token = "" # 临时访问令牌
        self.token_info: typing.Optional[SystemSyncToken] = None
        self.debug = True
        self.node_id = xconfig.get_global_config("system.node_id", "unknown_node_id")
        self.port = xconfig.get_global_config("system.port")
        self.fs_sync_failed_msg = ""

    def check_failed(self):
        if self.host is None:
            logging.warning("host为空")
            return True

        return False
    
    def check_access_token(self):
        if self.token_info is None or self.token_info.is_expired():
            self.handle_token()
        
    def handle_token(self):
        self.refresh_token()

    def refresh_token(self):
        node_id = self.node_id
        port = self.port
        url = f"{self.host}/system/sync?p=refresh_token&leader_token={self.token}&node_id={node_id}&port={port}"
        result = netutil.http_get(url)
        assert isinstance(result, (str, bytes))
        result_obj = jsonutil.parse_json_to_dict(result)
        success = result_obj.get("success", False)
        message = result_obj.get("message")
        if not success:
            raise Exception(f"refresh_token failed, err={message}")
        data = result_obj.get("data")
        token_info = SystemSyncToken.from_dict(data)
        if token_info == None:
            message = "token is empty"
            raise Exception(f"refresh_token failed, err={message}")
        self.access_token = token_info.token
        self.token_info = token_info

    def get_stat(self, params: dict):
        self.check_disk_space()
        self.handle_token()

        if self.check_failed():
            return None

        params["token"] = self.access_token

        url = "{host}/system/sync/leader?p=get_stat".format(host = self.host)
        result = netutil.http_get(url, params = params, skip_empty_value = True)
        result_obj = textutil.parse_json(result, ignore_error = True)
        result = LeaderStat.from_dict(result_obj)
        if result != None:
            result.access_token = self.access_token
        return result

    def list_files(self, last_id=0):
        self.check_access_token()
        if self.check_failed():
            return

        last_id_str = str(last_id)
        url = "{host}/system/sync/leader?p=list_files&token={token}&last_id={last_id}".format(
            host = self.host, token = self.access_token, last_id = last_id_str)
        
        if self.debug:
            logging.info("sync_from_leader: %s", url)

        content = netutil.http_get(url)
        result = textutil.parse_json(content, ignore_error = True)
        
        if result is None:
            error = Storage()
            error.url = url
            error.content = content
            print_debug_info("接口返回为空", error)
            return

        result = Storage(**result)
        if result.code != "success":
            print_debug_info("接口请求失败", result)

        follower_dict = result.get("follower_dict", {})
        for url in follower_dict:
            info = follower_dict.get(url)
            self.admin_token = info.get("admin_token")

        return result

    def is_same_file(self, dest_path, item: FileIndexInfo):
        if not os.path.exists(dest_path):
            return False

        stat = os.stat(dest_path)
        local_sha1_sum = fsutil.get_sha1_sum(dest_path)
        is_same_file = (item.fsize == stat.st_size and local_sha1_sum == item.sha1_sum)
        logging.debug("is_same_file: %s, sha1_sum: %s", is_same_file, item.sha1_sum)
        return is_same_file

    def check_disk_space(self):
        data_dir = xconfig.get_system_dir("data")
        free_space = fsutil.get_free_space(data_dir)
        result = free_space >= 1024 ** 3 # 要大于1G

        if not result:
            logging.debug("磁盘容量不足, 当前容量:%s", fsutil.format_size(free_space))

        return result
    
    def is_ignore_file(self, webpath: str):
        skip_dir_list = ["/data/db", "/data/tmp", "/data/log", "/data/backup", "/data/cache", "/data/trash"]
        for skip_dir in skip_dir_list:
            if fsutil.is_parent_dir(skip_dir, webpath):
                return True
        return False
    
    def is_invalid_file(self, webpath=""):
        if xutils.is_windows():
            invalid_list = ":?"
            for item in invalid_list:
                if item in webpath:
                    return True
        return False
    
    def get_dest_path(self, webpath=""):
        data_dir  = xconfig.FileConfig.data_dir
        temp_path = fsutil.get_relative_path(webpath, "/data/")
        path = os.path.join(data_dir, temp_path)
        return os.path.abspath(path)

    def download_file(self, item: FileIndexInfo):
        self.check_access_token()

        if not self.check_disk_space():
            logging.error("磁盘容量不足，跳过")
            self.fs_sync_failed_msg = "磁盘容量不足"
            raise Exception("磁盘容量不足")
        
        if not item.exists:
            logging.info("文件不存在, fpath=%s", item.fpath)
            return
        
        if item.ftype == "dir":
            logging.info("跳过目录, dir=%s", item.fpath)
            return
        
        if item.fsize != 0:
            assert item.sha1_sum != "", item
        
        # 数据库文件不能下载
        if self.is_ignore_file(item.webpath):
            logging.info("跳过系统/临时文件, fpath=%s", item.fpath)
            return

        webpath = item.webpath

        if isinstance(item.mtime, float):
            mtime = item.mtime
        else:
            try:
                mtime = dateutil.parse_datetime(item.mtime)
            except:
                mtime = time.time()

        encoded_fpath = xutils.encode_base64(webpath)
        url = "{host}/fs_download".format(host = self.host)
        params = dict(token = self.access_token, fpath = encoded_fpath)
        url = netutil._join_url_and_params(url, params)

        dest_path = self.get_dest_path(webpath)
        dirname   = os.path.dirname(dest_path)

        if self.is_same_file(dest_path, item):
            logging.debug("文件没有变化，跳过:%s", webpath)
            build_index_by_fpath(dest_path, user_id=item.user_id, file_id=item.id)
            return

        fsutil.makedirs(dirname)

        logging.debug("原始文件:%s", url)
        logging.debug("目标文件:%s", dest_path)

        try:
            netutil.http_download(url, dest_path)
        except HttpFileNotFoundError:
            logging.error("file not found: %s", webpath)
            return
        except HttpError as err:
            if err.status == 403:
                logging.error("auth failed")
                self.refresh_token()
            
            self.fs_sync_failed_msg = str(err)
            raise err
        
        os.utime(dest_path, times=(mtime, mtime))
        local_sha1_sum = fsutil.get_sha1_sum(dest_path)
        if local_sha1_sum != item.sha1_sum:
            # 重试也不能成功了
            faild_msg = f"sha1校验码检查失败, local={local_sha1_sum}, remote={item.sha1_sum}, webpath={item.webpath}, download_url={url}"
            self.fs_sync_failed_msg = faild_msg
            raise Exception(faild_msg)

        build_index_by_fpath(dest_path, user_id=item.user_id, file_id=item.id)
        self.fs_sync_failed_msg = ""

    def download_files(self, result):
        for item in result.data:
            self.download_file(FileIndexInfo(**item))

    @log_mem_info_deco("proxy.http_get")
    def http_get(self, url, params=None):
        return netutil.http_get(url, params=params)

    @log_mem_info_deco("proxy.list_binlog")
    def list_binlog(self, last_seq=0) -> dict:
        # TODO 这里做类型解析和转换
        assert isinstance(last_seq, int)
        params = dict(last_seq=str(last_seq), include_req_seq="false")
        self.check_access_token()

        leader_host = self.host
        url = "{host}/system/sync/leader?p=list_binlog&token={token}".format(
            host=leader_host, token=self.access_token)
        
        result = self.http_get(url, params=params)
        try:
            result_obj = textutil.parse_json(result)
            assert isinstance(result_obj, dict)
            return result_obj
        except:
            logging.error("解析json失败, result=%s", result)
            raise Exception("解析JSON失败")
    
    def list_db(self, last_key):
        # type: (str) -> str
        # TODO 这里做类型解析和转换
        self.check_access_token()
        leader_host = self.host
        params = dict(last_key=last_key, token=self.access_token)
        url = "{host}/system/sync/leader?p=list_db".format(host=leader_host)
        result = netutil.http_get(url, params=params)
        assert isinstance(result, str)
        return result


empty_http_client = HttpClient("", "", "")
