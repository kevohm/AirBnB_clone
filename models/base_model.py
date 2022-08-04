#!/usr/bin/python3
'''
	base class here
'''
from __init__ import storage
import uuid
from datetime import datetime

class BaseModel:
    '''
        BaseModel
    '''
    id = str(uuid.uuid4())
    created_at = datetime.now()
    updated_at = datetime.now()
    def __init__(self, *args, **kwargs):
        '''constructor'''
        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            for k in kwargs:
                if k != "__class__":
                    frmt = "%Y-%m-%dT%H:%M:%S.%f"
                    if k == "created_at" or k == "updated_at":
                        self.__dict__[k] = datetime.strptime(kwargs.get(k), frmt)
                    else:
                        self.__dict__[k] = kwargs.get(k);
    def __str__(self):
        '''representation of subclass of Base'''
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'
    def save(self):
        '''save updated object'''
        updated_at = datetime.now()
        storage.save()
    def to_dict(self):
        '''represent as string'''
        dict_model = self.__dict__
        dict_model['id'] = self.id
        dict_model['__class__'] = self.__class__.__name__
        dict_model['created_at'] = self.created_at.isoformat()
        dict_model['updated_at'] = self.updated_at.isoformat()
        return dict_model
