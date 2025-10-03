# encoding=utf-8

import time
import xutils

from xutils import SearchResult, u, Storage, functions
from xnote.core import xmanager, xconfig, xauth, xtemplate
from xnote.core.models import SearchContext
from handlers.message import dao, message_utils


@xmanager.searchable()
def on_search_message(ctx: SearchContext):
    if ctx.search_message is False:
        return
    
    if ctx.user_id == 0:
        return

    key = ctx.key
    message_utils.touch_key_by_content(ctx.user_name, 'key', key)

    handle_search_event(ctx, tag_name="待办", search_tag="task")
    handle_search_event(ctx, tag_name="随手记", search_tag="log")
    


def handle_search_event(ctx: SearchContext, tag_name="", search_tag="log"):
    key = ctx.key
    max_len = xconfig.SEARCH_SUMMARY_LEN

    if ctx.option.show_message_detail:
        # 搜索详情
        limit = 1000
    else:
        limit = 3

    messages, count = dao.search_message(ctx.user_id, key, offset=0, limit=limit, search_tags=[search_tag])
    search_result = []
    for message in messages:
        item = SearchResult()
        if message.content != None and len(message.content) > max_len:
            message.content = message.content[:max_len] + "......"
        message_utils.process_message(message)
        item.tag_name = tag_name
        item.tag_class = "orange"
        item.name = f"【{tag_name}】{message.ctime}"
        item.html = message.html
        item.icon = "hide"
        search_result.append(item)
        # print(message)
        
    if not ctx.option.show_message_detail:
        show_message_detail = xconfig.get_user_config(
            ctx.user_name, "search_message_detail_show")

        if show_message_detail == "false":
            search_result = []

    if count > 0:
        more = SearchResult()
        more.name = f"搜索到[{count}]条{tag_name}" 
        more.url = f"{xconfig.WebConfig.server_home}/message?tag={search_tag}.search&key=" + ctx.key
        more.icon = "fa-file-text-o"
        more.show_more_link = True
        more.show_move = False
        search_result.insert(0, more)

    if len(search_result) > 0:
        ctx.messages += search_result


class SearchHandler:
    """搜索逻辑处理"""

    def get_page(self):
        user_name = xauth.current_name_str()
        key = xutils.get_argument_str("key", "")
        tag = xutils.get_argument_str("tag", "search")

        kw = Storage()
        kw.tag = tag
        kw.key = key
        kw.keyword = key
        kw.default_content = message_utils.filter_key(key)
        kw.side_tags = self.list_side_tags(tag, user_name, 20)
        kw.create_tag = self.get_create_tag()
        kw.show_create_on_tag = kw.create_tag != "forbidden"
        kw.is_keyword_marked = message_utils.is_marked_keyword(user_name, key)
        kw.is_task_tag = message_utils.is_task_tag(tag)
        kw.search_type = message_utils.TagHelper.get_search_type(tag)
        kw.search_ext_dict = dict(tag = tag)

        return xtemplate.render("message/page/message_search.html", **kw)

    def get_ajax_data(self, *, user_name="", key="", offset=0,
                      limit=20, search_tags=None, no_tag=False, date=""):
        start_time = time.time()
        user_id = xauth.UserDao.get_id_by_name(user_name)
        chatlist, amount = dao.search_message(
            user_id, key, offset, limit,
            search_tags=search_tags, no_tag=no_tag, date=date)

        # 搜索扩展
        xmanager.fire("message.search", SearchContext(key))

        # 自动置顶
        message_utils.touch_key_by_content(user_name, "key", key)
        similar_key = message_utils.get_similar_key(key)
        if key != similar_key:
            message_utils.touch_key_by_content(user_name, "key", similar_key)

        cost_time = functions.second_to_ms(time.time() - start_time)

        dao.add_search_history(user_name, key, cost_time)

        return chatlist, amount

    def search_items(self, user_name, key):
        pass

    def get_create_tag(self):
        p = xutils.get_argument_str("p", "")
        if p == "task":
            return "task"

        if p == "log":
            return "log"

        return "forbidden"

    def list_side_tags(self, tag="", user_name="", limit=20):
        if message_utils.is_task_tag(tag):
            return message_utils.list_task_tags(user_name=user_name, limit=limit, tag=tag)
        else:
            return message_utils.list_hot_tags(user_name=user_name, limit=limit)
    
