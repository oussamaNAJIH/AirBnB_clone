#!/usr/bin/python3
"""
This module defines a class City
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    class City that inherits from BaseModel
    Public class attributes:
        state_id: string - empty string: it will be the State.id
        name: string - empty string
    """
    def __init__(self, *args, **kwargs):
        """
        method that initiates new object
        """
        super().__init__(*args, **kwargs)
        self.state_id = ""
        self.name = ""
