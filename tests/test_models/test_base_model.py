#!/usr/bin/python3
""" Test module for BaseModel """
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import storage
import os
import time
import unittest


class TestBaseModel(unittest.TestCase):
    """ Test cases for BaseModel class """

    def test_instance_creation(self):
        """ Test if a BaseModel instance is created successfully """
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)
        self.assertTrue(hasattr(my_model, 'id'))
        self.assertTrue(hasattr(my_model, 'created_at'))
        self.assertTrue(hasattr(my_model, 'updated_at'))

    def test_attributes_types(self):
        """ Test if attributes have the correct types """
        my_model = BaseModel()
        self.assertIsInstance(my_model.id, str)
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)

    def test_save_method(self):
        """ Test if save method updates the updated_at attribute """
        my_model = BaseModel()
        original_updated_at = my_model.updated_at
        time.sleep(1)  # Introduce a delay of 1 second
        my_model.save()
        self.assertGreater(my_model.updated_at, original_updated_at)

    def test_to_dict_method(self):
        """Test if to_dict method returns the
        correct dictionary representation"""
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()

        expected_keys = [
            'id',
            'created_at',
            'updated_at',
            'name',
            'my_number',
            '__class__'
        ]
        self.assertCountEqual(my_model_json.keys(), expected_keys)
        self.assertEqual(my_model_json['__class__'], 'BaseModel')
        self.assertEqual(my_model_json['name'], "My_First_Model")
        self.assertEqual(my_model_json['my_number'], 89)

    def test_str_method(self):
        """ Test if __str__ method returns the
        correct string representation """
        my_model = BaseModel()
        string_representation = str(my_model)
        class_name = my_model.__class__.__name__
        self.assertIn(class_name, string_representation)
        self.assertIn(my_model.id, string_representation)
        self.assertIn(str(my_model.__dict__), string_representation)

    def test_instance_recreation(self):
        """ Test if a new instance can be recreated
        from a dictionary representation """
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()

        my_new_model = BaseModel(**my_model_json)
        self.assertEqual(my_model.id, my_new_model.id)
        self.assertEqual(
            my_model.created_at.timestamp(),
            my_new_model.created_at.timestamp()
        )
        self.assertEqual(
            my_model.updated_at.timestamp(),
            my_new_model.updated_at.timestamp()
        )
        self.assertEqual(my_model.name, my_new_model.name)
        self.assertEqual(my_model.my_number, my_new_model.my_number)

    def test_unique_id(self):
        """ Test if the id attribute is unique for each instance """
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model1.id, model2.id)


if __name__ == '__main__':
    unittest.main()