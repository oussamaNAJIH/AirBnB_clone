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
    state_id = ""
    name = ""
