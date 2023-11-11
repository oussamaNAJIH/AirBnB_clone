#!/usr/bin/python3
"""
 This module defines a class BaseModel.
"""
import models
import uuid
from datetime import datetime


class BaseModel:
    """s
    Public instance attributes:
        id: an UUID when an instance is created
        created_at: the current datetime when an instance is created
        updated_at: the current datetime when an instance is created
        and it will be updated every time you change your object

    Public instance methods:
        save
        to_dict
    """
    def __init__(self, *args, **kwargs):
        """
        initiates objects
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)
        if not kwargs:
            models.storage.new(self)

    def __str__(self):
        """
        Return: a string representation of the instance.
        """
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates updated_at with the current datetime.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all
        keys/values of __dict__ of the instance.
        """
        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = type(self).__name__
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        return dict_copy
