# models/user.py
"""
User class that inherits from BaseModel.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User class with public attributes:
    - email (string, empty string)
    - password (string, empty string)
    - first_name (string, empty string)
    - last_name (string, empty string)
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = super().to_dict()
        return dictionary
