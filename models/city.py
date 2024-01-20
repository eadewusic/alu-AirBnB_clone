# models/city.py
from models.base_model import BaseModel


class City(BaseModel):
    """City class for the HBNB project."""
    state_id = ""
    name = ""

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = super().to_dict()
        return dictionary
