# models/review.py
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class for the HBNB project."""
    place_id = ""
    user_id = ""
    text = ""
