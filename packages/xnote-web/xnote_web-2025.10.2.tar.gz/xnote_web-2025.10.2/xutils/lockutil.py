# -*- coding:utf-8 -*-
# @author xupingmao
# @since 2021/12/04 15:35:23
# @modified 2022/01/23 23:57:56
# @filename lockutil.py
import os
import xutils
from xutils.interfaces import FileLockInterface

try:
	import fcntl
except ImportError:
	fcntl = None

class UnixLock(FileLockInterface):
	"""Unix环境的锁实现"""

	def __init__(self, fpath):
		self.fpath = fpath
		self.fp = open(fpath, "w+")
		self.got_lock = False

	def try_lock(self):
		try:
			# 获取锁时flock返回None
			# 未获取锁抛出异常: BlockingIOError: [Errno 11] Resource temporarily unavailable
			fcntl.lockf(self.fp, fcntl.LOCK_EX | fcntl.LOCK_NB)
			content = str(os.getpid())
			self.fp.write(content)
			self.fp.flush()
			self.got_lock = True
			return True
		except:
			xutils.print_exc()
			# TODO 这里读取文件内容为空，并且会清除文件内容，但是cat命令可以正常读取
			# pid = self.fp.read(1024)
			# raise Exception("lock file failed, locked by pid:%s" % pid)
			return False

	def unlock(self):		
		if self.got_lock:
			fcntl.flock(self.fp, fcntl.LOCK_UN)
			# 不需要重置为空
			self.fp.close()
			self.got_lock = False
		return True

class WinLock(FileLockInterface):
	"""Windows环境的锁实现"""

	def __init__(self, fpath):
		self.fpath = fpath
		self.got_lock = False

	def try_lock(self):
		if not os.path.exists(self.fpath):
			with open(self.fpath, "w+") as fp:
				fp.write(str(os.getpid()))
			self.got_lock = True
			return True
		return False
	
	def unlock(self):
		if not self.got_lock:
			return
		
		if os.path.exists(self.fpath):
			pid = ""
			with open(self.fpath, "r") as fp:
				pid = fp.read().strip()

			if pid == str(os.getpid()):
				os.remove(self.fpath)
			else:
				raise Exception(f"unlock failed, file pid={pid}, os pid={os.getpid()}")


class FileLockAdapter(FileLockInterface):
	"""文件锁，注意目前只支持posix系统"""

	def __init__(self, fpath):
		self.fpath = fpath
		if fcntl != None:
			self.impl = UnixLock(fpath)
		else:
			self.impl = WinLock(fpath)

	def try_lock(self):
		return self.impl.try_lock()

	def unlock(self):
		return self.impl.unlock()


class DummyLock(FileLockInterface):
	pass