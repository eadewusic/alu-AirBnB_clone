#!/usr/bin/python3
"""
User class that inherits from BaseModel.
"""

from models.base_model import BaseModel

class User(BaseModel):
    """User class for the HBNB project."""
    email = None
    password = None
    first_name = None
    last_name = None
