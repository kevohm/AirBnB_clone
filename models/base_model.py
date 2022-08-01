#!/usr/bin/python3
'''
	base class here
'''
import uuid
from datetime import datetime

class Base:
    id = uuid.uuid4()
    created_at = datetime.now()
    updated_at = datetime.now()
    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, slef.id, self.__dict__);
    def save(self):
        updated_at = datetime.now()
    def to_dict(self):
        self.__dict__.id = id
