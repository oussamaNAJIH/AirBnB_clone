#!/usr/bin/python3
"""
This module defines a class User
"""
import models
import uuid
from datetime import datetime
from models.base_model import BaseModel


class User(BaseModel):
    """
    class User that inherits from BaseModel
    Public instance attributes:
        email: string - empty string
        password: string - empty string
        first_name: string - empty string
        last_name: string - empty string
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
