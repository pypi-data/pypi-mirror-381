# encoding=utf-8
from xutils import Storage
from xutils.base import BaseEnum, EnumItem

class EventTypeEnum(BaseEnum):
    sys_reload = EnumItem("系统重新加载", "sys.reload")
    sys_init = EnumItem("系统初始化", "sys.init")

class FileUploadEvent(Storage):
    """文件上传事件"""

    def __init__(self):
        super().__init__()
        self.user_name = ""
        self.user_id = 0
        self.fpath = ""
        self.remark = ""

class FileDeleteEvent(FileUploadEvent):
    """文件删除事件"""
    pass

class FileRenameEvent(Storage):
    """文件重命名事件"""
    def __init__(self):
        super().__init__()
        self.user_name = ""
        self.user_id = 0
        self.fpath = ""
        self.old_fpath = ""

class NoteViewEvent(Storage):
    """笔记访问事件"""
    def __init__(self, id=0, user_name="", user_id=0):
        super().__init__()
        self.id = id
        self.user_name = user_name
        self.user_id = user_id


class MessageEvent(Storage):
    """待办/随手记变更事件"""
    def __init__(self, msg_key="", user_id=0, tag="", content=""):
        super().__init__()
        self.msg_key = msg_key
        self.tag = tag
        self.user_id = user_id
        self.content = content

class MessageUpdateEvent(Storage):

    def __init__(self):
        self.msg_id = 0
        self.msg_key = ""
        self.user_id = 0
        self.content = ""


class UserUpdateEvent(Storage):
    def __init__(self):
        self.user_id = 0
        self.user_name = ""