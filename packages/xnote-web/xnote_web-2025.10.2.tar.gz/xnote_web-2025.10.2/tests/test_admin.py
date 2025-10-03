# -*- coding:utf-8 -*-
"""
@Author       : xupingmao
@email        : 578749341@qq.com
@Date         : 2023-10-14 09:30:29
@LastEditors  : xupingmao
@LastEditTime : 2024-03-31 14:37:13
@FilePath     : /xnote/tests/test_admin.py
@Description  : 描述
"""

import web.utils

from . import test_base
from xnote.core import xconfig, xmanager, xauth
from xnote.service import JobService

app = test_base.init()

class TestMain(test_base.BaseTestCase):
    """测试管理后台的功能"""
    
    def test_db_struct(self):
        self.check_OK("/system/db/struct?table_name=user")
        
        
    def assert_no_auth(self, response):
        if response.status == "401 Unauthorized":
            return
        
        if "/unauthorized" in response.headers['Location']:
            return
        raise Exception("发现权限拦截漏洞")

    def test_admin_auth(self):
        print("")
        
        skip_list = set([
            "/system/settings",
            "/system/stats",
            "/system/stats/location",
            "/system/index",
            "/system/sys",
            "/system/system",
            r"/system/user\.css",
            r"/system/user\.js",
            "/system/log/visit",
            "/system/todo",
        ])

        check_list = set([
            "/plugins_upload",
            "/plugins_new",
            "/plugins_new/command",
        ])

        try:
            # 登录普通用户
            xauth.TestEnv.login_user("test")

            mapping = xmanager.get_handler_manager().mapping
            
            for pattern, raw_handler in web.utils.group(mapping, 2):
                if pattern in skip_list:
                    continue
                if pattern.startswith("/system/") or pattern in check_list or pattern.startswith("/admin/"):
                    print(f"Check {pattern} ...")
                    handler = raw_handler.handler_class
                    check_pass = False
                    if hasattr(handler, "GET"):
                        response = self.request_app(pattern, method="GET")
                        self.assert_no_auth(response)
                        check_pass = True
                    
                    if hasattr(handler, "POST"):
                        response = self.request_app(pattern, method="POST")
                        self.assert_no_auth(response)
                        check_pass = True
                    assert check_pass
        finally:
            xauth.TestEnv.login_user("admin")
        
    def test_admin_functions(self):
        self.check_OK("/admin/functions")

    def test_admin_job(self):
        self.check_OK("/admin/test_job")
        self.check_OK("/admin/jobs")
        
        job_list, amount = JobService.list_job_page()
        assert len(job_list) > 0
        assert amount > 0
        
        job_id = job_list[0].id
        
        self.check_OK(f"/admin/jobs?action=view&job_id={job_id}")
        self.check_OK(f"/admin/jobs?action=edit&job_id={job_id}")
        self.check_OK(f"/admin/jobs?action=delete&job_id={job_id}")
        
    def test_example(self):
        self.check_OK("/test/example/table")
    
    def test_admin_test(self):
        self.check_OK("/admin/test?type=lock")


    def test_thread_info(self):
        self.check_OK("/system/thread_info")

    def test_admin_repair(self):
        self.check_OK("/admin/repair")
        self.check_OK("/admin/repair?action=repair&code=fix_msg_tag")

    def test_system_template_cache(self):
        self.check_OK("/system/template_cache")