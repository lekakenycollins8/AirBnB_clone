#!/usr/bin/python3
"""module for class BaseModel test cases"""


import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        # Create a sample BaseModel instance for testing
        self.base_model = BaseModel()

    def test_init(self):
        # Test if the instance is created with proper default values
        self.assertIsNotNone(self.base_model.id)
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_save(self):
        # Test if save method updates updated_at attribute
        old_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(old_updated_at, self.base_model.updated_at)

    def test_to_dict(self):
        # Test if to_dict method returns dictionary with proper keys and values
        obj_dict = self.base_model.to_dict()
        self.assertIn('__class__', obj_dict)
        self.assertIn('id', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertIsInstance(obj_dict['created_at'], str)
        self.assertIsInstance(obj_dict['updated_at'], str)

    def test_str(self):
        # Test if __str__ method returns expected string format
        expected_string = "[BaseModel] ({}) {}".format(self.base_model.id, self.base_model.__dict__)
        self.assertEqual(str(self.base_model), expected_string)


if __name__ == '__main__':
    unittest.main()
