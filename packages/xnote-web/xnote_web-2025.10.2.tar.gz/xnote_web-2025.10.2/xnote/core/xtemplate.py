# -*- coding:utf-8 -*-
# @author xupingmao <578749341@qq.com>
# @since 2016/12/05
# @modified 2022/03/19 01:13:01
# @filename xtemplate.py


"""这个模块的主要作用是提供模板处理的统一接口，包括
- 渲染模板，封装了对tornado模板的魔改版本
    - 支持多语言配置
    - 支持多设备适配
- 插件模板，定义了插件的基类
"""
import os
import warnings
import math
import web # type: ignore
import xutils
import functools
import time
import typing

from xnote.core import xconfig, xauth, xnote_trace, xnote_hooks
from xnote.core import xnote_user_config
from xnote.core.xconfig import TemplateConfig
from xutils.tornado.template import Template, Loader
from xutils import dateutil, u
from xutils import tojson
from xutils import Storage
from xutils import textutil
from urllib.parse import quote

TEMPLATE_DIR = xconfig.HANDLERS_DIR
NAMESPACE = dict(
    format_date=dateutil.format_date,
    format_time=dateutil.format_time,
    quote=quote
)

_mobile_name_dict = dict() # type: dict[str, str]
LOAD_TIME = int(time.time())

def T(text: str, lang=None):
    if lang is None:
        lang = xconfig.get_current_user_config("LANG")

    mapping = TemplateConfig.get_lang_mapping(lang) # type: None | dict[str, str]
    if mapping is None:
        return text
    else:
        return mapping.get(text, text)

class XnoteTemplateVars:
    """xnote模板参数"""
    show_nav = True

class TemplateMapping:

    def __init__(self, prefix="", dirname=""):
        self.prefix = prefix
        self.dirname = dirname

class XnoteLoader(Loader):
    """定制Template Loader"""

    _instance = None # type: XnoteLoader|None
    path_mapping = {} # type: dict[str, str]
    template_mapping_list = [] # type: list[TemplateMapping]
    memory_prefix = "memory:"

    def __init__(self, *args, **kw):
        super(XnoteLoader, self).__init__(*args, **kw)
        self.reset()
        self.init_path_mapping()

    @classmethod
    def get_instance(cls):
        # type: () -> XnoteLoader
        instance = cls._instance
        if instance is None:
            raise AssertionError("XnoteLoader instance is None")
        return instance
    
    @classmethod
    def init_instance(cls, root_directory="", namespace={}):
        cls._instance = XnoteLoader(root_directory, namespace=namespace)

    def set_namespace(self, namespace):
        self.namespace = namespace

    def init_path_mapping(self):
        self.path_mapping = {
            "$base_nav_left": xconfig.FileConfig.template_base_nav_left,
            "$base_nav_top": xconfig.FileConfig.template_base_nav_top,
        }
        self.template_mapping_list = [
            TemplateMapping("$ext/", xconfig.FileConfig.ext_handlers_dir),
            TemplateMapping("$plugin/", xconfig.FileConfig.plugins_dir),
        ]

    def resolve_path_old(self, name: str, parent_path: typing.Optional[str] = None):
        """这是默认的按照相对路径处理模板路径"""
        if parent_path and not parent_path.startswith("<") and \
            not parent_path.startswith("/") and \
                not name.startswith("/"):
            current_path = os.path.join(self.root, parent_path)
            file_dir = os.path.dirname(os.path.abspath(current_path))
            relative_path = os.path.abspath(os.path.join(file_dir, name))
            if relative_path.startswith(self.root):
                name = relative_path[len(self.root) + 1:]
        return name

    def resolve_path(self, name: str, parent_path=None):
        """tornado中的Template._get_ancestors方法会把template的路径作为parent_path参数,
        但是Loader默认的方法处理绝对路径时，不处理相对路径,参考resolve_path_old
        由于判断绝对路径是通过`/`开头，这样造成windows系统和posix系统的处理结果不一致

        统一修改为`{% extends <abspath> %}` 和 `{% include <abspath> %}`, 继承和包含的模板路径强制为全局的，
        这样做的好处是一般全局母版的位置是不变的，移动模块不需要修改母版位置，这里的`全局`也并不是真的全局，
        而是寻找母版或者include模板时不进行路径转换
        """
        # 处理默认的模板，这里hack掉
        if name == "base":
            return os.path.join(xconfig.HANDLERS_DIR, xconfig.BASE_TEMPLATE)
        
        if name == "wide_base":
            return os.path.join(xconfig.HANDLERS_DIR, xconfig.WIDE_BASE_TEMPLATE)
        
        name = self.path_mapping.get(name, name)

        for template_mapping in self.template_mapping_list:
            if name.startswith(template_mapping.prefix):
                relative_path = name[len(template_mapping.prefix):]
                return os.path.join(template_mapping.dirname, relative_path)
        
        if name.startswith(self.memory_prefix):
            # 内存中的模板
            return name
        
        if name.endswith(".str"):
            # 字符串类型的模板,只在内存中存在
            return name

        return os.path.join(xconfig.HANDLERS_DIR, name)

    def _create_template(self, name: str):
        if name.startswith(self.memory_prefix):
            raise Exception(f"memory template not init: {name}")
        
        if name.endswith(".str"):
            raise Exception(f"str template not init: {name}")
        
        path = name
        with open(path, "rb") as f:
            template = Template(f.read(), name=name, loader=self)
            return template

    def init_template(self, name: str, text: str):
        self.templates[name] = Template(text, name=name, loader=self)


def get_user_agent():
    return xutils.get_client_user_agent()

def render_before_kw(kw: dict):
    """模板引擎预处理过程"""
    user_info = xauth.current_user()
    user_name = ""
    user_id = 0
    if user_info != None:
        user_id = user_info.user_id
        user_name = user_info.name
    
    user_role = xauth.current_role() or ""

    kw["math"] = math
    kw["_server_home"] = xconfig.WebConfig.server_home
    kw["_is_admin"] = xauth.is_admin()
    kw["_has_login"] = xauth.has_login()
    kw["_user_name"] = user_name
    kw["_user_id"] = user_id
    kw["_user_role"] = user_role
    kw["_user_agent"] = get_user_agent()
    # 用于渲染其他组件
    kw["_render"] = render
    kw["_nav_list"] = TemplateConfig.nav_list
    kw["_is_mobile"] = is_mobile_device()
    kw["_is_desktop"] = xutils.is_desktop_client()
    kw["Storage"] = Storage
    kw["xutils"] = xutils
    kw["xconfig"] = xconfig
    kw["T"] = T
    kw["_ts"] = LOAD_TIME  # 用于标识前端资源的缓存版本

    # 用户配置
    kw["_user_config"] = xnote_user_config.get_config_dict(user_name)
    kw["FONT_SCALE"] = xconfig.get_user_config(user_name, "FONT_SCALE")
    kw["HOME_PATH"] = xconfig.get_user_config(user_name, "HOME_PATH")
    kw["THEME"] = xconfig.get_user_config(user_name, "THEME")
    kw["_debug_info"] = xnote_trace.get_debug_info()

    if hasattr(web.ctx, "env"):
        kw["HOST"] = web.ctx.env.get("HTTP_HOST")

    if len(xconfig.errors) > 0:
        kw["warn"] = "; ".join(xconfig.errors)

    # 处理用户输入
    _input = web.ctx.get("_xnote.input")
    if _input is not None:
        kw.update(_input)


def render_after_kw(kw):
    """后置渲染，可以覆盖前面的数据"""
    render_search(kw)

    kw["_cost_time"] = xnote_trace.get_cost_time()


def get_mobile_template(name: str):
    global _mobile_name_dict
    global TEMPLATE_DIR

    cached_name = _mobile_name_dict.get(name)
    if cached_name != None:
        return cached_name

    if name.endswith(".html"):
        # 检查文件是否存在
        mobile_name = textutil.remove_tail(name, ".html") + ".mobile.html"
        fpath = os.path.join(TEMPLATE_DIR, mobile_name)
        if os.path.exists(fpath):
            _mobile_name_dict[name] = mobile_name
            return mobile_name
    _mobile_name_dict[name] = name
    return name


def is_mobile_device(user_agent=None):
    return xutils.is_mobile_client(user_agent)


def get_device_platform():
    platform = web.ctx.get("xnote_platform")
    if platform != None:
        return platform

    platform = _do_get_device_platform()
    web.ctx.xnote_platform = platform
    return platform


def _do_get_device_platform():
    return xutils.get_client_platform()


def render_by_ua(name, **kw):
    if is_mobile_device():
        # 部分移动设备的兼容性不行，无法使用codeMirror组件，要用简化版页面
        mobile_name = get_mobile_template(name)
        return render(mobile_name, **kw)
    return render(name, **kw)


def render_search(kw):
    # 已经定义了搜索行为
    if "search_action" in kw:
        return

    search_type = kw.get("search_type")
    handler = xnote_hooks.get_search_handler(search_type)
    if handler != None:
        kw["search_action"] = handler.action
        kw["search_placeholder"] = handler.placeholder
        kw["search_tag"] = handler.tag


def do_render_kw(kw):
    nkw = dict()
    # 预处理
    render_before_kw(nkw)

    # 传入的kw生效
    nkw.update(kw)

    # 后置处理
    render_after_kw(nkw)

    return nkw


@xutils.timeit_deco(name="Template.Render", logfile=True)
def render(template_name, **kw):
    _loader = XnoteLoader.get_instance()
    # 处理上下文渲染
    nkw = do_render_kw(kw)

    if hasattr(web.ctx, "env"):
        # 非web请求（比如单元测试等）
        _input = web.input()
        if _input.get("_format") == "json":
            web.header("Content-Type", "application/json")
            return tojson(nkw)
    return _loader.load(template_name).generate(**nkw)

def compile_template(text: str, name="<string>"):
    """预编译模板"""
    return Template(text, name=name, loader=XnoteLoader.get_instance())

def register_memory_template(name: str, text: str):
    """注册内存模板"""
    loader=XnoteLoader.get_instance()

    if not name.startswith(XnoteLoader.memory_prefix):
        raise Exception(f"template name must startswith `{XnoteLoader.memory_prefix}`")
    loader.init_template(name=name, text=text)

@functools.lru_cache(maxsize=128)
def get_md5_hex_with_cache(text=""):
    return xutils.md5_hex(text)

def render_text(text: str, template_name="<string>", **kw):
    """使用模板引擎渲染文本信息,使用缓存
    """
    _loader = XnoteLoader.get_instance()

    nkw = do_render_kw(kw)

    # 通过缓存加快md5的计算
    # 使用hash不能保证唯一性
    text_md5 = get_md5_hex_with_cache(text)

    name = f"{XnoteLoader.memory_prefix}{template_name}_{text_md5}"
    if name not in _loader.templates:
        _loader.init_template(name, text)
    return _loader.load(name).generate(**nkw)


def get_code(name):
    _loader = XnoteLoader.get_instance()
    return _loader.load(name).code


def get_templates():
    """获取所有模板的浅拷贝"""
    loader = XnoteLoader.get_instance()
    return loader.templates.copy()


def _do_init():
    XnoteLoader.init_instance(TEMPLATE_DIR, namespace=NAMESPACE)

@xutils.log_init_deco("xtemplate.reload")
def reload():
    """reload template manager"""
    _do_init()


def init():
    _do_init()


class TextResponse:

    def __init__(self, text):
        self.text = text
        
class IterResponse:
    
    def __init__(self, iter):
        self.iter = iter


class PluginOptionLink:
    def __init__(self, text="", href=""):
        self.text = text
        self.href = href

class BasePlugin:
    """插件的基类"""

    api_level = 0.0  # 插件的API版本 用于处理各种兼容性问题

    # {布局信息}
    show_nav = True  # 是否展示导航 (顶层 or 左侧)
    show_aside = False # 是否展示侧边栏
    CONTENT_WIDTH = 1000  # 内容的宽度
    # {侧边栏自定义HTML}
    aside_html = ""
    header_html = ""
    # 展示在标题栏的右侧
    option_html = ""

    # 插件的标题
    show_title = True
    title = u"插件名称"
    description = ""

    # {分类的配置}
    # 插件分类 {note, dir, system, network}
    show_category = True
    category = ""
    parent_link = None # 上级功能链接

    # {权限配置}
    # 默认需要管理员权限访问
    require_admin = True
    # 是否需要登录,默认需要
    require_login = True
    # 允许访问的权限列表
    permitted_role_list = [] # type: list[str]

    # {搜索配置}
    show_search = True
    search_type = "default"
    search_action = "/search"
    search_placeholder = "综合搜索"

    # {插件路径} 系统自动填充
    fname = ""
    fpath = ""

    # {输入配置}
    placeholder = ""
    btn_text = T("处理")
    # 输入框的行数
    rows = 20
    # 是否展示编辑插件的按钮
    show_edit = True
    # deprecated 使用 show_edit
    editable = True 
        
    # {输出配置}
    # 分页配置
    show_pagenation = False
    page_url = "?page="
    page = 1  # 当前分页，需要扩展方设置
    page_max = 1  # 最大分页，需要扩展方设置

    # 插件模板路径
    base_template_path = "plugin/base/base_plugin.html"

    def __init__(self):
        # 提交请求的方法
        self.method = "POST"
        self.output = u("")
        self.html = u("")
        self.css_style = u("")
        self.option_links = [] # type: list[PluginOptionLink]

    def add_option_link(self, text="", href=""):
        self.option_links.append(PluginOptionLink(text, href))

    def write(self, text):
        self.output += u(text)

    def writeline(self, line):
        self.output += u(line + "\n")

    def writetext(self, text):
        self.output += u(text)

    def writeheader(self, html, **kw):
        self.header_html = render_text(html, **kw)

    def writebody(self, html, **kw):
        """写内容区"""
        self.writetemplate(html, **kw)

    def writehtml(self, html, **kw):
        """@deprecated 请使用 #writebody
        这个方法现在和 `writetemplate` 等价"""
        return self.writetemplate(html, **kw)

    def writetemplate(self, template_text, **kw):
        html = render_text(template_text, template_name=self.title, **kw)
        self.html += u(html.decode("utf-8"))
        return self.html

    def write_aside(self, template, **kw):
        self.show_aside = True
        self.aside_html = render_text(template, **kw)

    def ajax_response(self, template, **kw):
        warnings.warn("use response_ajax instead", DeprecationWarning)
        return self.do_render_text(template, **kw)

    def text_response(self, template, **kw):
        """返回纯文本格式的内容"""
        warnings.warn("use response_text instead", DeprecationWarning)
        return self.do_render_text(template, **kw)

    def response_ajax(self, template, **kw):
        return self.do_render_text(template, **kw)

    def response_text(self, template, **kw):
        """返回纯文本格式的内容"""
        return self.do_render_text(template, **kw)
    
    def response_iter(self, iter):
        """返回迭代器(生成器)"""
        return IterResponse(iter)

    def do_render_text(self, template, **kw):
        """这个方法用于渲染动态的HTML，用于局部刷新的场景"""
        html = render_text(template, **kw)
        return TextResponse(html)

    def handle(self, input = ""):
        """插件类需要实现这个方法"""
        raise NotImplementedError()
    
    def handle_sub_plugin(self, sub_plugin: "BasePlugin"):
        """处理子插件的逻辑"""
        result = sub_plugin.handle()
        self.html += sub_plugin.html
        return result
    
    def get_input(self):
        return xutils.get_argument_str("input", "")

    def get_format(self):
        """返回当前请求的数据格式"""
        return xutils.get_argument_str("_format", "")

    def get_page(self):
        """返回当前页码"""
        return xutils.get_argument_int("page", 1)

    def check_access(self):
        role = xauth.get_current_role()
        if role in self.permitted_role_list:
            return

        if self.require_admin:
            xauth.check_login("admin")
        elif self.require_login:
            xauth.check_login()
            
    def iter_output(self, output):
        yield from output

    def render(self):
        """图形界面入口,实际的调用入口请查看`plugins.py`文件"""

        # 访问权限检查
        self.check_access()

        input = self.get_input()
        error = u("")
        output = u("")
        try:
            self.page = self.get_page()
            self.category_name = xnote_hooks.get_category_name_by_code(
                self.category)
            output = self.handle(input) or u("")
            
            if self.get_format() == "text":
                web.header("Content-Type", "text/plain; charset:utf-8")
                return self.output + output

            # 直接返回文本
            if isinstance(output, TextResponse):
                return output.text
            
            # 返回迭代器
            if isinstance(output, IterResponse):
                return self.iter_output(output.iter)

            # 结构化对象交给框架处理
            if isinstance(output, (dict, list)):
                return output

        except web.webapi.Redirect:
            # 跳转的异常
            pass
        except:
            error = xutils.print_exc()
            web.ctx.status = "500 Internal Server Error"

        if not isinstance(output, str):
            web.ctx.status = "500 Internal Server Error"
            return f"expect output to be <str> but got {type(output)}"
        
        # 转换内部属性
        kw = self.convert_attr_to_kw()
        kw.error = error
        kw.input = input
        kw.script_name = globals().get("script_name")
        kw.output = self.output + output
        return render(self.base_template_path, **kw)
    
    
    def convert_attr_to_kw(self):
        kw = Storage()
        kw.model = self
        kw.fpath = self.fpath
        kw.description = self.description
        kw.html_title = self.title
        kw.title = self.title
        kw.method = self.method
        kw.rows = self.rows
        # 插件的主体部分html
        kw.html = self.html
        kw.css_style = self.css_style
        kw.show_nav = self.show_nav
        kw.show_aside = self.show_aside
        kw.show_right = self.show_right
        kw.show_search = self.show_search
        kw.search_action = self.search_action
        kw.search_placeholder = self.search_placeholder
        kw.search_type = self.search_type
        kw.CONTENT_WIDTH = self.CONTENT_WIDTH
        return kw

    def on_action(self, name, context, input):
        """处理各种按钮行为，包括 action/confirm/prompt 等按钮
        @param {string} name 按钮名称
        @param {object} context 上下文，渲染的时候放入的
        @param {string/boolean} input 输入信息
        """
        pass

    def on_command(self, context=None):
        """命令行入口"""
        pass

    def on_install(self, context=None):
        """安装插件事件, TODO"""
        pass

    def on_uninstall(self, context=None):
        """卸载插件事件, TODO"""
        pass

    def on_init(self, context=None):
        """系统初始化事件"""
        pass

    def on_event(self, event):
        """其他事件"""
        pass

    def GET(self):
        return self.render()

    def POST(self):
        return self.render()

    def get_aside_html(self):
        return self.aside_html
    
    def get_option_html(self):
        return self.option_html
    
    @property
    def show_right(self):
        return self.show_aside
    
    @show_right.setter
    def show_right(self, show_aside = False):
        self.show_aside = show_aside

    @property
    def required_role(self):
        """兼容历史字段"""
        if len(self.permitted_role_list) > 0:
            return self.permitted_role_list[0]
        return None

BaseTextPage = BasePlugin
BaseTextPlugin = BasePlugin


class BaseFormPlugin(BasePlugin):
    # html模板路径
    html_template_path = "plugin/base/base_form_plugin.html"

    def get_input_template(self):
        raise NotImplementedError()


class PluginBase(BasePlugin):
    """这种命名规则更好一些 [领域-组成部分]"""
    pass