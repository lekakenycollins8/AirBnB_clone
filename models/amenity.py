#!/usr/bin/python3
"""class Amenity that inheits from BaseModel"""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """represents user's amenity
    Attributes:
        public class attributes:
            name: empty string for amenity name
    """
    name = ""
