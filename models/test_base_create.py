#!/usr/bin/python3

from __init__ import storage

from base_model import BaseModel

u = BaseModel()
print(u)
u.save()
print(u)
print({ i for i in storage.all().values()})
