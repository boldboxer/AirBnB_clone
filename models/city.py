#!/usr/bin/python3
"""
Defines city class inherited from the base_model
"""
from models.base_model import BaseModel


class City(BaseModel):
    """defines city to look for"""
    state_id = ""
    name = ""
