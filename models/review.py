# models/review.py
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class for the HBNB project."""
    place_id = ""
    user_id = ""
    text = ""

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = super().to_dict()
        return dictionary
