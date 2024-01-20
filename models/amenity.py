# models/amenity.py
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class for the HBNB project."""
    name = ""

    def __str__(self):
        """Return the string representation of the Amenity instance."""
        return "[Amenity] ({}) {}".format(self.id, self.__dict__)

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = super().to_dict()
        return dictionary
