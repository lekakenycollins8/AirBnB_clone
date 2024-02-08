#!/usr/bin/python3
"""class State that inherits from BaseModel"""


from models.base_model import BaseModel


class State(BaseModel):
    """manages user's state
    Attributes:
        name: empty string for state
    """
    name = ""
    def __init__(self):
        """instatiation of inherited attributes"""
        super().__init__(id, created_at, updated_at)

