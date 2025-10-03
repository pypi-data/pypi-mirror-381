# -*- coding:utf-8 -*-
"""
@Author       : xupingmao
@email        : 578749341@qq.com
@Date         : 2022-08-20 16:53:16
@LastEditors  : xupingmao
@LastEditTime : 2024-06-23 09:48:23
@FilePath     : /xnote/handlers/note/dao_delete.py
@Description  : 删除的处理
"""

import xutils
from .dao_api import NoteDao
from .dao import (
    delete_history,
    add_history,
    get_by_id,
    update_children_count,
    put_note_to_db,
    delete_note_skey,
    refresh_note_stat,
    _full_db,
    NoteIndexDao
)

from .dao_tag import NoteTagBindDao
from .constant import DELETED_PREFIX
from xutils import textutil

def delete_note_physically(creator: str, note_id: int):
    assert creator != None, "creator can not be null"
    assert note_id != None, "note_id can not be null"

    _full_db.delete_by_id(note_id)
    NoteIndexDao.delete_by_id(int(note_id))
    delete_history(note_id)


def delete_note(id):
    note = get_by_id(id)
    if note is None:
        return

    if note.is_deleted != 0:
        # 已经被删除了，执行物理删除
        delete_note_physically(note.creator, note.id)
        return

    # 标记删除
    note.mtime = xutils.format_datetime()
    note.dtime = xutils.format_datetime()
    note.is_deleted = 1

    # 防止冲突
    note.name = textutil.add_prefix(note.name, DELETED_PREFIX)
    
    put_note_to_db(id, note)

    # 更新数量
    update_children_count(note.parent_id)
    NoteTagBindDao.delete_by_note_id(note.creator_id, id)

    # 删除skey索引
    delete_note_skey(note)

def recover_note(id):
    """恢复删除的笔记"""
    note = get_by_id(id)
    if note is None:
        return
    
    if note.is_deleted == 0:
        return
    
    note.mtime = xutils.format_datetime()
    note.is_deleted = 0
    note.version = note.version + 1
    
    # 记录变更日志
    add_history(id, note.version, note)
    # 更新数据
    put_note_to_db(id, note)
    # 更新数量
    update_children_count(note.parent_id)

xutils.register_func("note.delete", delete_note)
xutils.register_func("note.delete_physically", delete_note_physically)


NoteDao.delete_note = delete_note
