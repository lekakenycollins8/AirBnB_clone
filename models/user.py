#!/usr/bin/python3
"""User class that inherits from base class"""


from models.base_model import BaseModel


class User(BaseModel):
    """manages user's identity
    Attributes:
        public class attributes:
            email: string of user's email
            password: string of user's password
            first_name: string of user's first name
            last_name: string of user's last_name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
