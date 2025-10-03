# encoding=utf-8
# Created by xupingmao on 2017/05/23
# @modified 2022/04/17 14:28:57

import os
from .a import *

from xnote.core import xtemplate
from xnote.core import xconfig
from xnote.core import xauth

from xutils.functions import TypedDict
from xutils import Storage
from xutils import dbutil
from xutils import dateutil, dbutil
from xutils import logutil
from xnote.core.models import SearchContext
from urllib.parse import quote

# cannot perform relative import
try:
    import test_base
except ImportError:
    from tests import test_base

app = test_base.init()
json_request = test_base.json_request
json_request_return_dict = test_base.json_request_return_dict
request_html = test_base.request_html
BaseTestCase = test_base.BaseTestCase

# 必须init之后再import

from handlers.message import dao as msg_dao
from handlers.message import message_model
from handlers.message import message_tag

MSG_DB = dbutil.get_table("msg_v3")


def get_script_path(name):
    return os.path.join(xconfig.SCRIPTS_DIR, name)


def del_msg_by_id(int_id: int):
    json_request("/message/delete", method="POST", data=dict(id=int_id))

def del_msg_tag(tag_id=0):
    json_request("/message/tag/delete", method="POST", data=dict(tag_id=tag_id))

def delete_all_messages():
    for record in MSG_DB.iter(limit=-1):
        MSG_DB.delete_by_key(record.get("_key"))


class TextPage(xtemplate.BaseTextPlugin):

    def get_input(self):
        return ""

    def get_format(self):
        return ""

    def handle(self, input):
        return "test"


class TestMain(BaseTestCase):

    def test_message_create_and_update(self):
        # Py2: webpy会自动把str对象转成unicode对象，data参数传unicode反而会有问题
        from handlers.message.dao import MessageDao
        response = json_request_return_dict(
            "/message/save", method="POST", data=dict(content="Xnote-Unit-Test"))
        self.assertEqual("success", response.get("code"))
        data = response.get("data")
        assert isinstance(data, dict)
        # Py2: 判断的时候必须使用unicode
        self.assertEqual(u"Xnote-Unit-Test", data.get("content"))
        json_request("/message/touch", method="POST",
                     data=dict(id=data.get("id")))

        msg_id = data.get("id")

        update_result = json_request_return_dict(
            "/message/save", method="POST", data=dict(id=msg_id, content="New Content"))
        self.assertEqual("success", update_result["code"])

        data = MessageDao.get_by_key(msg_id)
        assert data != None
        assert data.tag == "log"
        assert data.status == None

        self.assertEqual("New Content", data.content)

        keyword = quote("#test#")
        quoted_id = quote(data.id)
        self.check_OK(f"/message/create_dialog?keyword={keyword}&tag=log")
        self.check_OK(f"/message/edit_dialog?id={quoted_id}")

        json_request("/message/delete", method="POST",
                     data=dict(id=data.int_id))
        
        self.check_404(f"/message/edit_dialog?id={quoted_id}")
        
    def test_create_with_date(self):
        data = dict(content="Xnote-Date-Test", date="2020-01-01")
        result = json_request_return_dict("/message/save", method="POST", data=data)
        assert result.get_bool("success") == True
        msg_id = result.get_dict("data").get_int("id")
        data = msg_dao.MessageDao.get_by_key(msg_id)
        assert data != None
        assert data.change_time == "2020-01-01 23:59:00"

    def test_message_list(self):
        json_request("/message/list")
        json_request("/message/list?status=created")
        json_request("/message/list?status=suspended")
        json_request("/message/list?tag=file")
        json_request("/message/list?tag=link")
        json_request("/message/list?tag=todo")
        # search
        json_request("/message/list?key=1")

        self.check_OK("/message/list?format=html")

    def test_message_finish(self):
        response = json_request_return_dict(
            "/message/save", method="POST", data=dict(content="Xnote-Unit-Test", tag="task"))

        self.assertEqual("success", response.get("code"))
        data = response.get("data")
        assert isinstance(data, dict)

        msg_id = data['id']

        json_request("/message/finish", method="POST", data=dict(id=msg_id))
        done_result = json_request_return_dict("/message/list?tag=done")

        self.assertEqual("success", done_result['code'])

        done_list = done_result['data']
        self.assertEqual(1, len(done_list))

        for msg in done_list:
            del_msg_by_id(int(msg["_id"]))

    def count_message_key(self):
        response = json_request("/api/message/tag/list")
        assert isinstance(response, dict)
        assert response.get("code") == "success"
        data = response.get("data")
        assert isinstance(data, list)
        return len(data)

    def test_message_key(self):
        key_result = json_request("/api/message/tag/list")
        assert isinstance(key_result, dict)

        for item in key_result["data"]:
            del_msg_tag(item["tag_id"])

        assert self.count_message_key() == 0

        response = json_request_return_dict(
            "/message/save", method="POST", data=dict(content="#Xnote-Unit-Test#", tag="log"))

        self.assertEqual("success", response.get("code"))
        data = response.get("data")
        assert isinstance(data, dict)
        int_id = int(data["_id"])

        assert self.count_message_key() == 1

        del_msg_by_id(int_id)


    def test_message_stat(self):
        result = json_request_return_dict("/message/stat")
        self.assertTrue(result.get("cron_count") != None)

    def test_list_by_month(self):
        self.check_OK("/message/date?date=2021-05")

    def test_list_by_day(self):
        # 创建一条记录
        response = json_request("/message/save", method="POST",
                                data=dict(content="Xnote-Unit-Test", tag="log"))

        month = dateutil.format_date(fmt="%Y-%m")
        date = dateutil.format_date()
        self.check_OK("/message/list_by_day?date=" + month)
        self.check_OK("/message?date=" + date)

    def test_message_refresh(self):
        self.check_OK("/message/refresh")

    def test_message_task_tags(self):
        # 创建一条记录
        response = json_request("/message/save", method="POST",
                                data=dict(content="#TEST# Xnote-Unit-Test", tag="task"))

        self.check_OK("/message?tag=task_tags")

    def test_message_task(self):
        self.check_OK("/message?tag=task")
        self.check_OK("/message?tag=task&action=create")
        self.check_OK("/message?tag=task&filterKey=test")
        self.check_OK("/message/task")
        self.check_OK("/message/task?p=done")
        self.check_OK("/message/task/list_ajax")
        self.check_OK("/message/task/list_ajax?p=done")
        self.check_OK("/message/task/tag_list")

    def test_task_create_and_done(self):
        # Py2: webpy会自动把str对象转成unicode对象，data参数传unicode反而会有问题
        response = json_request_return_dict("/message/save", method="POST",
                                            data=dict(content="Xnote-Unit-Test-Task", tag="task"))
        self.assertEqual("success", response.get("code"))
        data = response.get("data")
        assert isinstance(data, dict)

        # Py2: 判断的时候必须使用unicode
        self.assertEqual(u"Xnote-Unit-Test-Task", data.get("content"))

        task_id = data["id"]

        update_result = json_request_return_dict("/message/finish", method="POST",
                                                 data=dict(id=task_id))
        self.assertEqual("success", update_result.get("code"))

        logutil.wait_task_done()

        # 重新把任务开启
        open_result = json_request_return_dict("/message/update_first_tag", method="POST",
                                               data=dict(id=task_id, tag="task"))
        assert open_result["success"] == True

        data = msg_dao.get_message_by_id(task_id)
        assert data != None
        assert data.tag == "task"

    def test_message_dairy(self):
        self.check_OK("/message/dairy")

    def do_test_search(self, content="", tag="", tag_name=""):
        delete_all_messages()

        user_name = xauth.current_name_str()

        create_data = dict(content=content, tag=tag)
        response = json_request(
            "/message/save", method="POST", data=create_data)

        assert isinstance(response, dict)
        resp_data = response.get("data")
        assert isinstance(resp_data, dict)
        new_msg_id = resp_data.get("id")
        self.assertEqual("success", response.get("code"))

        from handlers.message.message_search import on_search_message, SearchHandler
        ctx = SearchContext(key="xnote")
        ctx.search_message = True
        ctx.user_name = user_name
        ctx.user_id = xauth.current_user_id()
        
        on_search_message(ctx)
        # 两条记录（第一个是汇总，第二个是实际数据）
        self.assertEqual(2, len(ctx.messages))
        self.assertEqual(content, ctx.messages[1].html)
        self.assertEqual(tag_name, ctx.messages[1].tag_name)

        search_list, amount = SearchHandler().get_ajax_data(
            user_name=user_name, key="xnote")
        assert amount == 1
        assert len(search_list) == 1
        assert search_list[0].id == new_msg_id
        assert search_list[0].sort_value != ""

    def test_search_log(self):
        self.do_test_search("xnote-log-test", tag="log", tag_name="随手记")

    def test_search_task(self):
        self.do_test_search("xnote-task-test", tag="task", tag_name="待办")

    def test_message_search_page(self):
        self.check_OK("/message?tag=search&key=123")

    def test_message_tag_search(self):
        self.check_OK("/message/tag/search_dialog")

    def test_message_keyword_mark(self):
        user_name = xauth.current_name_str()
        from handlers.message.dao import MsgTagInfoDao
        tags = MsgTagInfoDao.list(user=user_name, tag_code="#test#")
        for tag in tags:
            print("删除tag:", tag)
            MsgTagInfoDao.delete(tag)

        response = json_request(
            "/message/save", method="POST", data=dict(content="Xnote-Unit-Test #test#"))

        assert isinstance(response, dict)

        self.assertEqual("success", response.get("code"))

        result = json_request("/message/keyword", method="POST",
                              data=dict(action="mark", keyword="#test#"))
        assert isinstance(result, dict)

        self.assertEqual("success", result["code"])

        from handlers.message.message import get_or_create_keyword

        user_id = xauth.current_user_id()
        keyword = get_or_create_keyword(user_id, "#test#", "127.0.0.1")
        print(keyword)

        assert keyword != None
        self.assertTrue(keyword.is_marked == True)

        logutil.wait_task_done()

    def test_message_keyword_delete(self):
        from handlers.message.dao import MessageDO
        user_name = xauth.current_name_str()
        user_id = xauth.current_user_id()
        tagname = "#delete-test#"

        tagInfo = msg_dao.MsgTagInfoDao.get_or_create(user_id, tagname)
        keyword = msg_dao.get_by_content(user_name, "key", tagname)
        assert keyword != None
        assert keyword.content == tagname

        resp = json_request_return_dict(
            "/message/tag/delete", method="POST", data=dict(tag_id=tagInfo.tag_id))
        print("resp=", resp)

        self.assertEqual("success", resp["code"])

        keyword = msg_dao.get_by_content(user_name, "key", tagname)
        print(keyword)
        self.assertIsNone(keyword)

        logutil.wait_task_done()

    def test_message_calendar(self):
        self.check_OK("/message/calendar")

    def test_message_comment(self):
        response = json_request_return_dict(
            "/message/save", method="POST", data=dict(content="Xnote-Unit-Test comment"))
        self.assertEqual("success", response.get("code"))
        resp_data = response.get("data")
        assert isinstance(resp_data, dict)
        msg_id = resp_data.get("id")

        create_comment_data = dict(id=msg_id, content="this is a comment")
        result = json_request_return_dict("/message/comment/create", method="POST", data=create_comment_data)
        assert result["success"] == True

    def test_message_add_tag(self):
        result = message_tag.add_tag_to_content("empty", "#test#")
        assert result == "#test#\nempty"
        result = message_tag.add_tag_to_content("#tag1#\ntext", "#tag2#")
        assert result == "#tag1# #tag2#\ntext"
        result = message_tag.add_tag_to_content("#tag1#\ntext", "#tag1#")
        assert result == "#tag1#\ntext"

    def test_parse_message(self):
        content = "#tag# test"
        data = dict(content=content)
        result = json_request_return_dict("/message/parse", method="POST", data=data)
        assert result.get("success")
        tokens = result.get