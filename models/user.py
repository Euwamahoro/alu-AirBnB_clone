#!/usr/bin/python3

"""
    Define 'User' class
"""

from models.model import BaseModel

class User(BaseModel):
    """
    User class that inherits from BaseModel.
    Public class attributes:
        email: string - empty string
        password: string - empty string
        first_name: string - empty string
        last_name: string - empty string
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize User instance.
        """
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
