import json

class Storage:
    """Simple storage class for managing instances"""

    __file_path = "file.json"  # JSON file to save instances
    __objects = {}  # Dictionary to store instances

    def all(self):
        """Returns the dictionary of instances"""
        return self.__objects

    def new(self, obj):
        """Adds a new instance to the storage"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes and saves the instances to a JSON file"""
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Deserializes and reloads instances from a JSON file"""
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, obj_dict in data.items():
                    class_name, obj_id = key.split('.')
                    module = __import__("models." + class_name, fromlist=[class_name])
                    class_ = getattr(module, class_name)
                    instance = class_(**obj_dict)
                    self.__objects[key] = instance
        except FileNotFoundError:
            pass

# Creating a singleton instance of Storage
storage = Storage()
