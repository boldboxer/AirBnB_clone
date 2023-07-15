#!/usr/bin/python3
"""
Defines review class inherited from base_model
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Reviews made by users about a place"""
    place_id = ""
    user_id = ""
    text = ""
