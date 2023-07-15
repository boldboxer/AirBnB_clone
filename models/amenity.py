#!/usr/bin/python3
"""
Defines amenities class inherited from the base_model
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Defines amenities that user can choose from to offer at its place"""
    name = ""
