#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.user import User
from models import storage

class TestSaveReloadBaseModel(unittest.TestCase):
    def create_and_save_base_model(self):
        # Create a new BaseModel object with specific attribute values
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model.save()
        return my_model

    def create_and_save_user(self):
        # Create a new User object with specific attribute values
        my_user = User()
        my_user.email = "user@example.com"
        my_user.password = "secret"
        my_user.first_name = "John"
        my_user.last_name = "Doe"
        my_user.save()
        return my_user

    def test_save_reload_base_model(self):
        # Create and save a BaseModel with specific attribute values
        base_model = self.create_and_save_base_model()

        # Create and save a User with specific attribute values
        user = self.create_and_save_user()

        # Reload all objects and print them
        all_objs = storage.all()
        print("-- Reloaded objects --")
        for obj_id in all_objs.keys():
            obj = all_objs[obj_id]
            print(obj)

if __name__ == '__main__':
    unittest.main()
