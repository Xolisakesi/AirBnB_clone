#!/usr/bin/python3
"""This module defines the FileStorage class."""
import json

class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file to instances."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        with open(self.__file_path, "w") as file:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, file)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(self.__file_path, "r") as file:
                data = json.load(file)
                from models.base_model import BaseModel
                for k, v in data.items():
                    class_name = v['__class__']
                    del v['__class__']
                    self.__objects[k] = eval(class_name)(**v)
        except FileNotFoundError:
            pass

    def classes(self):
        """Returns a dictionary of available classes"""
        from models.base_model import BaseModel
        return {"BaseModel": BaseModel}

