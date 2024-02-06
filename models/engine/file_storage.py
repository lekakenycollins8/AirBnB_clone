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
    __file_path = None
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return __objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(__file_path, "w") as json_file:
            json.dump(FileStorage.__objects, json_file)

    def reload(self):
        """deserializes the JSON file to __objects 
        (only if the JSON file (__file_path) exists"""
        if os.path.exists(FileStorage.__file_path):
            with open(__file_path, encoding="utf-8") as json_file:
                return json.loads(json_file.read())
