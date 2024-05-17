#!/usr/bin/python3
"""
    Defines a class that serializes instances to a JSON file and
    deserializes JSON file to instances:
"""
# imports
import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """Class for file storage"""
    __file_path = "file.json"
    """path to the JSON file"""

    __objects = {}
    """Stores all basemodel objects"""

    def all(self):
        """Returns a dictionary of all objects"""
        return self.__objects

    def new(self, obj):
        """Sets in the obj with key <obj class name>.id in __objects

        Args:
            obj (BaseModel): Object to be added
        """
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """"Serializes __objects to the JSON file (path: __file_path)"""
        # Open file for writing and close automatically
        temp_dictionary = self.__objects
        object_dictionary = {
            obj: temp_dictionary[obj].to_dict()
            for obj in temp_dictionary.keys()}
        with open(self.__file_path, "w") as file:
            json.dump(object_dictionary, file)

    def reload(self):
        """Deserializes the JSON file to __objects if file exists"""
        try:
            with open(self.__file_path, "r") as file:
                obj_dict = json.load(file)
                for o in obj_dict.values():
                    class_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(class_name)(**o))
        except FileNotFoundError:
            return
