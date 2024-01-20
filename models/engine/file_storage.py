#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
import inspect
import sys
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects.copy()

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def delete(self, key):
        """Deletes an object from __objects if it is inside"""
        if key in FileStorage.__objects.keys():
            del FileStorage.__objects[key]
            self.save()

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, "w", encoding='utf-8') as f:
            casted_dict = {}
            for key, value in FileStorage.__objects.items():
                casted_dict[key] = value.to_dict()
            json.dump(casted_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, "r", encoding='utf-8') as f:
                data = json.load(f)
                for key, value in data.items():
                    class_name = value.get("__class__")
                    if class_name:
                        cls = globals().get(class_name)
                        if cls and inspect.isclass(cls) and issubclass(cls, BaseModel):
                            FileStorage.__objects[key] = cls(**value)
        except (FileNotFoundError, json.JSONDecodeError, NameError, IOError):
            pass
