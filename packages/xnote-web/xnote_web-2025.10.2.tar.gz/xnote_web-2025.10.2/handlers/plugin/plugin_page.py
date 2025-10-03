# -*- coding:utf-8 -*-
# @author xupingmao <578749341@qq.com>
# @since 2018/09/30 20:53:38
# @modified 2022/03/04 23:02:45
import os
import xutils
import web
import copy
import typing

from typing import Optional
from xnote.core import xconfig
from xnote.core import xtemplate
from xnote.core import xauth
from xnote.core import xmanager
from xnote.core import xnote_hooks
from xnote.core.models import SearchContext
from urllib.parse import urlparse

from xnote.core.xtemplate import T
from xutils import Storage
from xutils import logutil
from xutils import textutil, SearchResult, dateutil, u
from xutils import mem_util
from xutils import netutil
from configparser import ConfigParser
from handlers.plugin.dao import (
    add_visit_log, list_visit_logs, PageVisitLogDO)
from handlers.plugin.service import CategoryService
from handlers.plugin import plugin_util
from xnote.plugin import load_plugin_file, PluginContext, LinkConfig
from xnote.plugin import TagSpan, BaseContainer
from xnote.plugin import iter_plugins
from handlers.plugin.plugin_config import INNER_TOOLS
from xnote.plugin.list import ItemList, ListItem, TextTag

"""xnote插件模块，由于插件的权限较大，开发权限只开放给管理员，普通用户可以使用

插件的模型：插件包含两部分，程序和数据，程序部分存储在插件目录中的文件，数据存储在数据库或者文件中，
使用dbutil/fsutil接口操作数据
- 插件名称、描述、文件名、文件路径
- 插件的主类
- 插件的分类
- 插件的访问权限

插件的生命周期
- 插件的注册：debug模式下实时注册，非debug模式：初始化注册+按需注册
- 插件的卸载：退出应用
- 插件的刷新：刷新系统的时候重新加载
- 插件的删除：删除插件文件

插件日志：
- 日志关系：每个用户保留一个插件访问记录，记录最近访问的时间，访问的总次数
- 日志的创建：访问的时候创建
- 日志的更新：访问的时候更新
- 日志的删除：暂无

"""


class PluginState:
    status = "loading"
    config_tools: typing.List[PluginContext] = []

DEFAULT_PLUGIN_ICON_CLASS = "fa fa-cube"

def get_plugin_category_list():
    return CategoryService.category_list


def get_category_url_by_code(code):
    server_home = xconfig.WebConfig.server_home
    if code is None:
        return f"{server_home}/plugin_list?category=all"
    for item in CategoryService.category_list:
        if item.code == code:
            return f"{server_home}{item.url}"
    return f"{server_home}/plugin_list?category=%s" % code


def get_category_name_by_code(code: str):
    category = get_category_by_code(code)
    if category != None:
        return category.name

    # 如果没有定义，就返回code
    return code

xnote_hooks.get_category_name_by_code = get_category_name_by_code

def get_category_by_code(code: str):
    for item in CategoryService.category_list:
        if item.code == code:
            return item
    return None


def get_category_icon_class_by_code(code):
    category = get_category_by_code(code)
    if category is None:
        return DEFAULT_PLUGIN_ICON_CLASS
    return category.icon_class


def check_and_load_class(plugin: PluginContext):
    if plugin.clazz is not None:
        return

    load_plugin_file(plugin.fpath)


def load_inner_plugins():
    for tool in INNER_TOOLS:
        xconfig.PLUGINS_DICT[tool.url] = tool


def load_plugin_dir(dirname=None):
    """加载插件目录"""
    if dirname is None:
        dirname = xconfig.PLUGINS_DIR

    xconfig.PLUGINS_DICT = {}
    for root, dirs, files in os.walk(dirname):
        for fname in files:
            fpath = os.path.join(root, fname)
            load_plugin_file(fpath)

    load_inner_plugins()


def can_visit_by_role(plugin: PluginContext, current_role: typing.Optional[str]):
    if current_role == "admin":
        return True

    # permitted_role_list 优先级更高
    if current_role in plugin.permitted_role_list:
        return True

    if plugin.require_admin:
        return False

    if plugin.required_role is None:
        return True

    if plugin.required_role == current_role:
        return True

    return False


@xutils.timeit(logfile=True, logargs=True, name="FindPlugins")
def find_plugins(category: str, orderby=None):
    assert category != "all"
    current_role = xauth.get_current_role()
    user_name = xauth.current_name()
    plugins = []

    if current_role is None:
        # not logged in
        return plugins

    if category == "None":
        category = "other"

    for p in iter_plugins():
        if category in p.category_list:
            if can_visit_by_role(p, current_role):
                plugins.append(p)
    return sorted_plugins(user_name, plugins, orderby)

def build_inner_tools(user_name=None):
    if user_name is None:
        user_name = xauth.current_name()
    tools_copy = copy.copy(INNER_TOOLS)
    sort_plugins(user_name, tools_copy)
    return tools_copy

def get_plugin_values() -> typing.List[PluginContext]:
    values = xconfig.PLUGINS_DICT.values()
    return list(values)


class PluginSort:

    def __init__(self, user_name):
        self.user_name = user_name
        self.logs = list_visit_logs(user_name)

    def get_log_by_url(self, url: str):
        # 先精确搜索一次
        for log in self.logs:
            if log.url == url:
                assert isinstance(log, PageVisitLogDO)
                return log
        # 再用path搜索一次
        result = urlparse(url)
        webpath = result.path
        for log in self.logs:
            if log.url == webpath:
                return log
        return None

    def sort_by_visit_cnt_desc(self, plugins: typing.List[PluginContext]):
        plugins.sort(key=lambda x: x.visit_cnt, reverse=True)

    def sort_by_recent(self, plugins: typing.List[PluginContext]):
        plugins.sort(key=lambda x: x.visit_time, reverse=True)

    def update_visit_info(self, plugins: typing.List[PluginContext]):
        for p in plugins:
            log = self.get_log_by_url(p.url)
            if log:
                p.visit_time = log.visit_time
                p.visit_cnt = log.visit_cnt
            else:
                p.visit_cnt = 0
                p.visit_time = ""


def sort_plugins(user_name, plugins: typing.List[PluginContext], orderby=None):
    sort_obj = PluginSort(user_name)
    sort_obj.update_visit_info(plugins)

    if orderby is None or orderby == "":
        # 默认排序
        sort_obj.sort_by_visit_cnt_desc(plugins)
    elif orderby == "recent":
        sort_obj.sort_by_recent(plugins)
    else:
        raise Exception("invalid orderby:%s" % orderby)

    return plugins


def sorted_plugins(user_name, plugins: typing.List[PluginContext], orderby=None):
    sort_plugins(user_name, plugins, orderby)
    return plugins


def debug_print_plugins(plugins, ctx=None):
    if False:
        print("\n" * 5)
        print(ctx)
        for p in plugins:
            print(p)


@logutil.timeit_deco(name="list_all_plugins")
def list_all_plugins(user_name, sort=True, orderby=None):
    links = get_plugin_values()

    if sort:
        return sorted_plugins(user_name, links, orderby)

    return links


def list_other_plugins(sort=True):
    return find_plugins("other")


@logutil.timeit_deco(name="list_plugins")
def list_plugins(category: str, sort=True, orderby=None):
    user_name = xauth.current_name()

    if category == "other":
        plugins = list_other_plugins()
    elif category and category != "all":
        # 某个分类的插件
        plugins = find_plugins(category)
    else:
        # 所有插件
        plugins = list_all_plugins(user_name)

    links = plugins
    if sort:
        return sorted_plugins(user_name, links, orderby=orderby)
    return links

@logutil.timeit_deco(name="list_recent_plugins")
def list_recent_plugins():
    user_name = xauth.current_name()
    plugins = list_all_plugins(user_name, sort=False)
    links = plugins
    sort_plugins(user_name, links, "recent")
    return links


def get_plugin_title_name(plugin: PluginContext):
    """返回插件的title+name"""
    if plugin.name == "":
        return plugin.title
    if plugin.title == plugin.name:
        return plugin.title
    return u(plugin.title + "(" + plugin.name + ")")

@xmanager.searchable()
def on_search_plugins(ctx: SearchContext):
    if not xauth.is_admin():
        return

    if not ctx.search_tool:
        return

    if ctx.search_dict:
        return

    if PluginState.status == "loading":
        result = SearchResult()
        result.name = "插件加载中，暂时不可用"
        result.icon = "fa-th-large"
        result.url = "#"

        ctx.tools.append(result)
        return

    tag_list = []

    for plugin in search_plugins(ctx.key):
        plugin_name = get_plugin_title_name(plugin)
        tag_list.append(TagSpan(text=plugin_name, href=plugin.url))

    result_count = len(tag_list)
    if ctx.category != "plugin" and len(tag_list) > 0:
        more = SearchResult()
        more.name = u("搜索到[%s]个插件") % result_count
        more.icon = "fa-th-large"
        more.url = "/plugin_list?category=plugin&key=" + ctx.key
        more.show_more_link = True
        container = BaseContainer()
        container.set_children(tag_list[:5])
        more.html = container.render()
        ctx.tools.append(more)


def is_plugin_matched(p: PluginContext, words):
    return textutil.contains_all(p.title, words) \
        or textutil.contains_all(p.url, words) \
        or textutil.contains_all(p.fname, words)


def search_plugins(key) -> typing.List[PluginContext]:
    from xutils.functions import dictvalues
    user_name = xauth.current_name()
    words = textutil.split_words(key)
    plugins = list_all_plugins(user_name, True)
    result = dict()
    for p in plugins:
        if is_plugin_matched(p, words):
            result[p.url] = p
    return dictvalues(result)


def get_template_by_version(version):
    if version == "1":
        return "plugin/page/plugins_v1.html"
    if version == "2":
        return "plugin/page/plugins_v2.html"

    # 最新版本
    return "plugin/page/plugins_v3.html"


def filter_plugins_by_role(plugins, user_role):
    result = []
    for p in plugins:
        if user_role in p.permitted_role_list:
            result.append(p)
    return result


def fill_plugins_badge_info(plugins, orderby):
    if orderby == "" or orderby is None:
        # 默认按热度访问
        for p in plugins:
            p.badge_info = "热度: %s" % p.visit_cnt
    else:
        # 最近访问的
        for p in plugins:
            p.badge_info = dateutil.format_date(p.visit_time)


def create_item_list(plugins: typing.List[PluginContext]):
    result = ItemList()

    for plugin in plugins:
        item_info = ListItem(text = T(plugin.title), href= plugin.url + plugin.url_query, 
                                icon_class=plugin.icon_class, badge_info=plugin.badge_info)
        item_info.show_chevron_right = True
        if plugin.is_external:
            item_info.tags.append(TextTag("外部", css_class="lightblue"))
        result.add_item(item_info)
    return result

class PluginListHandler:

    @logutil.timeit_deco(name="PluginListHandler")
    @xauth.login_required()
    def GET(self):
        category = xutils.get_argument_str("category", "")
        key = xutils.get_argument("key", "")
        header = xutils.get_argument("header", "")
        version = xutils.get_argument("version", "")
        show_back = xutils.get_argument_bool("show_back")
        orderby = xutils.get_argument("orderby", "")

        context = Storage()
        context.category = category
        context.category_name = get_category_name_by_code(category)
        context.html_title = "插件"
        context.header = header
        context.show_back = show_back

        user_name = xauth.current_name_str()
        xmanager.add_visit_log(
            user_name, "/plugin_list?category=%s" % category)

        if category == "recent":
            category = "all"
            orderby = "recent"

        if xauth.is_admin():
            if key != "" and key != None:
                plugins = search_plugins(key)
                context.show_category = False
                context.show_back = "true"
                context.title = T("搜索插件")
            else:
                plugins = list_plugins(category, orderby=orderby)
        else:
            # 普通用户插件访问
            user_role = xauth.current_role()
            plugins = list_plugins(category)
            plugins = filter_plugins_by_role(plugins, user_role)

        fill_plugins_badge_info(plugins, orderby)

        plugins = self.filter_plugins(plugins)
        context.plugins = plugins
        context.plugins_status = PluginState.status

        if category == "":
            context.plugin_category = "all"

        template_file = get_template_by_version(version)
        context.parent_link = LinkConfig.app_index
        context.plugin_list = create_item_list(plugins)
        return xtemplate.render(template_file, **context)
    
    def filter_plugins(self, plugins: typing.List[PluginContext]):
        return [p for p in plugins if p.visible_in_list]


class PluginCategoryListHandler:

    @xauth.login_required()
    def GET(self):
        version = xutils.get_argument_str("version")
        current_role = xauth.current_role()
        total_count = 0
        count_dict = dict()

        for p in iter_plugins():
            if not can_visit_by_role(p, current_role):
                continue

            total_count += 1
            for category in p.category_list:
                count = count_dict.get(category, 0)
                count += 1
                count_dict[category] = count

        sorted_items = sorted(count_dict.items(),
                              key=lambda x: x[1], reverse=True)
        category_keys = list(map(lambda x: x[0], sorted_items))

        plugins = []

        # 全部插件
        root = PluginContext()
        root.title = T("全部")
        root.url = f"{xconfig.WebConfig.server_home}/plugin_list?category=all&show_back=true"
        root.badge_info = str(total_count)
        root.icon_class = DEFAULT_PLUGIN_ICON_CLASS
        root.build()
        plugins.append(root)

        for key in category_keys:
            if key == "":
                continue
            p = PluginContext()
            p.title = get_category_name_by_code(key)
            url = get_category_url_by_code(key)
            url = textutil.add_url_param(url, "show_back", "true")
            p.url = url
            p.icon_class = get_category_icon_class_by_code(key)
            p.badge_info = count_dict[key]
            p.build()
            plugins.append(p)

        template_file = get_template_by_version(version)
        kw = Storage()
        kw.plugins = plugins
        kw.plugin_category = "index"
        kw.parent_link = LinkConfig.app_index
        kw.plugin_list = create_item_list(plugins)
        return xtemplate.render(template_file, **kw)


class LoadPluginHandler:

    def resolve_force_reload(self):
        need_reload = xutils.get_argument_bool("_reload", False)
        return xauth.is_admin() and need_reload

    def load_plugin(self, name, force_reload=False) -> Optional[PluginContext]:
        context = xconfig.PLUGINS_DICT.get(name)

        if context == None or force_reload:
            fpath = os.path.join(xconfig.PLUGINS_DIR, name)
            fpath = xutils.get_real_path(fpath)
            if not os.path.exists(fpath):
                return None
            # 发现了新的插件，重新加载一下
            return load_plugin_file(fpath)
        else:
            return context

    def GET(self, name=""):
        user_name = xauth.current_name_str()
        name = xutils.unquote(name)
        try:
            url = "/plugin/" + name
            force_reload = self.resolve_force_reload()
            plugin = self.load_plugin(name, force_reload)
            if plugin != None:
                # 访问日志
                add_visit_log(user_name, url)
                check_and_load_class(plugin)
                clazz = plugin.clazz
                assert clazz != None
                # 渲染页面
                return clazz().render()
            else:
                # 加载插件失败，删除日志，插件开发过程中出现误删，先不处理
                # delete_visit_log(user_name, name, url)
                return xtemplate.render("error.html",
                                        error="插件[%s]不存在!" % name)
        except:
            error = xutils.print_exc()
            return xtemplate.render("error.html", error=error)

    def POST(self, name=""):
        return self.GET(name)

class PluginLogHandler:

    @xauth.login_required()
    def GET(self):
        user_name = xauth.current_name_str()
        logs = list_visit_logs(user_name)
        return logs


@xmanager.listen("sys.reload")
@mem_util.log_mem_info_deco("reload_plugins")
def reload_plugins(ctx):
    PluginState.status = "loading"
    reload_plugins_by_config()
    load_plugin_dir()
    PluginState.status = "done"


@xutils.log_init_deco("reload_plugins_by_config")
def reload_plugins_by_config(ctx=None):
    parser = ConfigParser()

    fpath = "config/plugin/plugins.ini"
    sections = parser.read(fpath, encoding="utf-8")

    tmp_tools = []
    for section in parser.sections():
        name = parser.get(section, "name", fallback="")
        url = parser.get(section, "url", fallback="")
        category = parser.get(section, "category", fallback="")
        editable = parser.getboolean(section, "editable", fallback=False)

        # 构建上下文
        context = PluginContext()
        context.name = name
        context.title = name
        context.url = url
        context.editable = editable
        context.category = category

        tmp_tools.append(context)

    PluginState.config_tools = tmp_tools


xutils.register_func("plugin.find_plugins", find_plugins)
xutils.register_func("plugin.get_category_list", get_plugin_category_list)
xutils.register_func("plugin.get_category_url_by_code",get_category_url_by_code)

xurls = (
    r"/plugin/(.+)", LoadPluginHandler,
    r"/plugin_list", PluginListHandler,
    r"/plugin_category_list", PluginCategoryListHandler,
    r"/plugin_log", PluginLogHandler,
)
