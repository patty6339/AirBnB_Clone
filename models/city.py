#!/usr/bin/python3
"""This module contains City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City.

    Class that inherits from BaseModel.
        Attributes:
            state_id (str): The ID of the state,
            name (str): The name of the city
    """

    state_id = ""
    name = ""
