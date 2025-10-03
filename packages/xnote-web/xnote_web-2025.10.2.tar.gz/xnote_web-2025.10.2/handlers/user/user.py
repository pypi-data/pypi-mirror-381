# encoding=utf-8
# @modified 2022/04/04 14:01:57
import web
import json
import typing
import xutils
import math

from xnote.core import xauth
from xnote.core import xtemplate
from xnote.core import xmanager
from xnote.core.xtemplate import T
from xnote.core.xtemplate import BasePlugin
from xnote.core import xconfig

from xutils import textutil
from xutils import Storage
from xutils import dbutil
from xutils import webutil
from xnote.core.xauth import UserDO
from . import dao

from xnote.plugin.table_plugin import BaseTablePlugin
from xnote.plugin import DataTable, TableActionType, InfoTable, InfoItem
from xnote.plugin import DataForm, LinkConfig
from xnote.plugin.form import FormRowType
from xnote.plugin.list import ItemList, ListItem, ConfirmButton
from xnote.plugin import sidebar

OP_LOG_TABLE = xauth.UserOpLogDao


def create_op_log(user_name, op_type, detail):
    ip = webutil.get_real_ip()
    log = dao.UserOpLog()
    log.user_id = xauth.UserDao.get_id_by_name(user_name)
    log.ip = ip
    log.type = op_type
    log.detail = detail
    dao.UserOpLogDao.create_op_log(log)


class UserListHandler(BaseTablePlugin):
    """用户管理"""
    title = "用户管理"
    option_html = """<button class="btn" onclick="xnote.table.handleEditForm(this)"
            data-url="?action=edit" data-title="创建新用户">创建新用户</button>"""
    NAV_HTML = ""
    PAGE_HTML = BaseTablePlugin.TABLE_HTML
    parent_link = LinkConfig.app_index

    def handle_page(self):
        page = xutils.get_argument_int("page", 1)
        page_size = xutils.get_argument_int("page_size", 10)
        offset = (page-1) * page_size
        assert offset >= 0

        table = self.create_table()
        table.default_head_style.min_width = "100px"

        table.add_head("编号", "id")
        table.add_head("登录名", "name", link_field="edit_url")
        table.add_head("状态", "status_text")
        table.add_head("上次登录", "login_time", min_width="200px")
        # 操作按钮
        table.add_action("编辑", link_field="edit_url", type=TableActionType.link, css_class="btn btn-default")
        table.add_action("删除", link_field="delete_url", type=TableActionType.confirm, 
                         msg_field="delete_msg", css_class="btn danger")
        table.set_action_style(min_width="120px")

        for user_info in xauth.UserModel.list(offset = offset, limit = page_size):
            user_info.edit_url = f"{xconfig.WebConfig.server_home}/system/user?name={user_info.name}"
            user_info.delete_msg = f"确定删除{user_info.name}吗?"
            user_info.delete_url = f"{xconfig.WebConfig.server_home}/system/user/remove?user_id={user_info.id}"
            user_info.status_text = user_info.get_status_text()
            
            table.add_row(user_info)

        total = xauth.UserModel.count()

        kw = Storage()
        kw.user_info = None
        kw.show_aside = False
        kw.table = table
        kw.page = page
        kw.page_size = page_size
        kw.page_max = math.ceil(total/page_size)//1
        kw.page_url = "?page="

        self.write_aside("{% include system/component/admin_nav.html %}")

        return self.response_page(**kw)
    
    def handle_edit(self):
        form = DataForm()
        form.add_row("登录名", "name")
        
        kw = Storage()
        kw.form = form
        return self.response_form(**kw)
    
    def handle_save(self):
        data_dict = self.get_data_dict()

        model_id = data_dict.get_int("id")
        if model_id != 0:
            model_info = xauth.UserDao.get_by_id(user_id=model_id)
            assert model_info != None
        else:
            model_info = xauth.UserDO()
        
        user_name = data_dict.get_str("name")
        if user_name == None:
            return webutil.FailedResult(message="登录名不能为空")
        
        model_info.name = user_name
        return xauth.create_user(user_name, textutil.random_string(6))

class UserHandler:

    def handle_user_log(self, kw: Storage, user_info: xauth.UserDO):
        assert user_info != None
        page = xutils.get_argument_int("page", 1)
        user_id = user_info.id
        page_size = 20
        offset = (page-1) * page_size
        log_list = OP_LOG_TABLE.list_by_user(user_id=user_id, offset=offset, limit=page_size)

        table = DataTable()
        table.default_head_style.min_width = "100px"
        table.add_head("操作类型", "type")
        table.add_head("操作时间", "ctime", min_width="200px")
        table.add_head("IP地址", "ip", min_width="100px")
        table.add_head("详情", "detail", min_width="200px")

        for item in log_list:
            table.add_row(item)

        kw.table = table
        kw.page = page
        kw.page_size = page_size
        kw.page_totalsize = OP_LOG_TABLE.count(user_id=user_id)
        kw.page_url = f"?name={user_info.name}&page="
    
    @xauth.login_required("admin")
    def GET(self):
        name = xutils.get_argument_str("name")
        user_info = None
        if name != "":
            user_info = xauth.get_user(name)
        
        kw = Storage()
        kw.name = name
        kw.user_info = user_info
        kw.info_table = self.get_info_table(user_info)

        if user_info != None:
            self.handle_user_log(kw, user_info=user_info)

        return xtemplate.render("user/page/user_manage.html", **kw)
    
    def get_info_table(self, user_info: typing.Optional[UserDO]):
        if user_info is None:
            return None
        
        info = InfoTable()
        info.add_item(InfoItem(name="用户名", value=user_info.name))
        info.add_item(InfoItem(name="salt", value=user_info.salt))
        info.add_item(InfoItem(name="token", value=user_info.token))
        info.add_item(InfoItem(name="最近更新", value=user_info.mtime))
        info.add_item(InfoItem(name="上次登录", value=user_info.login_time))
        if not user_info.is_admin:
            user_id = user_info.user_id
            user_name = user_info.name
            info.bottom_action_bar.add_confirm_button(
                "删除用户", url=f"/system/user/remove?user_id={user_id}", 
                message=f"确定删除用户[{user_name}]吗?", css_class="danger", reload_url="/user/list")
            info.bottom_action_bar.add_confirm_button(
                "重置密码", url=f"/system/user/reset_password?user_id={user_id}&user_name={user_name}",
                message=f"确定重置用户[{user_name}]的密码吗?", method="POST", css_class="danger")
        return info

    @xauth.login_required("admin")
    def POST(self):
        name = xutils.get_argument_str("name")
        password = xutils.get_argument_str("password")
        user_info = xauth.get_user(name)
        if user_info is None:
            raise Exception("用户不存在:%s" % name)

        user_info.password = password
        xauth.update_user(name, user_info)

        raise web.seeother("/system/user?name=%s" % name)


class AddHandler:

    @xauth.login_required("admin")
    def POST(self):
        name = xutils.get_argument_str("name")
        return xauth.create_user(name, textutil.random_string(6))


class RemoveHandler:

    @xauth.login_required("admin")
    def POST(self):
        user_id = xutils.get_argument_int("user_id")
        xauth.UserModel.delete_by_id(user_id)
        return webutil.SuccessResult()
    
    def GET(self):
        return self.POST()


class UserInfoHandler(BasePlugin):
    require_login = True
    require_admin = False
    show_aside = True
    title = "账号设置"
    rows = 0

    HTML = """
{% include settings/page/settings_tab.html %}

<div class="card">
{% render item_list %}
</div>
"""

    def get_aside_html(self):
        return sidebar.get_settings_sidebar_html()
    
    def handle(self, input=""):
        user = xauth.current_user()
        assert user != None

        item_list = ItemList()
        item_list.add_item(ListItem(text="用户名", css_class="list-item-black", href="#", badge_info=user.name))
        item_list.add_item(ListItem(text="修改密码", css_class="list-item-black", href="/user/change_password", show_chevron_right=True))
        item_list.add_item(ListItem(text="用户日志", css_class="list-item-black", href="/user/op_log", show_chevron_right=True))

        logout = ListItem(text="登出账号", css_class="list-item-black", show_chevron_right=False)
        logout.action_btn = ConfirmButton("登出", url="/logout?_format=json", message="确认登出吗?", css_class="danger")
        item_list.add_item(logout)

        self.writehtml(self.HTML, item_list = item_list)

class UserInfoAjaxHandler:
    def getDesensitizedUserInfo(self):
        user = xauth.current_user()
        assert user != None
        mobile = ''
        if (user.mobile != None and user.mobile != ''):
            mobile = user.mobile[:3] + '****' + user.mobile[7:]
        return dict(name=user.name, phone=mobile)


    @xauth.login_required()
    def POST(self):
       return self.getDesensitizedUserInfo()

    @xauth.login_required()
    def GET(self):
        return self.getDesensitizedUserInfo()


class SessionInfoAjaxHandler:

    @xauth.login_required()
    def GET(self):
        user_name = xauth.current_name()
        return xauth.list_user_session_detail(user_name)


class ChangePasswordHandler:

    def GET(self, error=""):
        """获取页面, 修改密码后也需要跳转到这里，所以不能校验登录态"""
        old_password = xutils.get_argument_str("old_password", "")
        new_password = xutils.get_argument_str("new_password", "")
        return xtemplate.render("user/page/change_password.html",
                                old_password=old_password, new_password=new_password, error=error)

    @xauth.login_required()
    def POST(self):
        user_name = xauth.current_name_str()
        old_password = xutils.get_argument_str("old_password", "")
        new_password = xutils.get_argument_str("new_password", "")
        confirmed_password = xutils.get_argument_str("confirmed_password")

        if old_password == "":
            return webutil.FailedResult(message="旧的密码为空")
        if new_password == "":
            return webutil.FailedResult(message="新的密码为空")
        if new_password != confirmed_password:
            return webutil.FailedResult(message="两次输入的密码不一致")

        try:
            xauth.check_old_password(user_name, old_password)
            xauth.update_user(user_name, Storage(password=new_password))
            create_op_log(user_name, "change_password", "修改密码")
            return webutil.SuccessResult()
        except Exception as e:
            return webutil.FailedResult(message=str(e))

class ResetPasswordHandler:

    @xauth.login_required("admin")
    def POST(self):
        user_name = xutils.get_argument_str("user_name")
        new_password = xutils.random_number_str(8)
        xauth.update_user(user_name, Storage(password=new_password))
        create_op_log(user_name, dao.UserOpTypeEnum.reset_password.value, "重置密码")
        return webutil.SuccessResult(data=new_password)

class UserOpLogHandler(BaseTablePlugin):

    require_admin = False
    title = "用户日志"
    NAV_HTML = ""
    PAGE_HTML = BaseTablePlugin.TABLE_HTML

    @xauth.login_required()
    def handle_page(self):
        kw = Storage()
        user_info = xauth.current_user()
        assert user_info != None
        UserHandler().handle_user_log(kw, user_info=user_info)

        self.write_aside("""{% include settings/page/settings_sidebar.html %}""")

        return self.response_page(**kw)

xurls = (
    r"/user/add",  AddHandler,
    r"/user/list",  UserListHandler,
    r"/user/info",   UserInfoHandler,
    r"/user/info_ajax", UserInfoAjaxHandler,
    r"/user/session", SessionInfoAjaxHandler,
    r"/user/change_password", ChangePasswordHandler,
    r"/user/op_log", UserOpLogHandler,

    r"/system/user", UserHandler,
    r"/system/user/list", UserListHandler,
    r"/system/user/remove", RemoveHandler,
    r"/system/user/reset_password", ResetPasswordHandler,
)
