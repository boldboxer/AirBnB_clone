#!/usr/bin/python3
"""
A User class that inherits from BaseModel
===> User creation class
"""

from models.base_model import BaseModel


class User(BaseModel):
    """ Defines public class attributes """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
