# models/__init__.py

from models.engine.file_storage import FileStorage

# Instantiate storage
storage = FileStorage()
storage.reload()

# Import model classes
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.review import Review

# Add model classes to __all__ for wildcard import
__all__ = ["BaseModel", "User", "Place", "City", "State", "Amenity", "Review"]
