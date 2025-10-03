# encoding=utf-8
# created by xupingmao on 2017/04/22
from __future__ import print_function
import logging
import os
import time
import xutils
from xnote.core import xtemplate
from xnote.core import xauth
from xnote.core import xmanager
from xnote.core import xconfig
from xnote.core import xnote_event
from io import StringIO
try:
    from bs4 import BeautifulSoup
except ImportError:
    BeautifulSoup = None
from html2text import HTML2Text
from xutils import netutil
from xutils import Storage
from xutils import dbutil
from xutils import fsutil
from xutils import textutil
from xutils import webutil
from xutils import BaseDataRecord
from xutils.text_parser import TextParserBase
from . import dao
from . import dao_edit
from .dao_api import NoteDao
from handlers.note.models import NoteDO
from handlers.note import dao_edit
from handlers.config import LinkConfig

class FsMapRecord(BaseDataRecord):
    url = ""
    webpath = ""
    content_type = ""
    version = 0

class FsMapDao:
    fs_map_db = dbutil.get_hash_table("fs_map")

    @classmethod
    def get_by_url(cls, url: str):
        hash_key = textutil.sha256_hex(url)
        record = cls.fs_map_db.get(hash_key)
        if record != None:
            return FsMapRecord.from_dict_or_None(record)

        record = cls.fs_map_db.get(url)
        result = FsMapRecord.from_dict_or_None(record)
        if result:
            result.url = url
        return result
    
    @classmethod
    def save(cls, record: FsMapRecord):
        assert record.url != ""
        assert record.webpath != ""
        assert record.version > 0
        key = textutil.sha256_hex(record.url)
        cls.fs_map_db.put(key, record)


def get_addr(src, host):
    if src is None:
        return None
    if src.startswith("//"):
        return "http:" + src
    return src


def readhttp(url: str):
    url = xutils.quote_unicode(url)
    return netutil.http_get(url)


def get_addr_list(images, host=None):
    dest = set()
    for image in images:
        src = image.attrs.get("src")
        src = get_addr(src, host)
        if src is not None:
            dest.add(src)
    return list(dest)


def get_text_list(elements):
    dest = set()
    for ele in elements:
        text = ele.get_text()
        if text is not None and len(text) > 0:
            dest.add(text)
    return list(dest)


def get_res_name(url):
    slash_pos = url.rfind("/")
    return url[slash_pos+1:]


def download_res_list(reslist, dirname):
    dirname = os.path.join("./tmp", dirname)
    xutils.makedirs(dirname)

    for res in reslist:
        print("Download", res)
        res = xutils.quote_unicode(res)
        bytes = xutils.urlopen(res).read()
        name = get_res_name(res)
        path = os.path.join(dirname, name)
        with open(path, "wb") as fp:
            fp.write(bytes)


def isempty(str):
    return str == None or len(str) == 0


def bs_get_text(result, element, blacklist=None):
    if blacklist is None:
        blacklist = []
    if element.name in blacklist:
        return
    result.append(element.get_text(recursive=False))
    for child in element.children:
        bs_get_text(result, child, blacklist)


def clean_whitespace(text:str):
    buf = StringIO()
    buf.seek(0)
    whitespace = " \t\r\n\b"
    prev = "\0"
    for c in text:
        if c in whitespace and prev in whitespace:
            prev = c
            continue
        prev = c
        buf.write(c)
    buf.seek(0)
    return buf.read()


def get_html_title(soup):
    title = soup.title
    if title != None:
        return title.get_text()


def import_from_html(html, baseurl=""):
    assert BeautifulSoup != None
    soup = BeautifulSoup(html, "html.parser")
    element_list = soup.find_all(["script", "style"])
    for element in element_list:
        element.extract()
    plain_text = soup.get_text(separator=" ")
    plain_text = clean_whitespace(plain_text)

    images = soup.find_all("img")
    links = soup.find_all("a")
    csses = soup.find_all("link")
    scripts = soup.find_all("script")
    title = get_html_title(soup)

    h = HTML2Text(baseurl=baseurl)
    text = "From %s\n\n" % baseurl + h.handle(html)

    texts = [text]
    images = get_addr_list(images)
    scripts = get_addr_list(scripts)

    return Storage(plain_text=plain_text,
                   images=images,
                   title=title,
                   links=links,
                   csses=csses,
                   scripts=scripts,
                   texts=texts
                   )


class ImportNoteHandler:

    template_path = "note/page/html_importer.html"

    def get_kw(self):
        user_name = xauth.current_name()
        kw = Storage()
        kw.groups = dao.list_group_v2(user_name, orderby="name")
        return kw

    def GET(self):
        address = xutils.get_argument_str("url")
        save = xutils.get_argument_str("save")
        user_name = xauth.current_name_str()

        # 添加日志
        xmanager.add_visit_log(user_name, "/note/html_importer")

        if save != "":
            return self.POST()

        kw = self.get_kw()
        kw.url = address
        kw.address = address
        kw.show_aside = False
        kw.parent_link = LinkConfig.note_plugin_index

        return xtemplate.render(self.template_path, **kw)

    @xauth.login_required()
    def POST(self):
        try:
            file = xutils.get_argument_field_storage("file")
            address = xutils.get_argument_str("url", "")
            name = xutils.get_argument_str("name", "")
            filename = ""
            html = ""

            if hasattr(file, "filename"):
                filename = file.filename

            if not isempty(address):
                address = address.strip()
                html = readhttp(address)
                filename = address
            else:
                # 读取文件
                html = ""
                assert file.file is not None
                for chunk in file.file:
                    html += chunk.decode("utf-8")

            logging.info("import html, filename=%s, length=%s, type=%s", filename, len(html), type(html))

            result = import_from_html(html, address)

            kw = self.get_kw()
            kw.address = address
            kw.url = address
            kw.images = result.images
            kw.links = result.links
            kw.csses = result.csses
            kw.scripts = result.scripts
            kw.texts = result.texts
            kw.article_title = result.title
            kw.plain_text = result.plain_text
            kw.parent_link = LinkConfig.note_plugin_index

            return xtemplate.render(self.template_path, **kw)
        except Exception as e:
            xutils.print_stacktrace()

            kw = self.get_kw()
            kw.error = str(e)

            return xtemplate.render(self.template_path, **kw)


class MarkdownImageParser(TextParserBase):

    def __init__(self) -> None:
        super().__init__()
        self.check_only = False
        self._has_external_image = False

    def escape(self, text):
        return text

    def get_ext_by_content_type(self, content_type):
        return netutil.get_file_ext_by_content_type(content_type)
    
    def has_external_image(self):
        return self._has_external_image
    
    def download(self, url, fpath):
        try:
            return netutil.http_download(url, destpath=fpath)
        except Exception as e:
            logging.error("download (%s) failed", url)
            raise e

    def handle_image(self, url: str, user_name: str):
        from handlers.fs import fs_upload
        # TODO 注意越权问题 host不能是内部地址
        # 1. host不能是内网地址
        # 2. 防止缓存数据过大拖垮服务器

        url = url.replace("\r", "")
        url = url.replace("\n", "")

        if url.startswith("//"):
            url = "https:" + url

        if url.startswith("/"):
            # 已经是本地地址
            return url
        
        if url.startswith("data:"):
            # 数据编码
            return url

        if not url.startswith(("https://", "http://")):
            # 无效的网址
            return url
        
        if self.check_only:
            # 仅校验，不处理
            self._has_external_image = True
            return url
        
        if url.strip() == "":
            return url

        map_info = FsMapDao.get_by_url(url)
        if map_info != None:
            return map_info.webpath

       
        filename = textutil.create_uuid()
        tmp_file = os.path.join(xconfig.FileConfig.tmp_dir, "upload." + filename)
        try:
            resp_headers = self.download(url, tmp_file)
            fpath = fs_upload.get_auto_file_path(filename)
            os.rename(tmp_file, fpath)
        finally:
            fsutil.remove_file(tmp_file, hard=True)

        event = xnote_event.FileUploadEvent()
        event.fpath = fpath
        event.user_name = user_name
        xmanager.fire("fs.upload", event)

        content_type = ""
        if resp_headers != None:
            content_type = resp_headers["Content-Type"]
            ext = self.get_ext_by_content_type(content_type)
            if ext != None:
                new_fpath = fpath + ext
                if fpath != new_fpath:
                    os.rename(fpath, new_fpath)
                    event = xnote_event.FileRenameEvent()
                    event.fpath = new_fpath
                    event.old_fpath = fpath
                    event.user_name = user_name
                    xmanager.fire("fs.rename", event)
                    fpath = new_fpath

        webpath = fsutil.get_safe_webpath(fpath=fpath)
        map_record = FsMapRecord()
        map_record.url = url
        map_record.webpath = webpath
        map_record.content_type = content_type
        map_record.version = 2
        FsMapDao.save(map_record)
        return webpath

    def parse(self, text, user_name):
        self.init(text)

        c = self.current()
        while c != None:
            if self.startswith("!["):
                name_part = self.read_till_target("]")
                self.append_token(name_part)

                if self.current() != "(":
                    self.str_token_append(c)
                    continue
                else:
                    href_part = self.read_till_target(")")
                    url = href_part[1:-1]
                    new_href = self.handle_image(url, user_name)
                    self.append_token("(" + new_href + ")")
            if self.startswith("```"):
                code_part = self.read_till_target("```")
                self.append_token(code_part)
            else:
                self.str_token_append(c)
                self.read_next()

            c = self.current()

        self.save_str_token()
        result = []
        for item in self.tokens:
            result.append(item.value)
        return "".join(result)


class CacheExternalHandler:

    @xauth.login_required("admin")
    def POST(self):
        user_name = xauth.current_name()
        note_id = xutils.get_argument_int("note_id")
        note = dao.get_by_id_creator(note_id, user_name)
        if note == None:
            return webutil.FailedResult(code="fail", message="笔记不存在")
        if note.type != "md":
            return webutil.FailedResult(code="fail", message="文档类型不是markdown,暂时无法处理")

        md_content = note.content
        parser = MarkdownImageParser()
        md_content_new = parser.parse(md_content, note.creator)

        dao_edit.update_content(note, md_content_new)

        return webutil.SuccessResult(message="更新成功")

def has_external_image(note: NoteDO):
    # type: (dict) -> bool
    """判断是否有外部图片资源"""
    if note == None:
        return False
    p = MarkdownImageParser()
    p.check_only = True
    p.parse(note.content, user_name = note.creator)
    return p.has_external_image()

xutils.register_func("note.import_from_html", import_from_html)
xutils.register_func("note.has_external_image", has_external_image)

xurls = (
    r"/note/html_importer", ImportNoteHandler,
    r"/note/cache_external", CacheExternalHandler,
)
