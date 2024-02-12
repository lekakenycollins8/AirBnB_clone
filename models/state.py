#!/usr/bin/python3
"""class State that inherits from BaseModel"""


from models.base_model import BaseModel


class State(BaseModel):
    """manages user's state
    Attributes:
        name: empty string for state
    """
    name = ""
