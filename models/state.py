#!/usr/bin/python3
""" This module contains State class"""
from models.base_model import BaseModel


class State(BaseModel):
    """
        State class that inherits from BaseModel
            Attributes:
                name (str): The name of the state
    """
    name = ""
