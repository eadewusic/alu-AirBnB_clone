# models/state.py
from models.base_model import BaseModel


class State(BaseModel):
    """State class for the HBNB project."""
    name = ""

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = super().to_dict()
        return dictionary
