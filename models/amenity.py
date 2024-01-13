# models/amenity.py
from models.base_model import BaseModel

class Amenity(BaseModel):
    """
    Amenity class for the HBNB project.

    Attributes:
        name (str): The name of the amenity.
    """
    def __init__(self, *args, **kwargs):
        """Initialize Amenity instance."""
        super().__init__(*args, **kwargs)
        self.name = ""
