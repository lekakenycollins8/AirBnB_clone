#!/usr/bin/python3
"""class City that inherits from BaseModel"""


from models.base_model import BaseModel


class City(BaseModel):
    """manages user's city
    Attributes:
        public class attributes:
            state_id: empty string for state id
            name: name of the city
    """
    state_id = ""
    name = ""
