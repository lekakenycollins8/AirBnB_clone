"""Module with class FileStorage that serializes and deserializes JSON file"""


import os
import json

class FileStorage:
    """serializes instances to a JSON file and deserializes 
    JSON file to instances

    Attributes:
        private class attributes: 
            __file_path: string - path to the JSON file 
            __objects: dictionary - empty but will store all objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        serialized_objects = {}
        for key, obj in FileStorage.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(FileStorage.__file_path, "w") as json_file:
            json.dump(serialized_objects, json_file)

    def reload(self):
        """deserializes the JSON file to __objects 
        (only if the JSON file (__file_path) exists"""
        try:
            with open(FileStorage.__file_path, "r") as json_file:
                data = json.load(json_file)
                for key, obj in data.items():
                    class_name, obj_id = key.split(".")
                    module = __import__('models.' + class_name, fromlist=[class_name])
                    cls = getattr(module, class_name)
                    instance = cls(**val)
                    FileStorage.__objects[key] = instance
        except FileNotFoundError:
            pass
