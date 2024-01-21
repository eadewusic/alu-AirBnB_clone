import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    def test_all_method(self):
        storage = FileStorage()
        objects = storage.all()
        self.assertIsInstance(objects, dict)
        # Add more assertions or specific test cases for the all() method

    def test_new_method(self):
        storage = FileStorage()

        # Create a dummy object to test the new method
        class DummyObject:
            def __init__(self, id):
                self.id = id

            def to_dict(self):
                return {'id': self.id, '__class__': type(self).__name__}

        dummy_instance = DummyObject(id='dummy_id')
        storage.new(dummy_instance)
        self.assertIn('DummyObject.dummy_id', storage.all())
        # Add more assertions or specific test cases for the new() method

    def test_save_and_reload_methods(self):
        storage = FileStorage()

        # Create a dummy object to test save and reload methods
        class DummyObject:
            def __init__(self, id):
                self.id = id

            def to_dict(self):
                return {'id': self.id, '__class__': type(self).__name__}

        dummy_instance = DummyObject(id='dummy_id')
        storage.new(dummy_instance)
        storage.save()

        # Create a new storage instance to test the reload method
        new_storage = FileStorage()
        new_storage.reload()
        self.assertIn('DummyObject.dummy_id', new_storage.all())
        # Add more assertions or specific test cases for save() and reload() methods

    def test_reload_nonexistent_file(self):
        # Test reloading from a nonexistent file
        storage = FileStorage()
        with self.assertRaises(FileNotFoundError):
            storage.reload()

    def test_reload_empty_file(self):
        # Test reloading from an empty file
        storage = FileStorage()
        with open(FileStorage.__file_path, 'w') as f:
            f.write('')
        storage.reload()
        self.assertEqual(len(storage.all()), 0)

    def test_save_method_with_BaseModel(self):
        storage = FileStorage()

        # Create a BaseModel instance to test the save() method
        base_model_instance = BaseModel()
        storage.new(base_model_instance)
        storage.save()

        # Create a new storage instance to test the reload method
        new_storage = FileStorage()
        new_storage.reload()
        self.assertIn(f'BaseModel.{base_model_instance.id}', new_storage.all())


if __name__ == '__main__':
    unittest.main()
