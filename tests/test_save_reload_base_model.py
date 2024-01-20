#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models import storage


class TestSaveReloadBaseModel(unittest.TestCase):
    def create_and_save_model(self):
        # Create a new object
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        return my_model

    def test_save_reload_base_model(self):
        all_objs = storage.all()
        print("-- Reloaded objects --")
        for obj_id in all_objs.keys():
            obj = all_objs[obj_id]
            print(obj)


if __name__ == '__main__':
    unittest.main()
