# models/user.py
from models.base_model import BaseModel

class User(BaseModel):
    """User class for the HBNB project."""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
