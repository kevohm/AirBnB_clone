#!/usr/bin/python3

from models import storage

from models.base_model import BaseModel

u = BaseModel()
print(u)
u.save()
print(u)
print({ i for i in storage.all().values()})
