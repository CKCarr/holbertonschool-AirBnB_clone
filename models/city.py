#!/usr/bin/python3

"""
This module writes the subclass City
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    The City class is a subclass of BaseModel.
    """
    state_id = ""
    name = ""
