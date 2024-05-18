#!/usr/bin/python3
"""
Serializer.

This module defines a class that serializes
instances to a JSON file and deserializes
JSON files back to instances.
"""
# imports
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage:
    """
    Storage.

    Class for file storage.
    """

    __file_path = "file.json"
    """path to the JSON file"""

    __objects = {}
    """Stores all basemodel objects"""

    def all(self):
        """
        All.

        Returns a dictionary of all objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Create.

        Sets in the obj with key <obj class name>.id in __objects

        Args:
            obj (BaseModel): Object to be added
        """
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """
        Save.

        Serializes __objects to the JSON file (path: __file_path)
        """
        temp_dictionary = self.__objects
        object_dictionary = {
            obj: temp_dictionary[obj].to_dict()
            for obj in temp_dictionary.keys()}
        with open(self.__file_path, "w") as file:
            json.dump(object_dictionary, file)

    def reload(self):
        """
        Reload.

        Deserializes the JSON file to __objects
        (only if the JSON file exists)
        """
        try:
            with open(self.__file_path, "r") as file:
                obj_dict = json.load(file)
                for o in obj_dict.values():
                    class_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(class_name)(**o))
        except FileNotFoundError:
            return
