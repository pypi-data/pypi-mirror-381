# -*- coding:utf-8 -*-
# @author xupingmao
# @since 2016/12
# @modified 2022/04/22 23:44:25
import math
import web
import os
import xutils
import handlers.note.dao as note_dao
import handlers.note.dao_share as dao_share

from xnote.core import xauth, xconfig, xtables, xtemplate, xmanager
from web import HTTPError
from xnote.core.xconfig import Storage
from xnote.core import xnote_event
from xutils import fsutil
from xutils import textutil
from xutils import webutil
from xutils import dbutil, dateutil
from xutils import encode_uri_component
from xnote.core.xtemplate import T
from xnote.core.xnote_user_config import UserConfig
from .constant import CREATE_BTN_TEXT_DICT
from . import dao_tag
from .dao_api import NoteDao
from handlers.note.models import NotePathInfo, NoteRelationGroup
from xnote.plugin import TextLink
from . import dao_draft
from . import dao_log
from .models import OrderTypeEnum, NoteIndexDO, NoteTypeEnum
from .dao_tag import NoteTagInfoDao
from .dao import NoteIndexDao, NoteDO
from handlers.note.note_service import NoteService, NoteRelationService
from xnote.plugin.table import DataTable
from xnote.plugin import TabBox


PAGE_SIZE = xconfig.PAGE_SIZE
NOTE_DAO = xutils.DAO("note")

def is_empty_id(note_id):
    return note_id == 0 or note_id == ""

class NoteViewContext(Storage):

    note_detail_tab: TabBox

    def __init__(self, **kw):
        self.user_name = ""
        self.user_id = 0
        self.recommended_notes = [] # type: list|object
        self.next_note = None # type: NoteIndexDO|None
        self.prev_note = None # type: NoteIndexDO|None
        
        self.can_edit = False
        self.show_left = False
        self.show_groups = False
        self.show_aside = True
        self.show_contents_btn = False
        self.show_comment_edit = False
        self.show_comment = True
        self.show_content = True
        self.show_ext_info = True
        self.show_nav = True
        self.show_relation = False
        self.show_relation_row = True
        self.show_tag = True
        self.show_search_div = True
        self.show_parent_link = True

        self.page = 1
        self.pagesize = 20
        self.page_url = ""

        self.groups = []
        self.files = []
        self.show_mdate = False
        self.show_add_file = False
        self.template_name = "note/page/detail/note_detail.html"
        self.search_type = "note"
        self.comment_source_class = "hide"
        self.op = ""
        self.is_public_page = False
        self.OrderTypeEnum = OrderTypeEnum
        self.file = None # type: NoteIndexDO|None
        self.content = ""
        self.note_alias_list = [] # type: list[NoteIndexDO]
        self.show_recommend = False
        self.show_pagination = False
        self.edit_token = ""
        self.tab = ""
        self.create_btn_text = ""
        self.relation_group_list = None # type: None|list[NoteRelationGroup]
        self.related_notes = [] # type: list[TextLink]
        self.relation_table = None # type: DataTable|None
        self.rev_relation_table = None # type: DataTable|None
    
        self.update(kw)

    def hide_components(self):
        self.show_comment = False
        self.show_comment_edit = False
        self.show_content = False
        self.show_relation = False
        self.show_relation_row = False
        self.show_ext_info = False
        self.show_tag = False


@xmanager.listen("note.view", is_async=False)
def visit_by_id(ctx: xnote_event.NoteViewEvent):
    note_id = ctx.id
    user_name = ctx.user_name
    note_dao.visit_note(user_name, note_id, user_id=ctx.user_id)


def handle_note_recommend(kw: NoteViewContext, file, user_name):
    ctx = Storage(id=file.id, name=file.name, creator=file.creator,
                  content=file.content,
                  parent_id=file.parent_id,
                  result=[])
    xmanager.fire("note.recommend", ctx)
    kw.recommended_notes = ctx.result
    kw.next_note = note_dao.find_next_note(file, user_name)
    kw.prev_note = note_dao.find_prev_note(file, user_name)


def view_gallery_func(file: NoteDO, kw: NoteViewContext):
    fpath = os.path.join(xconfig.UPLOAD_DIR, file.creator,
                         str(file.parent_id), str(file.id))
    filelist = []
    # 处理相册
    # print(file)
    fpath = note_dao.get_gallery_path(file)
    # print(fpath)
    if fpath != None:
        filelist = fsutil.list_files(fpath, webpath=True)
    file.path = fpath
    kw.show_aside = False
    kw.path = fpath
    kw.filelist = filelist


def view_html_func(file: NoteDO, kw: NoteViewContext):
    """处理html/post等类型的文档"""
    content = file.content
    content = content.replace(u'\xad', '\n')
    content = content.replace(u'\n', '<br/>')
    file.data = file.data.replace(u"\xad", "\n")
    file.data = file.data.replace(u'\n', '<br/>')
    if file.data == None or file.data == "":
        file.data = content
    kw.show_recommend = True
    kw.show_pagination = False


def view_or_edit_md_func(file: NoteDO, kw: NoteViewContext):
    device = xutils.get_argument_str("device", "desktop")
    load_draft = xutils.get_argument_bool("load_draft")
    creator_id = file.creator_id
    note_id = file.note_id

    note_tab = TabBox(tab_key="tab", tab_default="all", css_class="btn-style")
    note_tab.add_item(title="全部", value="all")
    if not kw.is_public_page:
        note_tab.add_item(title="关系", value="relation")
    note_tab.add_item(title="评论", value="comment")

    kw.note_detail_tab = note_tab
    kw.content = file.content
    kw.show_recommend = True
    kw.show_pagination = False
    kw.edit_token = textutil.create_uuid()
    kw.note_alias_list = NoteIndexDao.list(creator_id=creator_id, parent_id=note_id)
    kw.relation_group_list = []
    kw.related_notes = NoteRelationService.get_related_notes(note_id=note_id, user_id=creator_id)

    if kw.op == "edit":
        if load_draft:
            # 读取草稿
            draft_content = dao_draft.get_draft(file.id)

            if draft_content != "" and draft_content != None:
                kw.content = draft_content
                file.content = draft_content

        kw.show_recommend = False
        kw.template_name = "note/component/editor/markdown_edit.html"

    if kw.op == "edit" and device == "mobile":
        # 强制使用移动端编辑器
        kw.template_name = "note/component/editor/markdown_edit.mobile.html"

    
    if kw.op == "edit" and webutil.is_mobile_client():
        kw.show_nav = False

    if kw.tab == "comment":
        kw.hide_components()
        kw.show_comment = True
        kw.show_comment_edit = True

    if kw.tab == "relation":
        kw.hide_components()
        kw.show_relation = True
        kw.create_btn_text = "创建关系"
        kw.relation_table = NoteRelationService.get_table(note_id=file.note_id, user_id=kw.user_id)
        kw.rev_relation_table = NoteRelationService.get_rev_table(target_id=file.note_id, user_id=kw.user_id)


def view_group_timeline_func(note, kw):
    raise web.found("/note/timeline?type=default&parent_id=%s" % note.id)


def view_group_detail_func(file: note_dao.NoteDO, kw: NoteViewContext):
    page = kw.page
    # pagesize  = kw.pagesize
    pagesize = 1000
    is_public_page = kw.is_public_page
    user_id = file.creator_id

    dialog = xutils.get_argument_bool("dialog")
    q_tag = xutils.get_argument_str("tag", "")

    if kw.op == "edit":
        # 编辑笔记本的简介
        kw.show_recommend = False
        kw.template_name = "note/component/editor/markdown_edit.html"
        return
    
    q_tags = None
    if q_tag != "":
        q_tags = [q_tag]

    if file.order_type == int(OrderTypeEnum.ctime_desc.value):
        files = []
        kw.show_timeline_body = True
    else:
        offset = max(page-1, 0) * pagesize
        files = note_dao.list_by_parent(
            file.creator, parent_id=file.id,
            offset=offset, limit=pagesize,
            order_type=file.order_type, tags=q_tags)

    if is_public_page:
        files = list(filter(lambda x: x.is_public, files))

    for child in files:
        if child.type == "group":
            child.badge_info = str(child.children_count)

    amount = file.size or 0
    kw.content = file.content
    kw.show_search_div = True
    kw.show_add_file = True
    kw.show_aside = False
    kw.show_pagination = True
    kw.files = files
    kw.show_parent_link = False
    kw.page_max = math.ceil(amount/pagesize)
    kw.parent_id = file.id
    kw.q_tag = q_tag
    kw.tag_meta_list = NoteTagInfoDao.list(user_id=user_id, group_id=file.id)
    kw.show_orderby = True
    kw.order_type = file.order_type

    if dialog:
        # 对话框的样式
        kw.template_name = "note/ajax/group_detail_dialog.html"
    else:
        kw.template_name = "note/page/detail/group_detail.html"


def view_checklist_func(note, kw):
    kw.show_aside = False
    kw.show_pagination = False
    kw.show_comment_title = True
    kw.comment_title = T("清单项")
    kw.op = "view"
    kw.template_name = "note/page/detail/checklist_detail.html"
    kw.search_type = "checklist"
    kw.search_ext_dict = dict(note_id=note.id)


def view_table_func(note, kw):
    kw.show_aside = False
    kw.template_name = "note/page/detail/table_detail.html"


def view_form_func(note, kw):
    # 表单支持脚本处理，可以实现一些标准化的表单工具
    kw.template_name = "note/page/detail/form_detail.html"
    kw.file_id = note.id


VIEW_FUNC_DICT = {
    "group": view_group_detail_func,
    "md": view_or_edit_md_func,
    "text": view_or_edit_md_func,
    "memo": view_or_edit_md_func,
    "log": view_or_edit_md_func,
    "list": view_checklist_func,
    "csv": view_table_func,
    "gallery": view_gallery_func,
    "html": view_html_func,
    "post": view_html_func,
    "form": view_form_func,
}


def view_func_before(kw: NoteViewContext):
    if kw.file is None:
        return
    note = kw.file
    file = kw.file
    # 是否允许评论跟着笔记走
    kw.show_comment_edit = UserConfig.show_comment_edit.get_bool(user_name=file.creator)
    dao_tag.handle_tag_for_note(note)


def find_note_for_view0(token, note_id=0, name=""):
    if token != "":
        return note_dao.NoteTokenDao.get_by_token(token)
    if note_id != 0:
        return note_dao.get_by_id(note_id)
    if name != "":
        return note_dao.get_by_name(xauth.current_name_str(), name)

    raise HTTPError(504)


def find_note_for_view(token, note_id, name):
    note = find_note_for_view0(token, note_id, name)
    if note != None:
        note.mdate = dateutil.format_date(note.mtime)
        note.cdate = dateutil.format_date(note.ctime)
        note.adate = dateutil.format_date(note.atime)
    return note

class ViewHandler:

    def handle_contents_btn(self, kw:NoteViewContext):
        file = kw.file
        if file is None:
            raise Exception("file is None")
        can_edit = kw.can_edit
        is_valid_type = (file.type != "group") and (file.parent_id != "0")
        kw.show_contents_btn = is_valid_type and can_edit

    def handle_pathlist(self, file: NoteIndexDO, is_public_page=False):
        if is_public_page:
            root = NotePathInfo()
            root.url = f"{xconfig.WebConfig.server_home}/note/public"
            root.name = "根目录"
            file_path = NotePathInfo.public_from_note_index(file)
            return [root, file_path]
        else:
            return note_dao.list_path(file)

    @xutils.timeit(name="Note.View", logfile=True)
    def GET(self, op:str, id=0, is_public_page=False):
        try:
            return self.do_get(op, id, is_public_page)
        except Exception as e:
            xutils.print_exc()
            return xtemplate.render("error.html", error=str(e))

    def do_get(self, op:str, id=0, is_public_page=False):
        if id == 0:
            id = xutils.get_argument_int("id")
        else:
            id = int(id)
        
        name = xutils.get_argument("name", "")
        page = xutils.get_argument_int("page", 1)
        pagesize = xutils.get_argument_int("pagesize", xconfig.PAGE_SIZE)
        is_iframe = xutils.get_argument_str("is_iframe", "false")
        token = xutils.get_argument_str("token")
        
        user_info = xauth.current_user()
        if user_info != None:
            user_name = user_info.name
            user_id = user_info.id
        else:
            user_name = ""
            user_id = 0

        skey = xutils.get_argument_str("skey")

        kw = NoteViewContext()
        kw.op = op
        kw.user_name = user_name
        kw.user_id = user_id
        kw.page = page
        kw.pagesize = pagesize
        kw.page_url = f"/note/view?id={id}&page="
        kw.is_public_page = is_public_page
        kw.tab = xutils.get_argument_str("tab")

        if token == "" and is_empty_id(id):
            raise web.found("/")

        if skey != None and skey != "":
            return xtemplate.render("error.html", error="skey属性已经废弃")
        else:
            # 回收站的笔记也能看到
            file = find_note_for_view(token, id, name)
        
        kw.file = file
        if file is None:
            if id != 0:
                event = Storage(id=id, user_name=user_name)
                xmanager.fire("note.notfound", event)
            raise web.notfound()

        if token == "":
            NoteService.check_auth(file, user_id)

        if file.is_alias:
            raise web.seeother(f"/note/view/{file.parent_id}")

        pathlist = self.handle_pathlist(file, is_public_page)

        can_edit = (file.creator == user_name) or (user_name == "admin")

        # 定义一些变量
        recent_created = []

        event_ctx = xnote_event.NoteViewEvent(id=file.id, user_name=user_name, user_id=user_id)
        xmanager.fire("note.view", event_ctx)

        # 通用的预处理
        view_func_before(kw)

        view_func = VIEW_FUNC_DICT.get(file.type, view_or_edit_md_func)
        view_func(file, kw)

        if op == "edit":
            kw.show_aside = False
            kw.show_search = False
            kw.show_comment = False
            kw._show_footer = False

        if is_iframe == "true":
            kw.show_menu = False
            kw.show_search = False

        template_name = kw['template_name']
        del kw['template_name']

        kw.file = file
        kw.can_edit = can_edit
        kw.get_tag_name_by_code = dao_tag.get_name_by_code

        # 处理目录按钮的展示
        self.handle_contents_btn(kw)

        kw.html_title = file.name
        kw.note_id = id
        kw.pathlist = pathlist
        kw.recent_created = recent_created
        kw.CREATE_BTN_TEXT_DICT = CREATE_BTN_TEXT_DICT
        kw.is_iframe = is_iframe

        if is_public_page:
            note_dao.visit_public(id)

        if can_edit:
            kw.show_draft_edit = self.check_has_draft(id)

        return xtemplate.render_by_ua(template_name, **kw)

    def check_has_draft(self, note_id=0):
        return dao_draft.DraftDao.exists(note_id)

class ViewByIdHandler(ViewHandler):

    def GET(self, id):
        return ViewHandler.GET(self, "view", id)

    def POST(self, id):
        return ViewHandler.GET(self, "view", id)


class PrintHandler:

    @xauth.login_required()
    def GET(self):
        note_id = xutils.get_argument_int("id")
        note = note_dao.get_by_id(note_id)
        if note == None:
            return xtemplate.render("error.html", error="笔记不存在")
        user_id = xauth.current_user_id()
        NoteService.check_auth(note, user_id)

        kw = Storage()
        kw.show_menu = False
        kw.note = note
        kw.html_title = note.name
        return xtemplate.render("note/page/print.html", **kw)


def result(success=True, msg=None):
    return {"success": success, "result": None, "msg": msg}


def get_link(filename, webpath):
    if xutils.is_img_file(filename):
        return "![%s](%s)" % (filename, webpath)
    return "[%s](%s)" % (filename, webpath)


class MarkHandler:

    @xauth.login_required()
    def GET(self):
        id = xutils.get_argument("id")
        db = xtables.get_file_table()
        db.update(is_marked=1, where=dict(id=id))
        raise web.seeother("/note/view?id=%s" % id)


class UnmarkHandler:

    @xauth.login_required()
    def GET(self):
        id = xutils.get_argument("id")
        db = xtables.get_file_table()
        db.update(is_marked=0, where=dict(id=id))
        raise web.seeother("/note/view?id=%s" % id)


class NoteHistoryHandler:

    @xauth.login_required()
    def GET(self):
        note_id = xutils.get_argument("id")
        creator = xauth.current_name()
        note = note_dao.get_by_id_creator(note_id, creator)
        if note is None:
            history_list = []
        else:
            history_list = note_dao.list_history(note_id)
        return xtemplate.render("note/page/history_list.html",
                                current_note=note,
                                history_list=history_list,
                                show_aside=True)


class HistoryViewHandler:

    @xauth.login_required()
    def GET(self):
        note_id = xutils.get_argument("id")
        version = xutils.get_argument("version")

        creator = xauth.current_name()
        note = note_dao.get_by_id_creator(note_id, creator)
        content = ""
        if note != None:
            history = xutils.call("note.get_history", note_id, version)
            if history != None:
                content = history.content
        return dict(code="success", data=content)


class QueryHandler:

    @xauth.login_required("admin")
    def GET(self, action=""):
        if action == "get_by_id":
            id = xutils.get_argument("id")
            return dict(code="success", data=note_dao.get_by_id(id))
        if action == "get_by_name":
            name = xutils.get_argument_str("name")
            return dict(code="success", data=note_dao.get_by_name(xauth.current_name_str(), name))
        return dict(code="fail", message="unknown action")


class GetDialogHandler:

    def get_group_option_dialog(self, kw):
        note_id = xutils.get_argument_int("note_id")
        file = NoteDao.get_by_id(note_id)
        if file != None and file.children_count == 0:
            kw.show_delete_btn = True
        kw.file = file

    def fill_share_data(self, kw):
        note_id = xutils.get_argument_int("note_id")
        file = note_dao.get_by_id(note_id)
        kw.file = file
        kw.share_to_list = []

        if file != None:
            kw.share_to_list = dao_share.list_share_by_note_id(file.id)

    @xauth.login_required()
    def GET(self, name=""):
        kw = Storage()

        if name == "group_option_dialog":
            self.get_group_option_dialog(kw)

        return xtemplate.render("note/ajax/%s.html" % name, **kw)


class ViewPublicHandler:
    """查看公开的笔记"""

    def GET(self):
        id = xutils.get_argument_int("id")
        return ViewHandler().GET("view", id, is_public_page=True)

class PreviewPopupHandler:
    @xauth.login_required()
    def GET(self):
        name = xutils.get_argument_str("name")
        user_id = xauth.current_user_id()
        if name == "":
            return "错误:笔记名称为空"
        note_info = note_dao.get_by_name_or_alias(name = name, creator_id = user_id)
        if note_info is None:
            return self.render_search(name)
        if not note_info.is_markdown:
            return self.render_search(name)
        content = note_info.content
        try:
            import markdown
            content = textutil.get_short_text(content, 200)
            search_url = self.get_search_url(name)
            footer = f"""<div class="row">
                <a href="{note_info.url}">查看全文</a>
                <span>|</span>
                <a href="{search_url}">搜索【{name}】</a>
            </div>"""
            return markdown.markdown(content) + footer
        except:
            return self.render_search(name)
        
    def get_search_url(self,name=""):
        return f"/s/{encode_uri_component(name)}"
        
    def render_search(self, name=""):
        search_url = self.get_search_url(name)
        return f"""<div class="row"><a href="{search_url}">搜索【{name}】</a></div>"""

xurls = (
    r"/note/(edit|view)", ViewHandler,
    r"/note/print", PrintHandler,
    r"/note/(\d+)", ViewByIdHandler,
    r"/note/view/public", ViewPublicHandler,
    r"/note/view/([\w\-]+)", ViewByIdHandler,
    r"/note/history", NoteHistoryHandler,
    r"/note/history_view", HistoryViewHandler,
    r"/note/query/(\w+)", QueryHandler,
    r"/note/ajax/(.+)", GetDialogHandler,
    r"/file/mark", MarkHandler,
    r"/file/unmark", UnmarkHandler,
    r"/file/markdown", ViewHandler,
    r"/note/preview_popup", PreviewPopupHandler,
)
