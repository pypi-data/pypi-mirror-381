# -*- coding:utf-8 -*-
# @author xupingmao
# @since 2021/07/18 18:36:23
# @modified 2021/07/18 19:45:09
# @filename test_search.py

from . import test_base
from .test_base import json_request_return_dict
from xnote.core import xauth
from handlers.plugin.dao import add_visit_log, delete_visit_log

app          = test_base.init()
json_request = test_base.json_request
request_html = test_base.request_html
BaseTestCase = test_base.BaseTestCase

class TestMain(BaseTestCase):

    def test_plugin_list(self):
        self.check_OK("/plugin_list")

    def test_table(self):
        self.check_OK("/test/example/table?name=table")

    def test_contribution_calendar(self):
        self.check_OK("/test/example/calendar?name=calendar")

    def test_list(self):
        self.check_OK("/test/example/list?name=list")

    def test_plugin_visit(self):
        delete_visit_log(user_name="admin", url="/test")
        assert add_visit_log(user_name="admin", url="/test") == 1
        assert add_visit_log(user_name="admin", url="/test") == 2

    def test_plugin_manage(self):
        self.check_OK("/plugin_manage")
        