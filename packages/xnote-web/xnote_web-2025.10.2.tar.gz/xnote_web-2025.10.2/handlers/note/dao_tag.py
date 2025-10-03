# -*- coding:utf-8 -*-
"""
@Author       : xupingmao
@email        : 578749341@qq.com
@Date         : 2022-08-20 15:46:37
@LastEditors  : xupingmao
@LastEditTime : 2024-06-29 19:48:32
@FilePath     : /xnote/handlers/note/dao_tag.py
@Description  : 标签
"""

import json
import xutils
import logging
import typing
import handlers.note.dao as note_dao

from xnote.core import xtables
from xnote.core import xauth
from xutils import functions, lists
from xutils import dbutil
from xutils import attrget, Storage
from xutils.base import BaseDataRecord, BaseEnum, EnumItem
from handlers.note.dao_api import NoteDao
from xnote.service import NoteTagBindService, TagTypeEnum, TagBindDO
from xnote.service import NoteTagInfoService, TagInfoDO
from xnote.service import TagCategoryService, TagCategoryDO
from xnote.service import SystemTagEnum
from .models import NoteIndexDO
from xnote.plugin import TextLink

class TagCategoryDetail(TagCategoryDO):
    def __init__(self, name = "", link: typing.Optional[TextLink] = None, 
                 is_system = False, **kw):
        self.name = name
        self.tag_list = []

        if link:
            self.link = link
        else:
            self.link = TextLink()

        self.is_system = is_system
        self.update(kw)

    @property
    def title(self):
        return self.name

class _TagBindDaoImpl:
    """标签绑定信息"""
    tag_bind_service = NoteTagBindService

    def get_by_note_id(self, user_id=0, note_id=0):
        return self.tag_bind_service.list_by_target_id(user_id=user_id, target_id=note_id)
    
    def list_by_note_id(self, user_id=0, note_id=0):
        return self.tag_bind_service.list_by_target_id(user_id=user_id, target_id=note_id)
    
    def list_by_tag(self, user_id=0, tag_code=""):
        return self.tag_bind_service.list_by_tag(user_id=user_id, tag_code=tag_code)
    
    @classmethod    
    def get_uniq_tags(cls, new_tags=[]):
        return lists.get_uniq_list(new_tags)
    
    def update_tag(self, user_id=0, note_id=0, tags=[]):
        self.tag_bind_service.bind_tags(user_id=user_id, target_id=note_id, tags=tags)
    
    def update_tag_and_note(self, user_id=0, note_id=0, tags: typing.Sequence[str]=[]):
        tags = self.get_uniq_tags(tags)
        note_index = note_dao.NoteIndexDao.get_by_id(note_id)
        if note_index == None:
            raise Exception("note is empty")
        old_tags = self.get_by_note_id(user_id=user_id, note_id=note_id)
        old_tag_codes = [x.tag_code for x in old_tags]

        self.tag_bind_service.bind_tags(user_id=user_id, target_id=int(note_id), tags=tags)
        note_index.set_tags(tags)
        note_dao.update_index(note_index)

        all_tags = set()
        all_tags.update(tags)
        all_tags.update(old_tag_codes)

        for tag_code in all_tags:
            count = self.tag_bind_service.count_user_tag(user_id=user_id, tag_code=tag_code)
            NoteTagInfoDao.update_tag_amount(user_id=user_id, tag_code=tag_code, amount=count)

    def list_tag(self, user_id=0):
        tag_list, count = NoteTagInfoService.get_page(user_id=user_id, limit=1000, skip_count=True)
        return tag_list
    
    def get_note_page_by_tag(self, user_id=0, tag_code="", offset=0, limit=20, order=None):
        tag_bind_list, amount = self.tag_bind_service.get_page(user_id=user_id, tag_code=tag_code, 
                                                               offset=offset, limit=limit, order=order)
        note_id_list = [x.target_id for x in tag_bind_list]
        return note_dao.batch_query_list(id_list=note_id_list, creator_id=user_id), amount
    
    def batch_get_tag_bind(self, user_id=0, target_id_list=[]) -> typing.List[TagBindDO]:
        if len(target_id_list) == 0:
            return []
        result, _ = NoteTagBindService.get_page(user_id=user_id, target_id_list=target_id_list, skip_count=True)
        return result
    
    def append_tag(self, note_id=0, tag_code=""):
        """向笔记追加标签"""
        note_info = note_dao.get_by_id(note_id)
        if note_info == None:
            raise Exception("笔记不存在")
        tags = note_info.tags
        assert isinstance(tags, list)
        tags.append(tag_code)
        NoteTagBindDao.update_tag_and_note(note_info.creator_id, note_id, tags)

    def remove_tag(self, note_id=0, tag_code=""):
        note_info = note_dao.get_by_id(note_id)
        if note_info == None:
            raise Exception("笔记不存在")
        tags = note_info.tags
        assert isinstance(tags, list)
        tags.remove(tag_code)
        NoteTagBindDao.update_tag_and_note(note_info.creator_id, note_id, tags)

    def delete_by_note_id(self, user_id=0, note_id=0):
        self.tag_bind_service.delete_tags(user_id=user_id, target_id=note_id)


class _NoteTagInfoDaoImpl:
    tag_info_service = NoteTagInfoService

    def create(self, user_id=0, tag_code=""):
        old = self.get_by_code(user_id=user_id, tag_code=tag_code)
        if old is not None:
            return
        
        tag_info = TagInfoDO()
        tag_info.tag_code = tag_code
        tag_info.user_id = user_id
        return self.tag_info_service.create(tag_info)

    def count(self, user_id=0):
        return self.tag_info_service.count(user_id=user_id)
    
    def get_by_code(self, user_id=0, tag_code=""):
        return self.tag_info_service.get_first(user_id=user_id, tag_code=tag_code)
    
    def search(self, user_id=0, tag_code_like="", order=None):
        return self.tag_info_service.search(user_id=user_id, tag_code_like=tag_code_like, order=order)
    
    def list(self, user_id=0, group_id=0, order=None) -> typing.List[TagInfoDO]:
        if group_id > 0:
            tags = NoteTagBindDao.get_by_note_id(user_id=user_id, note_id=group_id)
            tag_code_list = [x.tag_code for x in tags]
            tag_info_list = NoteTagInfoService.get_by_code_list(user_id=user_id, tag_code_list=tag_code_list, order=order)
            tag_info_dict = {} # type: dict[str, TagInfoDO]
            for tag_info in tag_info_list:
                tag_info_dict[tag_info.tag_code] = tag_info

            result = [] # type: list[TagInfoDO]
            for tag_code in tag_code_list:
                tag_info = tag_info_dict.get(tag_code)
                if tag_info is None:
                    tag_info = TagInfoDO(tag_code=tag_code, tag_name=tag_code)
                else:
                    tag_info.tag_name = get_name_by_code(tag_info.tag_code)
                result.append(tag_info)
            return result
        result, _ = NoteTagInfoService.get_page(user_id=user_id, limit=1000, skip_count=True, order=order)
        for item in result:
            item.tag_name = get_name_by_code(item.tag_code)
        return result
    
    def update_tag_amount(self, user_id=0, tag_code="", amount=0):
        self.fix_dup_tag(user_id=user_id, tag_code=tag_code)
        self.tag_info_service.update_amount(user_id=user_id, tag_code=tag_code, amount=amount)

    def fix_dup_tag(self, user_id=0, tag_code=""):
        tag_list = self.tag_info_service.get_by_code_list(user_id=user_id, tag_code_list=[tag_code], order="tag_id")
        if len(tag_list) == 0:
            new_tag = TagInfoDO(tag_code=tag_code, user_id=user_id)
            self.tag_info_service.create(new_tag)
            return
        if len(tag_list) > 1:
            for tag in tag_list[1:]:
                self.tag_info_service.delete(tag)
        

def bind_tags(user_id=0, note_id=0, tags=[], tag_type="group"):
    NoteTagBindDao.update_tag_and_note(user_id=user_id, note_id=note_id, tags=tags)


def batch_get_tags_by_notes(notes: typing.List[NoteIndexDO]):
    if len(notes) == 0:
        return

    note_id_list = [x.id for x in notes]
    creator_id = notes[0].creator_id
    bind_list = NoteTagBindDao.batch_get_tag_bind(user_id=creator_id, target_id_list=note_id_list)
    tag_dict = {} # type: dict[int, list]

    for bind in bind_list:
        tags = tag_dict.get(bind.target_id)
        if tags is None:
            tags = []
        tags.append(bind.tag_code)
        tag_dict[bind.target_id] = tags
    
    for note in notes:
        tags = tag_dict.get(note.id, [])
        note.tags = tags
        note.tags_json = json.dumps(tags)


def get_tag_name_by_code(tag_code: str):
    return SystemTagEnum.get_name_by_code(tag_code)

def handle_tag_for_note(note_info: note_dao.NoteIndexDO):
    note = note_info
    if note.tags == None:
        note.tags = []
    note.tags_json = xutils.tojson(note.tags)
    tag_info_list = []
    for tag_code in note.tags:
        tag_name = get_name_by_code(tag_code)
        tag_info = TagInfoDO(tag_code = tag_code, tag_name = tag_name)
        tag_info_list.append(tag_info)
    note.tag_info_list = tag_info_list


def append_tag(note_id=0, tag_code=""):
    NoteTagBindDao.append_tag(note_id, tag_code)

def get_skip_tag_type(tag_type=0):
    if tag_type == 0:
        return True
    return False

def list_tag_category_detail(user_id=0, tag_type=0):
    skip_tag_type = get_skip_tag_type(tag_type)
    all_tags, _ = NoteTagInfoService.get_page(user_id=user_id, tag_type=tag_type, limit=1000, 
                                              skip_count=True, skip_tag_type=skip_tag_type, order="amount desc")
    cate_list = TagCategoryService.list(user_id=user_id)
    cate_dict = {} # type: dict[int, TagCategoryDetail]
    cate_detail_list = [] # type: list[TagCategoryDetail]
    for item in cate_list:
        cate_info = TagCategoryDetail(**item)
        cate_dict[item.category_id] = cate_info
        cate_detail_list.append(cate_info)
    
    sys_cate = TagCategoryDetail(name="系统标签", is_system = True)
    other_cate = TagCategoryDetail(name="其他标签")

    for item in all_tags:
        item.tag_name = get_name_by_code(item.tag_code)
        if SystemTagEnum.is_sys_tag(item.tag_code):
            sys_cate.tag_list.append(item)
        else:
            cate_info = cate_dict.get(item.category_id)
            if cate_info != None:
                cate_info.tag_list.append(item)
            else:
                other_cate.tag_list.append(item)

    result = [] # type: list[TagCategoryDetail]
    result.append(sys_cate)

    for item in cate_detail_list:
        if len(item.tag_list) > 0:
            result.append(item)
    
    if len(other_cate.tag_list) > 0:
        result.append(other_cate)

    return result

NoteTagInfoDao = _NoteTagInfoDaoImpl()
NoteTagBindDao = _TagBindDaoImpl()
get_name_by_code = get_tag_name_by_code

