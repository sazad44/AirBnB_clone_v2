#!/usr/bin/python3
"""This is the file storage class for AirBnB"""
import json
from models.base_model import BaseModel
from models.place import Place
from models.city import City
from models.state import State
from models.review import Review
from models.user import User


class FileStorage:
    """This class serializes instances to a JSON file and
    deserializes JSON file to instances
    Attributes:
        __file_path: path to the JSON file
        __objects: objects will be stored
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """returns a dictionary
        Return:
            returns a dictionary of __object
        """
        if type(cls) != str and cls:
            cls = cls.__name__
        elif cls is None:
            return self.__objects
        retdict = {}
        for key in self.__objects.keys():
            if cls in key:
                retdict[key] = self.__objects[key]
        return retdict

    def new(self, obj):
        """sets __object to given obj
        Args:
            obj: given object
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """serialize the file path to JSON file path
        """
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(my_dict, f)

    def reload(self):
        """serialize the file path to JSON file path
        """
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """delete object provided"""
        if obj is None:
            return
        key = "{}.{}".format(type(obj).__name__, obj.id)
        if key in self.__objects.keys():
            del self.__objects[key]

    def close(self):
        """reload before exiting the session"""
        self.reload()
