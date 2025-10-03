# -*- coding:utf-8 -*-
# @author xupingmao <578749341@qq.com>
# @since 2019/08/10 23:44:48
# @modified 2022/04/16 22:36:45
import math
import xutils
import typing

from xnote.core import xconfig
from xnote.core import xauth
from xnote.core import xtemplate
from xnote.core import xmanager
from xutils import DAO
from xutils import Storage
from urllib.parse import quote
from xutils import textutil
from xnote.core.xtemplate import T
from . import dao as note_dao
from . import dao_comment
from xutils import webutil
from xutils import dateutil
from xnote.core.models import SearchContext, SearchResult
from .dao_comment import search_comment, CommentDO
from xutils.text_parser import TokenType
from .models import NoteTypeInfo
from handlers.note.note_service import NoteService
from handlers.note.dao import NoteIndexDao

NOTE_DAO = DAO("note")

def get_page_max(count):
    return int(math.ceil(count/xconfig.PAGE_SIZE))


def translate_search(key0: str):
    key = key0.lstrip("")
    key = key.rstrip("")
    quoted_key = textutil.quote(key)
    value = textutil.escape_html(key0)
    fmt = "<a class=\"link\" href=\"/search?search_type=comment&key={quoted_key}\">{value}</a>"
    return fmt.format(quoted_key=quoted_key, value=value)

def mark_text(content):
    from xutils.text_parser import TextParser
    from xutils.text_parser import set_img_file_ext
    # 设置图片文集后缀
    set_img_file_ext(xconfig.FS_IMG_EXT_LIST)

    parser = TextParser()
    tokens = parser.parse_to_tokens(content)

    for token in tokens:
        if token.type in (TokenType.topic, TokenType.search):
            token.html = translate_search(token.value)

    # parser.set_topic_translator(search_translator)
    # parser.set_search_translator(search_translator)

    text_tokens = parser.get_text_tokens(tokens)
    return "".join(text_tokens)

def process_comments(comments: typing.List[CommentDO], show_note = False):
    for comment in comments:
        if comment.content is None:
            continue
        comment.html = mark_text(comment.content)

        if show_note:
            note = note_dao.get_by_id(comment.note_id, include_full=False)
            if note != None:
                comment.note_name = note.name
                comment.note_url  = note.url

def search_comment_summary(ctx: SearchContext):
    comments = dao_comment.search_comment(user_name = ctx.user_name, keywords = ctx.words)
    if len(comments) > 0:
        result = SearchResult()
        result.name = "搜索到[%s]条评论" % len(comments)
        result.url  = "/search?key=%s&search_type=comment" % quote(ctx.key)
        result.icon = "fa-comments-o"
        result.show_more_link = True
        ctx.messages.append(result)

def search_comment_detail(ctx: SearchContext):
    """搜索评论详细列表接口
    @param {SearchContext} ctx 搜索上下文
    @return None
    """
    result = []
    comments = dao_comment.search_comment(user_name = ctx.user_name, keywords = ctx.words)

    process_comments(comments, show_note = True)

    for item in comments:
        item.icon = "fa-comment-o"
        item.name = "[评论] %s" % item.note_name
        item.url  = item.note_url
        item.mtime = item.ctime
        result.append(item)

    ctx.messages += result

@xmanager.searchable(r".+")
def on_search_comments(ctx: SearchContext):
    if ctx.category == "default":
        search_comment_summary(ctx)

    if ctx.category == "comment":
        search_comment_detail(ctx)

def convert_to_html(comments, show_note = False, page = 1, page_max = 1, show_edit = False, note_user_id=0):
    return xtemplate.render("note/page/comment/comment_list_ajax.html", 
        show_comment_edit = show_edit,
        page = page,
        page_max = page_max,
        comments = comments, 
        show_note = show_note,
        note_user_id=note_user_id)

class CommentListAjaxHandler:

    def GET(self):
        note_id   = xutils.get_argument_int("note_id")
        list_type = xutils.get_argument_str("list_type")
        resp_type = xutils.get_argument_str("resp_type")
        list_date = xutils.get_argument_str("list_date")
        show_note = xutils.get_argument_bool("show_note")
        show_edit = xutils.get_argument_bool("show_edit")
        comment_order = xutils.get_argument_str("comment_order")
        page = xutils.get_argument_int("page", 1)
        page_max  = 1
        page_size = xconfig.PAGE_SIZE
        user_info = xauth.current_user()
        user_name = ""
        user_id = 0
        note_user_id = 0
        
        # can visit comment without login
        if user_info != None:
            user_name = user_info.name
            user_id = user_info.user_id

        offset = max(0, page-1) * page_size

        if list_type == "user":
            if user_id == 0:
                raise Exception("user not login")
            count  = dao_comment.count_comments_by_user(user_id, list_date)
            comments = dao_comment.list_comments_by_user(user_id=user_id, 
                date = list_date, offset = offset, 
                limit = page_size)
        elif list_type == "search":
            comments = self.search_comments(user_name)
            count = len(comments)
        else:
            assert note_id > 0
            note_index = NoteIndexDao.get_by_id(note_id)
            if note_index is None:
                raise Exception("笔记不存在")
            NoteService.check_auth(note_index, user_id=user_id)
            comments  = dao_comment.list_comments(note_id, offset = offset, limit = page_size, 
                                                  user_name=user_name, order=comment_order)
            count = dao_comment.count_comment_by_note(note_id)
            note_user_id = note_index.creator_id
        
        page_max = get_page_max(count)

        # 处理评论列表
        process_comments(comments, show_note)

        if resp_type == "html":
            return convert_to_html(comments, show_note, 
                page = page, page_max = page_max, show_edit = show_edit, note_user_id=note_user_id)
        else:
            return comments
    
    def search_comments(self, user_name):
        key = xutils.get_argument_str("key", "")
        note_id = xutils.get_argument("note_id", "")
        keywords = textutil.split_words(key)
        return search_comment(user_name = user_name, keywords = keywords, limit=1000, note_id = note_id)

class SaveCommentAjaxHandler:

    @xauth.login_required()
    def POST(self):
        note_id = xutils.get_argument_int("note_id")
        content = xutils.get_argument_str("content")
        type = xutils.get_argument_str("type")
        user_info = xauth.current_user()

        if user_info == None:
            return webutil.FailedResult(code="403", message="请登录进行操作~")

        if note_id == 0:
            return webutil.FailedResult(message="note_id参数为空")
        
        if content == "":
            return webutil.FailedResult(code = "400", message = "content参数为空")

        comment = dao_comment.CommentDO()
        comment.user = user_info.name
        comment.user_id = user_info.id
        comment.type = type
        comment.content = content
        comment.note_id = note_id

        dao_comment.create_comment(comment)
        note_dao.touch_note(note_id)
        
        return dict(code = "success", success = True)

class DeleteCommentAjaxHandler:

    def GET(self):
        return self.POST()

    @xauth.login_required()
    def POST(self):
        comment_id = xutils.get_argument_int("comment_id")
        user       = xauth.current_name()
        comment    = dao_comment.get_comment(comment_id)
        if comment is None:
            dao_comment.delete_index(comment_id)
            return webutil.SuccessResult()
        if user != comment.user:
            return webutil.FailedResult(message = "unauthorized")
        dao_comment.delete_comment(comment_id)
        return webutil.SuccessResult()

class MyCommentsHandler:

    @xauth.login_required()
    def GET(self):
        user_name = xauth.current_name_str()
        xmanager.add_visit_log(user_name, "/note/comment/mine")
        date = xutils.get_argument_str("date", "")

        kw = Storage()
        kw.show_comment_title = False
        kw.show_comment_create = False
        kw.show_comment_note = True
        kw.comment_list_date = date
        kw.comment_list_type = "user"
        kw.note_type = "comment"
        kw.type_list = NoteTypeInfo.get_type_list()

        return xtemplate.render("note/page/comment/comment_user_page.html", **kw)

class CommentAjaxHandler:

    @xauth.login_required()
    def GET(self):
        p = xutils.get_argument_str("p")
        user_name = xauth.current_name()
        comment_id = xutils.get_argument_int("comment_id")

        if p == "edit":
            comment = dao_comment.get_comment(comment_id)
            if comment == None:
                return "评论不存在"
            if comment.user != user_name:
                return "无操作权限"
            return xtemplate.render("note/page/comment/comment_edit_dialog.html", comment = comment)
        
        if p == "update":
            comment = dao_comment.get_comment(comment_id)
            if comment == None:
                return webutil.FailedResult(code = "404", message = "评论不存在")
            if comment.user != user_name:
                return webutil.FailedResult(code = "403", message = "无权限操作")
            content = xutils.get_argument_str("content", "")
            date = xutils.get_argument_str("date")
            old_date = dateutil.parse_date_to_object(comment.ctime)
            update_ctime = False
            if date != old_date.format_date():
                comment.ctime = f"{date} {old_date.time}"
                update_ctime = True
            comment.content = content
            dao_comment.CommentDao.update(comment, update_ctime=update_ctime)
            return webutil.SuccessResult()
        return "未知的操作"

    def POST(self):
        return self.GET()
    
class UpdatePinLevelHandler:

    @xauth.login_required()
    def POST(self):
        comment_id = xutils.get_argument_int("comment_id")
        pin_level = xutils.get_argument_int("pin_level")
        user_id = xauth.current_user_id()
        comment_index = dao_comment.CommentDao.get_index_by_id(comment_id=comment_id)
        if comment_index is None:
            return webutil.FailedResult("404", message="评论不存在")
        note_index = NoteIndexDao.get_by_id(note_id=comment_index.target_id)
        if note_index is None:
            return webutil.FailedResult("404", message="笔记不存在")
        if note_index.creator_id != user_id:
            return webutil.FailedResult("401", message="没有操作权限")
        comment_index.pin_level = pin_level
        dao_comment.CommentDao.update_index(comment_index)
        return webutil.SuccessResult()

xutils.register_func("note.search_comment_detail", search_comment_detail)

xurls = (
    r"/note/comment", CommentAjaxHandler,
    r"/note/comments", CommentListAjaxHandler,
    r"/note/comment/list", CommentListAjaxHandler,
    r"/note/comment/save", SaveCommentAjaxHandler,
    r"/note/comment/delete", DeleteCommentAjaxHandler,
    r"/note/comment/mine", MyCommentsHandler,
    r"/note/comment/update_pin_level", UpdatePinLevelHandler,
)