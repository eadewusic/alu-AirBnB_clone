from models.engine.file_storage import FileStorage

# Define BaseModel first.
from models.base_model import BaseModel

# Ensure that the storage instance is created after the BaseModel class has been defined.
storage = FileStorage()
storage.reload()
