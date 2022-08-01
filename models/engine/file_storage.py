#!/usr/bin/python3
'''
    file storage class
'''
class FileStorage:
    __file_path = 0
    __objects = {}
    def all(self):
        return FileStorage.__objects
    def new(self, obj):
        FileStorage.__objects[obj.__class__.__name__ + str(obj.id)] = obj
    def save(self):
        for obj in FileStorage.__objects.values():
            with open(FileStorage.__file_path) as f:
                f.write(json.dumps(obj.__dict__));
    def reload(self):
        try:
            with open(FileStorage.__file_path, "w+") as f:
                obj = json.loads(f.read())
        except:
            pass
