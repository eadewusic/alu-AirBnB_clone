#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
from datetime import datetime, timezone
import uuid
import json

class BaseModel:
    def __init__(self, *args, **kwargs):
        """Initialize BaseModel instance."""
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != '__class__':
                    setattr(self, key, value)
            if hasattr(self, 'created_at') and type(self.created_at) is datetime:
                pass
            else:
                self.created_at = datetime.now()
                self.updated_at = datetime.now()
            if not hasattr(self, 'id'):
                self.id = str(uuid.uuid4())

    def save(self, storage_instance):
        """Update the updated_at attribute and save the instance to storage."""
        self.updated_at = datetime.now()
        storage_instance.save()

    def to_dict(self):
        """Return a dictionary representation of the instance."""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

    def __str__(self):
        """Return the string representation of the instance."""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, str(self.__dict__))

    def recreate_instance(self, dictionary, class_reference):
        """Recreate a BaseModel instance from a dictionary representation."""
        instance = class_reference(**dictionary)
        return instance

    def delete(self):
        """Delete the current instance from storage."""
        from models import storage
        storage.delete(self)
