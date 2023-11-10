#!/usr/bin/python3
"""
This module defines a class State
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    class State that inherits from BaseModel
    Public class attributes:
        name: string - empty string
    """
    def __init__(self, *args, **kwargs):
        """
        method that initiates new object
        """
        super().__init__(*args, **kwargs)
        self.name = ""
