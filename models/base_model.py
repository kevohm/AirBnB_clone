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
    def __init__(self, *args, **kwargs):
        '''constructor'''
        frmt = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for k in kwargs:
                if k != "__class__":
                    if k == "created_at" or k == "updated_at":
                        self.__dict__[k] = datetime.strptime(kwargs.get(k), frmt)
                    else:
                        self.__dict__[k] = kwargs.get(k);
        else:
            storage.new(self)

    def __str__(self):
        '''representation of subclass of Base'''
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        '''save updated object'''
        updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        '''represent as string'''
        dict_model = self.__dict__.copy()
        dict_model['id'] = self.id
        dict_model['__class__'] = self.__class__.__name__
        dict_model['created_at'] = self.created_at.isoformat()
        dict_model['updated_at'] = self.updated_at.isoformat()
        return dict_model
