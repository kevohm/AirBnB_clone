#!/usr/bin/python3
'''
    file storage class
'''
import json
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        key = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(key, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        main_dict = FileStorage.__objects
        obj_write = {obj: main_dict[obj].to_dict() for obj in main_dict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_write, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f2:
                obj_read = json.load(f2)
                for v in obj_read.values():
                    cls_name = v["__class__"]
                    del v["__class__"]
                    self.new(eval(cls_name)(**v))
        except FileNotFoundError:
            return
