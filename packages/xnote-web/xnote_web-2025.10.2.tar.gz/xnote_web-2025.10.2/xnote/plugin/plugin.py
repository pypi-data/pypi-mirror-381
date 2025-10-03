# -*- coding:utf-8 -*-
"""
@Author       : xupingmao
@email        : 578749341@qq.com
@Date         : 2023-10-29 15:43:50
@LastEditors  : xupingmao
@LastEditTime : 2023-10-29 16:32:24
@FilePath     : /xnote/xnote/plugin/plugin.py
@Description  : 插件管理
"""

import os
import xutils
import enum
import typing

from xnote.core import xconfig
from xutils import mem_util, fsutil, Storage, attrget, ScriptMeta
from xnote.core.xtemplate import BasePlugin
from xnote.core import xtables

DEFAULT_PLUGIN_ICON_CLASS = "fa fa-cube"


class PluginMetaKey(enum.Enum):
    api_level = "api-level"
    category = "category"
    id = "id"
    author = "author"


def _get_absolute_url(url: str):
    server_home = xconfig.WebConfig.server_home
    if url.startswith(server_home):
        return url
    return server_home + url

class PluginContext(Storage):
    """插件上下文"""

    def __init__(self):
        self.meta = ScriptMeta()
        self.title = "" # 展示的名称
        self.description = ""
        
        self.name = "" # 文件名称
        self.plugin_id = "" # 唯一识别符号
        self.plugin_name = "" # 相对plugin目录的名称
        self.fname = ""
        self.fpath = ""
        
        self.url = ""  # 这个应该算是基础url，用于匹配访问日志
        self.url_query = ""  # 查询参数部分
        self.abs_url = "" # URL的绝对路径
        self.category = "" # type: str
        self.category_list = []
        
        self.require_admin = True
        self.required_role = "" # type: None|str
        self.permitted_role_list = []  # 允许访问的权限列表
        self.atime = ""
        self.editable = True
        self.edit_link = ""
        self.clazz = None # type: None|type[BasePlugin] # BasePlugin的类型
        self.priority = 0
        self.icon = DEFAULT_PLUGIN_ICON_CLASS
        self.author = None
        self.version = None
        self.debug = False
        self.badge_info = "" # 角标信息
        self.is_external = False # 是否是外部插件
        self.visible_in_list = True # 是否在列表中展示
        self.visit_time = xtables.DEFAULT_DATETIME # 访问时间
        self.visit_cnt = 0
    
    @property
    def link(self):
        return self.url
    
    @link.setter
    def link(self, link=""):
        self.url = link

    @property
    def is_builtin(self):
        return not self.is_external

    # sort方法重写__lt__即可
    def __lt__(self, other: "PluginContext"):
        return self.title < other.title

    def load_category_info(self, meta_obj: ScriptMeta):
        self.category = meta_obj.get_str_value("category")  # 这里取第一个分类
        self.category_list = meta_obj.get_list_value("category")  # 获取分类列表
        self.build_category()

    def load_permission_info(self, meta_obj: ScriptMeta):
        self.require_admin = meta_obj.get_bool_value(
            "require-admin", True)  # 访问是否要求管理员权限
        self.permitted_role_list = meta_obj.get_list_value(
            "permitted-role")  # 允许访问的角色

    def load_from_meta(self, meta_obj: ScriptMeta):
        self.api_level = meta_obj.get_float_value("api-level", 0.0)

        if self.api_level >= 2.8:
            self.title = meta_obj.get_str_value("title")
            self.description = meta_obj.get_str_value("description")
            self.author = meta_obj.get_str_value("author")
            self.version = meta_obj.get_str_value("version")
            self.icon = meta_obj.get_str_value("icon-class")
            self.since = meta_obj.get_str_value("since")
            self.debug = meta_obj.get_bool_value("debug")

            self.load_category_info(meta_obj)
            self.load_permission_info(meta_obj)

    def build_category(self):
        if self.category is None and len(self.category_list) > 0:
            self.category = self.category_list[0]

        if self.category != None and self.category not in self.category_list:
            self.category_list.append(self.category)

        if self.category is None and len(self.category_list) == 0:
            self.category = "other"
            self.category_list.append(self.category)

    def build_permission_info(self):
        if self.clazz != None:
            self.clazz.permitted_role_list = self.permitted_role_list

    def build(self):
        """构建完整的对象"""
        self.build_category()
        self.build_permission_info()

        if self.icon is None:
            self.icon = DEFAULT_PLUGIN_ICON_CLASS
            self.icon_class = DEFAULT_PLUGIN_ICON_CLASS
        if self.url == "":
            self.url = f"/plugin/{self.plugin_name}"
        
        self.abs_url = _get_absolute_url(self.url)


def is_plugin_file(fpath: str):
    return os.path.isfile(fpath) and fpath.endswith(".py")


@mem_util.log_mem_info_deco("load_plugin_file", log_args=True)
def load_plugin_file(fpath: str, fname=None, raise_exception=False):
    if not is_plugin_file(fpath):
        return
    if fname is None:
        fname = os.path.basename(fpath)
    dirname = os.path.dirname(fpath)

    # 相对于插件目录的名称
    plugin_name = fsutil.get_relative_path(fpath, xconfig.FileConfig.plugins_dir)

    vars = dict()
    vars["script_name"] = plugin_name
    vars["fpath"] = fpath

    try:
        meta = xutils.load_script_meta(fpath)
        context = PluginContext()
        context.is_external = True
        context.icon_class = DEFAULT_PLUGIN_ICON_CLASS
        # 读取meta信息
        context.load_from_meta(meta)
        context.fpath = fpath
        context.plugin_id = meta.get_str_value("plugin_id")
        context.meta = meta
        context.plugin_name = plugin_name
        
        if context.plugin_id == "":
            # 兼容没有 plugin_id 的数据
            context.plugin_id = fpath

        if meta.has_tag("disabled"):
            return

        # 2.8版本之后从注解中获取插件信息
        module = xutils.load_script(fname, vars, dirname=dirname)
        main_class = vars.get("Main")
        return load_plugin_by_context_and_class(context, main_class)
    except Exception as e:
        # TODO 增加异常日志
        xutils.print_exc()
        if raise_exception:
            raise e

def load_plugin_by_context(context: PluginContext):
    assert isinstance(context, PluginContext)
    assert context.plugin_name != ""
    assert context.clazz != None
    assert context.title != ""
    
    context.build()
    plugin_name = context.plugin_name
    xconfig.PLUGINS_DICT[plugin_name] = context

def load_plugin_by_context_and_class(context: PluginContext, main_class = None):
    if main_class != None:
        if not issubclass(main_class, BasePlugin):
            raise Exception("main_class must be subclass of BasePlugin")
        
        fname = context.fname
        fpath = context.fpath
        plugin_name = context.plugin_name

        # 更新类的属性
        main_class.fname = fname
        main_class.fpath = fpath

        # 实例化插件
        instance = main_class()
        context.name = os.path.splitext(fname)[0]

        if context.api_level < 2.8:
            context.title = instance.title
            context.category = instance.category
            context.required_role = instance.required_role

        if context.api_level >= 2.8:
            main_class.title = context.title
            main_class.category = context.category
            main_class.permitted_role_list = context.permitted_role_list

        context.url = f"/plugin/{plugin_name}"
        context.clazz = main_class
        context.edit_link = "code/edit?path=" + fpath

        # 初始化插件
        if hasattr(main_class, 'on_init'):
            instance.on_init(context)

        # 注册插件
        xconfig.PLUGINS_DICT[plugin_name] = context
        context.build()
        return context

def find_plugin(url: str) -> typing.Optional[PluginContext]:
    return xconfig.PLUGINS_DICT.get(url)


def iter_plugins() -> typing.Generator[PluginContext, None, None]:
    yield from xconfig.PLUGINS_DICT.values()
