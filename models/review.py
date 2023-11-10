#!/usr/bin/python3
"""
This module defines a class Review
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    class Review that inherits from BaseModel
    Public class attributes:
        place_id: string - empty string: it will be the Place.id
        user_id: string - empty string: it will be the User.id
        text: string - empty string
    """
    def __init__(self, *args, **kwargs):
        """
        method that initiates new object
        """
        super().__init__(*args, **kwargs)
        self.place_id = ""
        self.user_id = ""
        self.text = ""
