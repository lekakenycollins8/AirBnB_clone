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

    def allclasses(self):
        """returns a dictionary of all Airbnb classes"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes ={"BaseModel": BaseModel,
                "User": User,
                "State": State,
                "City": City,
                "Amenity": Amenity,
                "Place": Place,
                "Review": Review}
        return classes


    def reload(self):
        """deserializes the JSON file to __objects 
        (only if the JSON file (__file_path) exists"""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, encoding="utf-8") as json_file:
                try:
                    object_data = json.load(json_file)
                    for key, data in object_data.items():
                        obj_class_name = data.get("__class__")
                        if obj_class_name:
                            if obj_class_name in self.allclasses():
                                obj_class = self.allclasses()[obj_class_name]
                                instance = obj_class(**data)
                            FileStorage.__objects[key] = instance
                except FileNotFoundError:
                    pass
