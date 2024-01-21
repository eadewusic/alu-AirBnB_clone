import unittest
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def test_all_method(self):
        storage = FileStorage()
        objects = storage.all()
        self.assertIsInstance(objects, dict)
        # Add more test cases specific to the FileStorage model

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


if __name__ == '__main__':
    unittest.main()
