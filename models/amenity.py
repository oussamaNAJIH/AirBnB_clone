#!/usr/bin/python3
"""
This module defines a class Amenity
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    class Amenity that inherits from BaseModel
    Public class attributes:
        name: string - empty string
    """
    def __init__(self, *args, **kwargs):
        """
        method that initiates new object
        """
        super().__init__(*args, **kwargs)
        self.name = ""
