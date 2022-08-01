#!/usr/bin/python3
'''
	base class here
'''
import uuid
from datetime import datetime

class BaseModel:
    id = str(uuid.uuid4())
    created_at = datetime.now()
    updated_at = datetime.now()
    def __init__(self, *args, **kwargs):
        '''constructor'''
        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
        else:
            for kwarg in kwargs:
                if kwarg != "__class__":
                    if kwarg == "created_at" or kwarg == "updated_at":
                        self.__dict__[kwarg] = datetime.strptime(kwargs.get(kwarg), "%Y-%m-%dT%H:%M:%S.%f")
                    else:
                        self.__dict__[kwarg] = kwargs.get(kwarg);
    def __str__(self):
        '''representation of subclass of Base'''
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'
    def save(self):
        '''save updated object'''
        updated_at = datetime.now()
    def to_dict(self):
        '''represent as string'''
        dict_model = self.__dict__
        dict_model['id'] = self.id
        dict_model['__class__'] = self.__class__.__name__
        dict_model['created_at'] = self.created_at.isoformat()
        dict_model['updated_at'] = self.updated_at.isoformat()
        return dict_model
