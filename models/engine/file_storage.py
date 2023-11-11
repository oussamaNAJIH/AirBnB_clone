#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances
    Private class attributes:
        __file_path
        __objects
    Public instance methods:
        all(self)
        new(self, obj)
        save(self)
        reload(self)
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file
        """
        with open(self.__file_path, 'w') as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        """
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    cls_name, obj_id = key.split(".")
                    if cls_name == "User":
                        self.__objects[key] = User(**value)
                    elif cls_name == "Place":
                        self.__objects[key] = Place(**value)
                    elif cls_name == "State":
                        self.__objects[key] = State(**value)
                    elif cls_name == "City":
                        self.__objects[key] = City(**value)
                    elif cls_name == "Amenity":
                        self.__objects[key] = Amenity(**value)
                    elif cls_name == "Review":
                        self.__objects[key] = Review(**value)
                    elif cls_name == "BaseModel":
                        self.__objects[key] = BaseModel(**value)
        except FileNotFoundError:
            pass
