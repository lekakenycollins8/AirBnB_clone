#!/usr/bin/python3
"""class Review that inheits from BaseModel"""


from models.base_model import BaseModel


class Review(BaseModel):
    """manages user's review
    Attributes:
        public class attributes:
            place_id: string - empty string: it will be the Place.id
            user_id: string - empty string: it will be the User.id
            text: string - empty string
    """
    place_id = ""
    user_id = ""
    text = ""
