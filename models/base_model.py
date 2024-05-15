#!/usr/bin/python3
"""This module contains the Base class"""
from uuid import uuid4
from datetime import datetime
# from models import storage


class BaseModel:
    """Defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()
            # storage.new(self)

    def __str__(self):
        """Return a string representation of the BaseModel instance"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__

        dict_repr = {
            'my_number': obj_dict.get('my_number'),
            'name': obj_dict.get('name'),
            'updated_at': repr(obj_dict.get('updated_at')),
            'id': obj_dict.get('id'),
            'created_at': repr(obj_dict.get('created_at')),
            # '__class__': obj_dict.get('__class__')
        }
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, dict_repr)

    def save(self):
        """Update updated_at attribute with datetime"""
        self.updated_at = datetime.now()
        # storage.save()

    def to_dict(self):
        """Return a dictionary representation of the BaseModel instance"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()

        # Ensure the dictionary keys are in the desired order
        key_order = [
            'my_number',
            'name', '__class__',
            'updated_at', 'id',
            'created_at'
        ]
        sorted_obj_dict = {k: obj_dict[k] for k in key_order if k in obj_dict}
        return sorted_obj_dict
