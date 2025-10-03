# encoding=utf-8
# @author xupingmao
# @since 2016/12/09
# @modified 2022/02/05 21:54:58

"""处理时间的工具类

==========
格式化的参数
==========

%Y  Year with century as a decimal number.
%m  Month as a decimal number [01,12].
%d  Day of the month as a decimal number [01,31].
%H  Hour (24-hour clock) as a decimal number [00,23].
%M  Minute as a decimal number [00,59].
%S  Second as a decimal number [00,61].
%z  Time zone offset from UTC.
%a  Locale's abbreviated weekday name.
%A  Locale's full weekday name.
%b  Locale's abbreviated month name.
%B  Locale's full month name.
%c  Locale's appropriate date and time representation.
%I  Hour (12-hour clock) as a decimal number [01,12].
%p  Locale's equivalent of either AM or PM.

=======
tm结构体
=======
tm_year  实际的年份
tm_mon   月份（从一月开始，0代表一月） - 取值区间为[0,11]
tm_mday  一个月中的日期 - 取值区间为[1,31]
tm_wday  星期 – 取值区间为[0,6]，其中0代表星期天，1代表星期一，以此类推
tm_yday  从每年的1月1日开始的天数 – 取值区间为[0,365]，其中0代表1月1日，1代表1月2日，以此类推


"""
import typing
import time
import math
import datetime

SECONDS_PER_DAY = 3600 * 24
DEFAULT_FORMAT = '%Y-%m-%d %H:%M:%S'
FORMAT = DEFAULT_FORMAT
DATE_FORMAT = "%Y-%m-%d"
DATETIME_FORMAT = DEFAULT_FORMAT
DEFAULT_DATETIME = "1970-01-01 00:00:00"
DEFAULT_DATE = "1970-01-01"
DEFAULT_DATETIME_OBJ = datetime.datetime(1970, 1, 1)

WDAY_DICT = {
    "*": u"每天",
    "1": u"周一",
    "2": u"周二",
    "3": u"周三",
    "4": u"周四",
    "5": u"周五",
    "6": u"周六",
    "7": u"周日"
}

class DateInfo:

    def __init__(self, year = 1, month = 1, day = 1):
        self.year = year
        self.month = month
        self.day = day
        self.wday = 0 # week day
        self.time = "00:00:00"

    def next_month(self):
        if self.month == 12:
            return DateInfo(year=self.year+1, month=1, day = 1)
        return DateInfo(year=self.year, month=self.month+1, day=self.day)
    
    def format_year_month(self):
        return f"{self.year:04}-{self.month:02}"
    
    def format_date(self):
        return f"{self.year:04}-{self.month:02}-{self.day:02}"

    def __repr__(self):
        return "(%r,%r,%r)" % (self.year, self.month, self.day)

def to_py_date(date_info: "str|datetime.date"):
    """转换成python内置的date类型
    >>> to_py_date("2020-01-02")
    datetime.date(2020, 1, 2)
    >>> to_py_date("2020-01-02 00:00:00")
    datetime.date(2020, 1, 2)
    """
    if isinstance(date_info, str):
        try:
            return datetime.datetime.strptime(date_info, DATE_FORMAT).date()
        except:
            return datetime.datetime.strptime(date_info, DATETIME_FORMAT).date()
    assert isinstance(date_info, datetime.date)
    return date_info

def to_py_datetime(datetime_info: "str|datetime.date"):
    """转换成python内置的datetime类型
    >>> to_py_datetime("2020-01-01 00:00:00")
    datetime.datetime(2020, 1, 1, 0, 0)
    >>> to_py_datetime(datetime.datetime(2020,1,2))
    datetime.datetime(2020, 1, 2, 0, 0)
    """
    if isinstance(datetime_info, str):
        timestamp = parse_datetime(datetime_info)
        return datetime.datetime.fromtimestamp(timestamp)
    assert isinstance(datetime_info, datetime.datetime)
    return datetime_info

def is_str(s):
    return isinstance(s, str)

def before(days:typing.Optional[int]=None, month:typing.Optional[int]=None, format=False):
    if days is not None:
        fasttime = time.time() - days * SECONDS_PER_DAY
        if format:
            return format_time(fasttime)
        return fasttime
    return None

def days_before(days:int, format=False):
    """获取N天前的日期"""
    seconds = time.time()
    seconds -= days * 3600 * 24
    if format:
        return format_time(seconds)
    return time.localtime(seconds)


def format_datetime(value: typing.Union[None, datetime.datetime, float] = None, 
                    format='%Y-%m-%d %H:%M:%S'):
    """格式化日期时间
    >>> format_datetime(0)
    '1970-01-01 08:00:00'
    """
    if value == None:
        return time.strftime(format)
    elif isinstance(value, datetime.datetime):
        return value.strftime(format)
    else:
        st = time.localtime(value)
        return time.strftime(format, st)

format_time = format_datetime

def format_time_only(seconds: typing.Optional[float]=None):
    """只格式化时间 TODO 时区问题
    >>> format_time_only(0)
    '08:00:00'
    """
    if seconds == None:
        return time.strftime('%H:%M:%S')
    else:
        st = time.localtime(seconds)
        return time.strftime('%H:%M:%S', st)

def format_weekday(date_str:str, fmt = "") -> str:
    if fmt == "":
        fmt = "%Y-%m-%d"
    
    tm = time.strptime(date_str, fmt)
    wday = str(tm.tm_wday + 1)
    return WDAY_DICT.get(wday) or ""

format_wday = format_weekday
convert_date_to_wday = format_weekday

def datetime_to_weekday(datetime_obj: typing.Union[None, datetime.datetime, str]):
    """把datetime转换成星期"""
    if datetime_obj is None:
        return ""
    if isinstance(datetime_obj, datetime.datetime):
        weekday = str(datetime_obj.weekday()+1)
        return WDAY_DICT.get(weekday, "")
    if isinstance(datetime_obj, str):
        parts = datetime_obj.split()
        if len(parts) == 0:
            return ""
        date_str = parts[0]
        return format_weekday(date_str)
    raise Exception("unsupported type: %r" % type(datetime_obj))

def format_date(value: typing.Union[None, datetime.datetime, str, float]=None, fmt = ""):
    """格式化日期
    >>> format_date("2020-01-01 00:00:00", "/")
    '2020/02/01'
    >>> format_date(1000)
    '1970-01-01'
    >>> format_date(1000, "/")
    '1970/01/01'
    """
    arg_fmt = fmt
    if fmt == "":
        fmt = "%Y-%m-%d"
    if arg_fmt == "/":
        fmt = "%Y/%m/%d"
    if value is None:
        return time.strftime(fmt)
    elif isinstance(value, datetime.datetime):
        return value.strftime(fmt)
    elif isinstance(value, str):
        date_str = value.split(" ")[0]
        if arg_fmt == "/":
            date_str = date_str.replace("-", "/")
        return date_str
    elif isinstance(value, (float, int)):
        st = time.localtime(value)
        return time.strftime(fmt, st)
    raise Exception(f"invalid type: {type(value)}")
        

def format_mmdd(seconds:typing.Union[str, float, None]=None):
    """格式化月/日
    >>> format_mmdd(0)
    '01/01'
    >>> format_mmdd("2020-12-02")
    '12/02'
    """
    if isinstance(seconds, str):
        date_part = seconds.split(" ")[0]
        date_part = date_part.replace("-", "/")
        parts = date_part.split("/")
        if len(parts) != 3:
            return date_part
        return "%s/%s" % (parts[-2], parts[-1])
    else:
        return format_date(seconds, "%m/%d")

def format_millis(mills: typing.Union[int, float]):
    return format_time(mills / 1000)

def parse_date_to_timestamp(date_str: str):
    st = time.strptime(date_str, DATE_FORMAT)
    return time.mktime(st)

def parse_date_to_struct(date_str=""):
    return time.strptime(date_str, DATE_FORMAT)

def parse_date_to_object(date_str: str):
    """解析日期结构
    @param {string} date_str 日期的格式

        >>> parse_date_to_object("2020-01")
        (2020,1,None)
        >>> parse_date_to_object("2020")
        (2020,None,None)
        >>> parse_date_to_object("2020-01-01")
        (2020,1,1)
        >>> parse_date_to_object("2020-01-01 00:00:00")
        (2020,1,1)
    """
    assert date_str != None
    assert isinstance(date_str, str)
    
    date_parts = date_str.split(" ")
    date_str = date_parts[0]
    time_str = "00:00:00"
    if len(date_parts) > 1:
        time_str = date_parts[1]
    parts = date_str.split("-")
    
    date_object = DateInfo()
    date_object.time = time_str

    def _parse_int(value):
        try:
            return int(value)
        except:
            raise Exception("parse_date: invalid date str %r" % date_str)

    if len(parts) == 0:
        raise Exception("parse_date: invalid date str %r" % date_str)
        
    if len(parts) >= 1:
        date_object.year = _parse_int(parts[0])

    if len(parts) >= 2:
        date_object.month = _parse_int(parts[1])

    if len(parts) >= 3:
        date_object.day = _parse_int(parts[2])

    return date_object


def parse_datetime(date: typing.Union[str, datetime.datetime] = "", fmt = DEFAULT_FORMAT) -> float:
    """解析时间字符串为unix时间戳
    :param {string} date: 时间
    :param {string} fmt: 时间的格式
    :return {float}: 时间戳，单位是秒
    """
    if date == "":
        return time.time()
    if isinstance(date, datetime.datetime):
        return date.timestamp()
    st = time.strptime(date, fmt)
    return time.mktime(st)

parse_time = parse_datetime

def get_seconds(date = "", fmt = DEFAULT_FORMAT):
    return parse_datetime(date, fmt)

def get_current_year():
    """获取当前年份"""
    tm = time.localtime()
    return tm.tm_year

def get_current_month():
    """获取当前月份"""
    tm = time.localtime()
    return tm.tm_mon

def get_current_mday():
    """返回今天在当前月份的日子"""
    tm = time.localtime()
    return tm.tm_mday

def current_wday() -> str:
    tm = time.localtime()
    wday = str(tm.tm_wday + 1)
    return WDAY_DICT.get(wday) or ""

def date_str_add(date_str="1970-01-01", years=0, months=0, days=0):
    tm = parse_date_to_struct(date_str)
    year, month, day = date_add(tm, years=years, months=months, days=days)
    return datetime.datetime(year, month, day).strftime(DATE_FORMAT)

def date_add(tm: typing.Optional[time.struct_time], years = 0, months = 0, days = 0):
    """date计算"""
    if tm is None:
        tm = time.localtime()
    else:
        assert isinstance(tm, time.struct_time)
    
    year  = tm.tm_year
    month = tm.tm_mon
    day   = tm.tm_mday
    if years != 0:
        year += years
    if months != 0:
        assert months > -12
        if months < 0:
            year -= 1
            months += 12
        month += months
        year += math.floor((month - 1.0) / 12)
        month = (month - 1) % 12 + 1
    if days != 0:
        date_obj = datetime.datetime(year=year, month=month, day=day)
        date_obj += datetime.timedelta(days=days)
        return date_obj.year, date_obj.month, date_obj.day
    return int(year), month, day

def get_last_day_of_month(date_info: datetime.date):
    """获取一个月的最后一天"""
    new_day = get_days_of_month(date_info.year, date_info.month)
    return datetime.date(date_info.year, date_info.month, new_day)

def get_first_day_of_month(date_info: datetime.date):
    """获取一个月的第一天"""
    return datetime.date(date_info.year, date_info.month, 1)

def get_last_day_of_year(date: datetime.date):
    """获取一年的最后一天"""
    return datetime.date(date.year, 12, 31)

def is_leap_year(year: int):
    """判断是否是闰年"""
    return ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)

def get_days_of_month(year=2020, month=1):
    """获取指定月份的天数 (get days of a month)
        >>> get_days_of_month(2000, 2)
        29
        >>> get_days_of_month(2001, 2)
        28
        >>> get_days_of_month(2002, 1)
        31
        >>> get_days_of_month(1900, 2)
        28
    """
    days = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
    if 2 == month:
        if is_leap_year(year):
            d = 29
        else:
            d = 28
    else:
        d = days[month-1]
    return d

def match_time(year: typing.Optional[int] = None, month: typing.Optional[int] = None, 
               day: typing.Optional[int] = None, wday: typing.Optional[int] = None, 
               tm: typing.Optional[time.struct_time] = None):
    if tm is None:
        tm = time.localtime()
    if year is not None and year != tm.tm_year:
        return False
    if month is not None and month != tm.tm_mon:
        return False
    if day is not None and day != tm.tm_mday:
        return False
    if wday is not None and wday != tm.tm_wday:
        return False
    return True

def get_today():
    return format_date()

def is_empty_datetime(value: typing.Union[str, datetime.datetime]):
    if value == DEFAULT_DATETIME or value == "":
        return True
    if isinstance(value, datetime.datetime):
        return value == DEFAULT_DATETIME_OBJ
    return False
    