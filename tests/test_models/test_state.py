#!/usr/bin/python3
"""Module for State test cases"""


import unittest
from models.state import State  # Import your State class


class TestState(unittest.TestCase):

    def setUp(self):
        # Create a sample State instance for testing
        self.state = State()

    def test_attributes(self):
        # Test if the State instance has the proper attributes
        self.assertTrue(hasattr(self.state, 'id'))
        self.assertTrue(hasattr(self.state, 'created_at'))
        self.assertTrue(hasattr(self.state, 'updated_at'))
        self.assertTrue(hasattr(self.state, 'name'))

    def test_name_default_value(self):
        # Test if the default value of name attribute is an empty string
        self.assertEqual(self.state.name, "")

    def test_str_representation(self):
        # Test if the __str__ method returns the expected string format
        expected_string = "[State] ({}) {}".format(self.state.id, self.state.__dict__)
        self.assertEqual(str(self.state), expected_string)

    def test_to_dict_method(self):
        # Test if to_dict method returns dictionary with proper keys and values
        obj_dict = self.state.to_dict()
        self.assertIn('__class__', obj_dict)
        self.assertIn('id', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)
        self.assertEqual(obj_dict['__class__'], 'State')

    def test_save_method_updates_updated_at(self):
        # Test if save method updates the updated_at attribute
        old_updated_at = self.state.updated_at
        self.state.save()
        self.assertNotEqual(old_updated_at, self.state.updated_at)


if __name__ == '__main__':
    unittest.main()
