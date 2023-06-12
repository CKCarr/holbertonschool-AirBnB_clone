#!/usr/bin/python3

"""
This module write the subclass Review
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    The Review class is a subclass of BaseModel.
    """
    place_id = ""
    user_id = ""
    text = ""
