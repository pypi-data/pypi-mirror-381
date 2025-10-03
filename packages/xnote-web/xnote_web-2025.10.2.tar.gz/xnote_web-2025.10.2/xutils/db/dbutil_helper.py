# encoding=utf-8


def new_from_dict(class_, dict_value):
    obj = class_()
    obj.update(dict_value)
    return obj

def new_from_dict_list(class_, dict_list: list):
    result = []
    for item in dict_list:
        obj = class_()
        obj.update(item)
        result.append(obj)
    return result

class PageBuilder:
    """分页构造器"""
    def __init__(self, offset=0, limit=20):
        self.records = []
        self.offset = offset
        self.limit = limit
        self.total = 0

    def add_record(self, record):
        if self.total >= self.offset and len(self.records) < self.limit:
            self.records.append(record)
        self.total += 1
    
    @property
    def reached_limit(self):
        return len(self.records) >= self.limit

def batch_iter(data=[], batch_size=20):
    """把一个大的列表拆分成多个批次"""
    i = 0
    while i < len(data):
        batch = data[i:i+batch_size]
        yield batch
        i += batch_size

