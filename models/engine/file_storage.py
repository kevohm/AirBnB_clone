#!/usr/bin/python3
'''
    file storage class
'''
import json

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
        obj_write = {obj: main_dict[obj].to_dict()  for obj in main_dict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_write, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                obj_read = json.load(f)
                for v in obj_read.values():
                    cls_name = v["__class__"]
                    del v["__class__"]
                    self.new(eval(cls_name)(**v))
                print("[object] = {} [__object] ={}".format(eval(cls_name).get(v.id)), FileStorage.__objects)
        except:
            return
