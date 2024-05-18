#!/usr/bin/python3
"""This module contains Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class that inherits from BaseModel.

    Attributes:
        place_id (str): The ID of the place
        user_id (str): The ID of the user
        text (str): The review text
    """

    place_id = ""
    user_id = ""
    text = ""
