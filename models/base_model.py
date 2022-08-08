#!/usr/bin/python3
'''
    base class
'''
import models
import uuid
from datetime import datetime


class BaseModel:
    '''
        BaseModel
    '''
    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.
        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        frmt = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, frmt)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def __str__(self):
        '''representation of subclass of Base'''
        cls_name = self.__class__.__name__
        return "[{}] ({}) {}".format(cls_name, self.id, self.__dict__)

    def save(self):
        '''save updated object'''
        updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        '''represent as string'''
        dict_model = self.__dict__.copy()
        dict_model['id'] = self.id
        dict_model['__class__'] = self.__class__.__name__
        dict_model['created_at'] = self.created_at.isoformat()
        dict_model['updated_at'] = self.updated_at.isoformat()
        return dict_model
