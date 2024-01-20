#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
from models import base_model, user, place, state, city, amenity, review
import inspect
import json
import sys


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns a dictionary of models currently in storage"""
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.all().update({key: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            json.dump({k: v.to_dict() for k, v in FileStorage.__objects.items()}, f)

    def reload(self):
        """Loads storage dictionary from file"""
        classes = {cls.__name__: cls for name, cls in inspect.getmembers(
            sys.modules[__name__], inspect.isclass)}

        try:
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    class_name = val.get('__class__')
                    if class_name and class_name in classes:
                        self.all()[key] = classes[class_name](**val)
                    else:
                        print("Class not found:", class_name)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print("Error loading file:", e)
            # Handle the error accordingly (raise, log, etc.)
            pass
