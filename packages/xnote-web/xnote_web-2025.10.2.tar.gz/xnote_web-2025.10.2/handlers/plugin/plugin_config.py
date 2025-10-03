# encoding=utf-8
# @since 2024/11/02
import xutils
import typing

from xnote.core import xconfig, xtemplate
from xnote.plugin import PluginContext
from .models import PluginCategory


def inner_plugin(name: str, url:str, category="inner", url_query="", icon= "fa fa-cube"):
    context = PluginContext()
    context.name = name
    context.title = name
    context.url = url
    context.url_query = url_query
    context.editable = False
    context.category = category
    context.permitted_role_list = ["admin", "user"]
    context.require_admin = False
    context.icon = icon
    context.icon_class = icon
    context.build()
    return context


def note_plugin(name: str, url: str, icon="", required_role="user", url_query="", visible_in_list=True):
    context = PluginContext()
    context.name = name
    context.title = name
    context.url = url
    context.url_query = url_query
    context.icon = icon
    context.icon_class = "fa %s" % icon
    context.editable = False
    context.category = "note"
    context.require_admin = False
    context.required_role = required_role
    context.permitted_role_list = ["admin", "user"]
    context.is_external = False
    context.visible_in_list = visible_in_list
    context.build()
    return context


def index_plugin(name, url, url_query=""):
    return inner_plugin(name, url, "index", url_query=url_query)


def file_plugin(name, url, icon= "fa fa-cube"):
    return inner_plugin(name, url, "dir", icon=icon)


def dev_plugin(name: str, url: str, visible_in_list = True):
    result = inner_plugin(name, url, "develop")
    result.visible_in_list = visible_in_list
    return result


def system_plugin(name: str, url: str):
    return inner_plugin(name, url, "system")

def admin_plugin(name: str, url: str, visible_in_list = True):
    result = inner_plugin(name, url, "admin")
    result.visible_in_list = visible_in_list
    return result

def load_inner_tools():
    pass


# 内部工具,如果已经在产品列表页展示,应该配置成在插件列表不可见,但是可以被搜索到
INNER_TOOLS = [
    # 开发工具
    dev_plugin("浏览器信息", "/tools/browser_info"),
    dev_plugin("系统模块", "/system/module_list"),
    dev_plugin("前端组件", "/test/example"),
    dev_plugin("性能分析", "/system/handler_profile"),

    # 文本
    dev_plugin("文本工具", "/tools/text_convert?tab=convert&nav=true"),
    dev_plugin("文本转换", "/tools/text_convert?tab=convert", visible_in_list=False),
    dev_plugin("文本对比", "/tools/text_diff?tab=diff", visible_in_list=False),
    dev_plugin("随机文本", "/tools/text_random?tab=random", visible_in_list=False),

    # 图片
    dev_plugin("图片工具", "/tools/img_merge?tab=merge&nav=true"),
    dev_plugin("图片合并", "/tools/img_merge?tab=merge", visible_in_list=False),
    dev_plugin("图片拆分", "/tools/img_split?tab=split", visible_in_list=False),
    dev_plugin("图像灰度化", "/tools/img_gray?tab=gray", visible_in_list=False),

    # 编解码
    dev_plugin("编解码工具", "/tools/encode?tab=BASE64&nav=true"),
    dev_plugin("base64", "/tools/encode?tab=BASE64", visible_in_list=False),
    dev_plugin("HEX转换", "/tools/hex", visible_in_list=False),
    dev_plugin("md5签名", "/tools/md5", visible_in_list=False),
    dev_plugin("sha1签名", "/tools/sha1", visible_in_list=False),
    dev_plugin("URL编解码", "/tools/urlcoder", visible_in_list=False),
    dev_plugin("条形码", "/tools/barcode", visible_in_list=False),
    dev_plugin("二维码", "/tools/qrcode", visible_in_list=False),
    dev_plugin("插件目录v2", "/plugin_list_v2"),
    dev_plugin("Menu_Modules", "/system/modules_info"),

    # 其他工具
    inner_plugin("分屏模式", "/tools/multi_win"),
    inner_plugin("RunJS", "/tools/runjs"),
    inner_plugin("摄像头", "/tools/camera"),

    # 笔记工具
    note_plugin("新建笔记", "/note/create", "fa-plus-square", visible_in_list=False),
    note_plugin("我的置顶", "/note/sticky", "fa-thumb-tack", visible_in_list=False),
    note_plugin("搜索历史", "/search/history", "fa-search", visible_in_list=False),
    note_plugin("导入笔记", "/note/html_importer",
                "fa-internet-explorer", required_role="admin"),
    note_plugin("时间视图", "/note/date", "fa-clock-o",
                url_query="?show_back=true"),
    note_plugin("数据统计", "/note/stat", "fa-bar-chart", visible_in_list=False),
    note_plugin("上传管理", "/fs_upload", "fa-upload", visible_in_list=False),
    note_plugin("我的文件", "/fs_upload?source=file", "fa-upload", visible_in_list=False),
    note_plugin("笔记批量管理", "/note/management", "fa-gear"),
    note_plugin("回收站", "/note/removed", "fa-trash", visible_in_list=False),
    note_plugin("笔记本", "/note/group", "fa-th-large", visible_in_list=False),
    note_plugin("待办任务", "/message/task", "fa-calendar-check-o", visible_in_list=False),
    note_plugin("随手记", "/message?tag=log", "fa-file-text-o", visible_in_list=False),
    note_plugin("我的相册", "/note/gallery", "fa-photo", visible_in_list=False),
    note_plugin("我的清单", "/note/list", "fa-list", visible_in_list=False),
    note_plugin("我的评论", "/note/comment/mine", "fa-comments", visible_in_list=False),
    note_plugin("标签列表", "/note/taglist", "fa-tags", visible_in_list=False),
    note_plugin("常用笔记", "/note/recent?orderby=hot", "fa-file-text-o", visible_in_list=False),
    note_plugin("词典", "/note/dict", "icon-dict", visible_in_list=False),
    note_plugin("时光轴", "/note/timeline", "fa-clock-o"),
    note_plugin("笔记日历", "/note/group/year", "fa-file-text-o"),

    # 文件工具
    file_plugin("文件索引", "/fs_index"),
    file_plugin("我的收藏夹", "/fs_bookmark", icon="fa fa-folder"),

    # 管理后台
    admin_plugin("系统注册表", "/system/event", visible_in_list=False),
    admin_plugin("集群管理", "/system/sync", visible_in_list=False),
    admin_plugin("系统日志", "/system/log", visible_in_list=False),
    admin_plugin("缓存管理", "/system/cache", visible_in_list=False),
    admin_plugin("数据修复", "/admin/repair"),
    # 系统工具
    # system_plugin("系统日志", "/system/log"),
]

class CategoryService:

    category_list: typing.List[PluginCategory] = []

    @classmethod
    def define_plugin_category(cls, code: str,
                            name: str,
                            url=None,
                            raise_duplication=True,
                            required_roles=None,
                            platforms=None,
                            icon_class=None,
                            css_class=""):
        for item in cls.category_list:
            if item.code == code:
                if raise_duplication:
                    raise Exception("code: %s is defined" % code)
                else:
                    return
            if item.name == name:
                if raise_duplication:
                    raise Exception("name: %s is defined" % name)
                else:
                    return
        category = PluginCategory(code, name, url, required_roles)
        category.platforms = platforms
        category.css_class = css_class
        if icon_class != None:
            category.icon_class = icon_class
        cls.category_list.append(category)

    @classmethod
    def init_category_list(cls):    
        cls.define_plugin_category("all",      u"常用", icon_class="fa fa-th-large")
        cls.define_plugin_category("recent",   u"最近")
        cls.define_plugin_category("note",   u"笔记")
        cls.define_plugin_category("dir",      u"文件", required_roles=["admin"], icon_class="fa fa-folder")
        cls.define_plugin_category("system",   u"系统", required_roles=["admin"], icon_class="fa fa-gear")
        cls.define_plugin_category("network",  u"网络", required_roles=["admin"], icon_class="icon-network-14px")
        cls.define_plugin_category("develop",  u"开发", required_roles=["admin", "user"])
        cls.define_plugin_category("datetime", u"时间", icon_class="fa fa-clock-o")
        cls.define_plugin_category("work",     u"工作", icon_class="icon-work")
        cls.define_plugin_category("inner",    u"内置工具", platforms=[])
        cls.define_plugin_category("money",    u"理财")
        cls.define_plugin_category("test",     u"测试", platforms=[])
        cls.define_plugin_category("admin", "管理员", css_class="hide")
        cls.define_plugin_category("other", "其他", css_class="hide")

        cls.define_plugin_category(
            code="index",
            name="全部分类", 
            url="/plugin_category_list?category=index", 
            icon_class="fa fa-th-large")

CategoryService.init_category_list()
