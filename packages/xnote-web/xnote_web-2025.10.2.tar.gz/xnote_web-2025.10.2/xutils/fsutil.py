# -*- coding:utf-8 -*-
# @author xupingmao <578749341@qq.com>
# @since 2020/03/21 18:04:32
# @modified 2022/04/23 00:06:59
"""fsutil: 文件操作工具，文件工具分为如下部分：
1、path处理，比如判断是否是父级目录
2、文件操作，比如读写文件，创建目录
"""

import os
import platform
import xutils
import base64
import time
import hashlib
import typing

import logging
# 部分系统没有ctypes（比如SAE的云引擎）
try:
    import ctypes
except ImportError:
    ctypes = None

from io import BufferedReader
from xutils import six
from xutils.imports import *
from xutils.base import Storage
from xutils import textutil
from fnmatch import fnmatch
from configparser import ConfigParser

# mbcs泛指通过2字节来编码的字符编码
# https://zhuanlan.zhihu.com/p/453675608
# GBK兼容GB2312
# GB18030兼容GB2312 基本兼容GBK
# 支持的编码参考 encodings 包
ENCODING_TUPLE = ("utf-8", "gbk", "gb18030", "mbcs", "latin_1")

# 配置文件最大大小
CONFIG_FILE_MAX_SIZE = 1024 * 1024

# Windows的文件名最大长度
WIN_MAXPATH = 260


class FileUtilConfig:
    """文件util配置"""
    encode_name = False
    data_dir = ""
    tmp_dir = "/tmp"
    trash_dir = ""
    encode_name_ext = (".x0", ".xenc")

    @classmethod
    def get_trash_dir(cls):
        assert cls.trash_dir != ""
        return cls.trash_dir

def get_real_path(path):
    """获取真实的path信息，如果配置了urlencode，强制进行urlencode，否则先按原路径检查，如果文件不存在，再进行urlencode
    之所以要这样做，主要是为了兼容从不支持unicode文件名的服务器同步到本地的文件"""
    assert isinstance(path, str)
    if path == "":
        return path

    if FileUtilConfig.encode_name:
        return get_real_path_encode_first(path)

    # 如果文件存在,直接返回
    if os.path.exists(path):
        return path

    # 兼容urlencode编码
    quoted = quote_unicode(path)
    if os.path.exists(quoted):
        return quoted

    # 如果quote不行还是返回原来的输入
    return path


def get_real_path_encode_first(path):
    """获取真实路径，优先使用encode版本的path"""
    quoted = quote_unicode(path)
    if os.path.exists(quoted):
        return quoted

    return path


def is_parent_dir(parent: str, child: str):
    """判断是否是父级目录 arg0.is_parent_dir_of(arg1)
    @param {string} parent 父级路径
    @param {string} child 子路径

    >>> is_parent_dir('/test/', '/test/child.txt')
    True
    >>> is_parent_dir('/test', '/test/child.txt')
    True
    >>> is_parent_dir('/test', '/test_1/child.txt')
    False
    >>> is_parent_dir('/test', '/a/test/child.txt')
    False
    """
    child_path = os.path.abspath(child)
    parent_path = os.path.abspath(parent)

    if parent_path[-1] != os.path.sep:
        parent_path += os.path.sep
    return child_path.startswith(parent_path)


def get_relative_path(path:str, parent:str):
    """获取文件相对parent的路径
    @param {str} path 当前文件路径
    @param {str} parent 父级文件路径
    @return {str} 相对路径
    
    >>> get_relative_path('/users/xxx/test/hello.html', '/users/xxx')
    'test/hello.html'
    >>> get_relative_path('/tmp/test.html', '/tmp/test.html')
    ''
    """
    path1 = os.path.abspath(path)
    parent1 = os.path.abspath(parent)
    # abpath之后最后没有/
    # 比如
    # ./                 -> /users/xxx
    # ./test/hello.html  -> /users/xxx/test/hello.html
    # 相减的结果是         -> /test/hello.html
    # 需要除去第一个/
    relative_path = path1[len(parent1):]
    relative_path = relative_path.replace("\\", "/")
    if relative_path.startswith("/"):
        relative_path = relative_path[1:]
    return relative_path


def detect_encoding(fpath: str):
    last_err = None
    for encoding in ENCODING_TUPLE:
        try:
            with open(fpath, encoding=encoding) as fp:
                # 探测100K数据
                for i in range(100):
                    fp.read(1024)
                return encoding
        except Exception as e:
            last_err = e
    if last_err:
        raise Exception("can not detect file encoding, path=[%s]" % fpath,
                        last_err)
    return None


def get_file_ext(fname):
    """获取文件扩展名,不带dot符号"""
    realname = decode_name(fname)
    name, ext = os.path.splitext(realname)
    ext = ext.strip(".")
    if len(ext) > 5:
        # 太长的扩展名视作无效
        return ""
    return ext.lower()

def format_size(size: typing.Union[int, float]):
    """格式化大小

    >>> format_size(10240)
    '10.00K'
    >>> format_size(1429365116108)
    '1.3T'
    >>> format_size(1429365116108000)
    '1.3P'
    >>> format_size(-10240)
    '-10.00K'
    """
    if size < 0:
        return "-" + format_size(-size)
    if size < 1024:
        return '%sB' % size
    elif size < 1024**2:
        return '%.2fK' % (float(size) / 1024)
    elif size < 1024**3:
        return '%.2fM' % (float(size) / 1024**2)
    elif size < 1024**4:
        return '%.2fG' % (float(size) / 1024**3)
    elif size < 1024**5:
        return '%.2fT' % (float(size) / 1024**4)
    else:
        return "%.2fP" % (float(size) / 1024**5)

def format_file_size(fpath):
    """获取文件大小,返回文本格式"""
    return get_file_size(fpath, format=True)


def get_file_size_int(fpath: str, raise_exception=False):
    """读取文件大小,返回数字"""
    try:
        st = os.stat(fpath)
        if st and st.st_size >= 0:
            return st.st_size
    except OSError as e:
        if raise_exception:
            raise e
        return -1
    return 0

def get_file_size(fpath, format=False):
    size = get_file_size_int(fpath)
    if size < 0 and format:
        return "-"
    if format:
        return format_size(size)
    return size

def list_file_objects(dirname, webpath=False):
    from xnote.core import xconfig
    filelist = [
        FileItem(os.path.join(dirname, child)) for child in os.listdir(dirname)
    ]
    if webpath:
        for item in filelist:
            item.path = get_relative_path(item.path, xconfig.UPLOAD_DIR)
    filelist.sort()
    return filelist


def list_files(dirname, webpath=False):
    return list_file_objects(dirname, webpath)


def split_path_to_objects(path):
    """拆分文件路径
    @param {string} path 文件路径
    """
    path = os.path.abspath(path)
    path = path.replace("\\", "/")
    pathes = path.split("/")

    if path[0] == "/":
        last = ""
    else:
        last = None
    file_objects = []
    for path in pathes:
        if path == "":
            continue
        if last is not None:
            path = last + "/" + path
        file_objects.append(FileItem(path, merge=False))
        last = path

    return file_objects


def splitpath(path):
    return split_path_to_objects(path)


def decode_name(name: str):
    """将文件名解码成可读的名称"""
    dirname = os.path.dirname(name)
    basename = os.path.basename(name)
    namepart, ext = os.path.splitext(basename)
    if ext in FileUtilConfig.encode_name_ext:
        try:
            pad_size = 4 - len(namepart)%4
            namepart += '=' * pad_size
            basename = base64.urlsafe_b64decode(
                namepart.encode("utf-8")).decode("utf-8")
            return os.path.join(dirname, basename)
        except:
            pass
    return xutils.unquote(name)


def encode_name(name: str):
    """对文件名进行编码,以避免文件系统的编码问题"""
    namepart, ext = os.path.splitext(name)
    if ext in FileUtilConfig.encode_name_ext:
        return name
    result = base64.urlsafe_b64encode(name.encode("utf-8")).decode("utf-8")
    result = result.strip("=")
    return result + ".x0"


def path_equals(source, target):
    """判断两个路径是否相同

    >>> path_equals('/home/a.txt', '/home/ccc/../a.txt')
    True

    """
    return os.path.abspath(source) == os.path.abspath(target)


def get_tmp_path(fname="", prefix="", ext=""):
    """生成临时文件路径
    TODO 多线程情况下加锁
    """
    if ext != "":
        if ext[0] != ".":
            raise Exception("expect ext like .xx")

    if fname != "" and fname != None:
        return os.path.join(FileUtilConfig.tmp_dir, fname)

    retry_times = 10
    name = prefix + time.strftime("%Y_%m_%d_") + textutil.create_uuid()
    base_path = os.path.join(FileUtilConfig.tmp_dir, name)
    path = base_path + ext

    for i in range(1, retry_times + 1):
        if not os.path.exists(path):
            return path
        path = "%s_%s" % (base_path, i) + ext
    raise Exception("创建临时文件失败, 请手动重试")

tmp_path = get_tmp_path

def data_path(fname):
    """获取data目录文件路径"""
    return os.path.join(FileUtilConfig.data_dir, fname)


### 文件操作部分
from xutils.base import makedirs

def _try_readfile(path, mode="r", limit=-1, encoding='utf-8') -> str:
    with open(path, mode=mode, encoding=encoding) as fp:
        if limit > 0:
            content = fp.read(limit)
        else:
            content = fp.read()
        return content


def readfile(path: str, mode="r", limit=-1):
    """读取文件，尝试多种编码，编码别名参考标准库`Lib/encodings/aliases.py`
    * utf-8 是一种边长编码，兼容ASCII
    * GBK 是一种双字节编码，全称《汉字内码扩展规范》，兼容GB2312
    * latin_1 是iso-8859-1的别名，单字节编码，兼容ASCII
    """
    last_err = None
    for encoding in ENCODING_TUPLE:
        try:
            return _try_readfile(path, mode, limit, encoding)
        except Exception as e:
            last_err = e
    
    raise Exception("can not read file %s" % path, last_err)


def _try_readlines(fpath: str, limit=-1, encoding='utf-8'):
    with open(fpath, encoding=encoding) as fp:
        if limit <= 0:
            return fp.readlines()
        else:
            lines = []
            for n in range(limit):
                lines.append(fp.readline())
            return lines


def readlines(fpath: str, limit=-1):
    last_err = None
    for encoding in ENCODING_TUPLE:
        try:
            return _try_readlines(fpath, limit, encoding)
        except Exception as e:
            last_err = e

    raise Exception("readlines failed", last_err)


# readfile别名
read = readfile
read_utf8 = readfile


def writefile(path: str, content: typing.Union[str, bytes], mode="wb"):
    import codecs
    dirname = os.path.dirname(path)
    makedirs(dirname)

    with open(path, mode=mode) as fp:
        if isinstance(content, str):
            buf = codecs.encode(content, "utf-8")
        else:
            buf = content
        fp.write(buf)
    return content


savetofile = writefile
savefile = writefile
writebytes = writefile


def writeline(path, content, mode="wb"):
    writefile(path, content + "\n", mode)


def readbytes(path):
    with open(path, "rb") as fp:
        bytes = fp.read()
    return bytes

class MoveFileHandler:

    @classmethod
    def move(cls, from_path, to_path, rename_on_conflict=False):
        if not os.path.exists(from_path):
            return
        to_dirname = os.path.dirname(to_path)
        makedirs(to_dirname)

        if os.path.exists(to_path):
            if rename_on_conflict:
                to_path = cls.find_target_path(to_path)
        os.rename(from_path, to_path)
    
    @classmethod
    def find_target_path(cls, to_path):
        name, ext = os.path.splitext(to_path)
        for suffix in range(10):
            tempfile = name + "-" + str(suffix+1)
            if not os.path.exists(tempfile):
                return tempfile
        raise Exception("target path not found")


mvfile = MoveFileHandler.move


def rename_file(srcname, dstname):
    return mvfile(srcname, dstname)


def rmdir(path, hard=False):
    """删除文件夹
    @param {str} path 文件路径
    @param {bool} hard 是否是物理删除
    """
    trash_dir = FileUtilConfig.get_trash_dir()

    if hard:
        shutil.rmtree(path)
        return
    path = path.rstrip("/")
    basename = os.path.basename(path)
    target = os.path.join(trash_dir, basename)
    target = os.path.abspath(target)
    path = os.path.abspath(path)

    if is_parent_dir(trash_dir, path):
        # 已经在回收站，直接删除文件夹
        shutil.rmtree(path)
        return
    else:
        suffix = 0
        while True:
            suffix += 1
            if os.path.exists(target):
                tmp_name = "%s@%s" % (basename, suffix)
                target = os.path.join(trash_dir, tmp_name)
            else:
                shutil.move(path, target)
                break
        return target


def remove_file(path, hard=False):
    # type: (str, bool) -> bool
    """删除文件，默认软删除，移动到trash目录中
    - 如果已经在trash目录或者硬删除, 从磁盘中抹除
    - 如果文件不存在, 不报错
    @param {str} path
    @param {bool} hard=False 是否硬删除
    @return {str} path in trash.
    """

    if not os.path.exists(path):
        # 尝试转换一下path
        path = get_real_path(path)
        if not os.path.exists(path):
            return False
    if os.path.isfile(path):
        if hard:
            os.remove(path)
            return True
        if os.path.islink(path):
            # 软链接直接删除
            os.remove(path)
            return True

        trash_dir = FileUtilConfig.get_trash_dir()
        dirname = os.path.dirname(path)
        dirname = os.path.abspath(dirname)
        dustbin = os.path.abspath(trash_dir)
        if is_parent_dir(trash_dir, path):
            os.remove(path)
        else:
            fname = os.path.basename(path)
            name, ext = os.path.splitext(fname)
            suffix = 0
            dirname = os.path.join(dustbin, time.strftime("%Y%m%d"))
            makedirs(dirname)

            while True:
                suffix += 1
                destpath = os.path.join(dustbin, dirname,
                                        "%s@%s%s" % (name, suffix, ext))
                if not os.path.exists(destpath):
                    break
            # os.rename(path, destpath)
            # shutil.move 可以跨磁盘分区移动文件
            shutil.move(path, destpath)
        # os.remove(path)
    elif os.path.isdir(path):
        rmdir(path, hard)
    return True


rmfile = remove_file
remove = rmfile


def copy(src, dest):
    bufsize = 64 * 1024  # 64k
    srcfp = open(src, "rb")
    destfp = open(dest, "wb")

    try:
        while True:
            buf = srcfp.read(bufsize)
            if not buf:
                break
            destfp.write(buf)
    except Exception as e:
        logging.error("copy file from %s to %s failed, %s", src, dest, e)
    finally:
        srcfp.close()
        destfp.close()


def open_directory(dirname):
    if os.name == "nt":
        os.popen("explorer %s" % dirname)
    elif platform.system() == "Darwin":
        os.popen("open %s" % dirname)


def try_listdir(dirname):
    try:
        return os.listdir(dirname)
    except:
        return []


def fixed_dir_path(dirname):
    if not dirname.endswith("/"):
        return dirname + "/"
    return dirname


def normalize_path(fpath):
    """标准化文件路径"""
    fpath = os.path.abspath(fpath)
    if os.path.isdir(fpath):
        return fixed_dir_path(fpath)
    return fpath


def fixed_basename(path):
    if path.endswith("/"):
        path = path[:-1]
    return os.path.basename(path)


class FileStatInfo(Storage):
    def __init__(self):
        super().__init__()
        self.st_size = 0

class FileItem(Storage):
    """文件对象"""

    def __init__(self,
                 path: str,
                 parent:typing.Optional[str] = None,
                 merge=False,
                 encode_path=True,
                 name:typing.Optional[str]=None):
        self.path = path
        self.path_b64 = textutil.encode_base64(path)
        realname = fixed_basename(path)
        self.name = realname
        self.realname = realname

        self.size = '-'
        self.cdate = '-'
        self.icon = "fa-file-o"
        _, self.ext = os.path.splitext(path)
        self.ext = self.ext.lower()

        if parent != None:
            self.name = get_relative_path(path, parent)

        # 处理Windows盘符
        if path.endswith(":"):
            self.name = path
            # 必须带`/`, 否则的话`C:`会等同于当前目录
            self.path = path + "/"

        if encode_path:
            self.encoded_path = xutils.encode_uri_component(self.path)

        # 处理文件属性
        self.handle_file_stat(merge, parent)

        if name != None:
            self.name = name

    def handle_file_stat(self, merge, parent):
        path = self.path
        try:
            st = os.stat(path)
            self.cdate = xutils.format_date(st.st_ctime)
        except:
            st = FileStatInfo()

        self.name = xutils.unquote(self.name)
        self.name = decode_name(self.name)
        if os.path.isfile(path):
            self.type = "file"
            _, self.ext = os.path.splitext(self.name)
            self.size = format_size(st.st_size)
        else:
            children = try_listdir(path)
            self.type = "dir"
            self.path = fixed_dir_path(self.path)

            if children != None:
                self.size = len(children)
            else:
                self.size = "ERR"

            if merge and self.size == 1:
                new_path = os.path.join(path, children[0])
                if not os.path.isdir(new_path):
                    return
                if parent is None:
                    parent = os.path.dirname(path)
                self.__init__(new_path, parent)

    # sort方法重写__lt__即可
    def __lt__(self, other: "FileItem"):
        if self.type == "dir" and other.type == "file":
            return True
        if self.type == "file" and other.type == "dir":
            return False
        return self.name < other.name

def touch(path):
    """类似于Linux的touch命令"""
    if not os.path.exists(path):
        with open(path, "wb") as fp:
            pass
    else:
        current = time.mktime(time.gmtime())
        times = (current, current)
        os.utime(path, times)


def _search_path0(path, key, limit=200, option=""):
    result_dirs = []
    result_files = []
    key = key.lower()
    count = 0
    for root, dirs, files in os.walk(path):
        root_len = len(root)
        if option != "file":
            for f in dirs:
                abspath = os.path.join(root, f)
                if fnmatch(f.lower(), key):
                    result_dirs.append(abspath)
                    count += 1
                    if count >= limit:
                        break
        for f in files:
            abspath = os.path.join(root, f)
            if fnmatch(f.lower(), key):
                result_files.append(abspath)
                count += 1
                if count >= limit:
                    break
        if count >= limit:
            break
    return result_dirs + result_files


def search_path(path, key, option=""):
    """搜索文件系统，key支持通配符表示，具体见fnmatch模块
    @param {string} path 
    @param {string} key
    @param {string} option 附加选项
        - file 仅搜索文件
        - dir 仅搜索目录
    """
    result = []
    quoted_key = quote_unicode(key)
    if key != quoted_key:
        result = _search_path0(path, quoted_key, 200, option)
    return result + _search_path0(path, key, 200, option)


def get_display_name(fpath, parent):
    """获取文件的显示名称"""
    path = get_relative_path(fpath, parent)
    return xutils.unquote(path)


def do_list_dir_abs_recursive(dirname):
    pathlist = []
    for root, dirs, files in os.walk(dirname):
        for fname in files:
            fpath = os.path.join(root, fname)
            pathlist.append(fpath)
    pathlist = sorted(pathlist)
    return pathlist


def listdir_abs(dirname, recursive=True):
    if recursive:
        return do_list_dir_abs_recursive(dirname)
    else:
        pathlist = []
        for fname in os.listdir(dirname):
            fpath = os.path.join(dirname, fname)
            pathlist.append(fpath)
        pathlist.sort()
        return pathlist


def _parse_line(line):
    if line == None:
        return None
    line = line.strip()
    if line == "":
        return None
    if line[0] == "#":
        return None
    return line


def load_list_config(fpath):
    """加载列表配置文件"""
    text = readfile(fpath)
    lines = text.split("\n")
    result = []
    for line in lines:
        line = _parse_line(line)
        if line != None:
            result.append(line)
    return result


def load_set_config(fpath):
    """加载集合配置文件"""
    text = readfile(fpath)
    lines = text.split("\n")
    result = set()
    for line in lines:
        line = _parse_line(line)
        if line != None:
            result.add(line)
    return result


def load_prop_config(fpath):
    # type: (str) -> dict[str, str]
    text = readfile(fpath)
    from xutils.text_parser_properties import parse_prop_text_to_dict
    return parse_prop_text_to_dict(text)


def load_json_config(fpath):
    text = readfile(fpath)
    assert text != None
    return json.loads(text)

def load_json_dict(fpath: str):
    from xutils.functions import TypedDict
    obj = load_json_config(fpath)
    return TypedDict(obj)


class IniConfigData:

    def __init__(self):
        self.sections = []
        self.items = Storage()


def load_ini_config(fpath):
    """加载ini文件，转换为Storage对象"""
    parser = ConfigParser()

    if six.PY2:
        parser.read(fpath)
    else:
        text = readfile(fpath, limit=CONFIG_FILE_MAX_SIZE)
        parser.read_string(text)

    result = IniConfigData()
    result.sections = parser.sections()

    for section in parser.sections():
        item = Storage()
        for key, value in parser.items(section):
            setattr(item, key, value)
        setattr(result.items, section, item)
    return result

def get_safe_webpath(fpath: str):
    if not is_parent_dir(FileUtilConfig.data_dir, fpath):
        raise Exception(f"unsafe fpath: {fpath}")
    rpath = get_relative_path(fpath, FileUtilConfig.data_dir)
    return "/data/" + rpath

def get_webpath(fpath: str):
    """TODO 这个方法不安全, 待重构"""
    if is_parent_dir(FileUtilConfig.data_dir, fpath):
        rpath = get_relative_path(fpath, FileUtilConfig.data_dir)
        return "/data/" + rpath
    return "/fs/~" + fpath

def backupfile(path, backup_dir=None, rename=False):
    if os.path.exists(path):
        if backup_dir is None:
            backup_dir = os.path.dirname(path)
        name = os.path.basename(path)
        newname = name + ".bak"
        newpath = os.path.join(backup_dir, newname)
        # need to handle case that bakup file exists
        import shutil
        shutil.copyfile(path, newpath)


def get_free_space(folder: str):
    """返回文件夹的可用空间
    参考来源: https://www.jb51.net/article/115604.htm

    Python3.3 shutil模块新增了 disk_usage 方法，可以直接使用
    """
    if platform.system() == 'Windows':
        assert ctypes != None
        free_bytes = ctypes.c_ulonglong(0)
        c_folder = ctypes.c_wchar_p(folder)
        ctypes.windll.kernel32.GetDiskFreeSpaceExW(c_folder, None, None,
                                                   ctypes.pointer(free_bytes))
        return free_bytes.value
    else:
        # linux/Unix
        st = os.statvfs(folder)
        return st.f_bavail * st.f_frsize

def is_same_file(path1, path2):
    return os.path.abspath(path1) == os.path.abspath(path2)


def get_safe_file_name(filename: str):
    """处理文件名中的特殊符号"""
    for c in " @$:#\\|=&?":
        filename = filename.replace(c, "_")
    
    quote_name = xutils.quote_unicode(filename)
    if quote_name != filename:
        return encode_name(filename)
    return filename

def do_check_file_type(filename, target_set):
    """根据文件后缀判断是否是图片"""
    realname = decode_name(filename)
    name, ext = os.path.splitext(realname)
    return ext.lower() in target_set

def is_img_file(filename):
    """根据文件后缀判断是否是图片"""
    return do_check_file_type(filename, xutils.FS_IMG_EXT_LIST)

def is_text_file(filename):
    """根据文件后缀判断是否是文本文件"""
    return do_check_file_type(filename, xutils.FS_TEXT_EXT_LIST)

def is_audio_file(filename):
    return do_check_file_type(filename, xutils.FS_AUDIO_EXT_LIST)

def is_code_file(filename):
    return do_check_file_type(filename, xutils.FS_CODE_EXT_LIST)

def get_text_ext():
    return xutils.FS_TEXT_EXT_LIST

def is_editable(fpath):
    return is_text_file(fpath) or is_code_file(fpath)


class FileHasher:

    def __init__(self, fpath, hash_type="md5"):
        self.fpath = fpath
        self.hash_type = hash_type
        self.chunksize = 8192 # 8K

    def get_hash_algo(self):
        hash_type = self.hash_type
        if hash_type == "md5":
            return hashlib.md5()
        if hash_type == "sha1":
            return hashlib.sha1()
        if hash_type == "sha256":
            return hashlib.sha256()
        if hash_type == "sha512":
            return hashlib.sha512()
        raise Exception(f"unsupported hash_type:{hash_type}")
    
    def get_hash_hex(self):
        fpath = self.fpath
        chunk_size = self.chunksize
        if not os.path.exists(fpath):
            return ""
        if os.path.isdir(fpath):
            return ""
        def read_chunks(fh: BufferedReader):
            fh.seek(0)
            chunk = fh.read(chunk_size)
            while chunk:
                yield chunk
                chunk = fh.read(chunk_size)
            else: #最后要将游标放回文件开头
                fh.seek(0)
        
        m = self.get_hash_algo()
        with open(fpath, "rb") as fh:
            for chunk in read_chunks(fh):
                m.update(chunk)
        return m.hexdigest()

def get_md5_sum(fpath):
    """计算文件的MD5校验码, MD5早已经被证明不安全, 但是由于计算速度快, 一些场景还是保留用于快速校验"""
    hasher = FileHasher(fpath=fpath, hash_type="md5")
    return hasher.get_hash_hex()

def get_sha1_sum(fpath: str):
    """计算文件的SHA1校验码, 注意: SHA1算法已经被证明不安全"""
    hasher = FileHasher(fpath=fpath, hash_type="sha1")
    return hasher.get_hash_hex()

def get_sha256_sum(fpath: str):
    """计算文件的SHA-256校验码"""
    hasher = FileHasher(fpath=fpath, hash_type="sha256")
    return hasher.get_hash_hex()