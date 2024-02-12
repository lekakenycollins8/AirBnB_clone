#!/usr/bin/python3
""" City test cases"""


import unittest
from models.city import City  # Import your City class


class TestCity(unittest.TestCase):

    def setUp(self):
        # Create a sample City instance for testing
        self.city = City()

    def test_attributes(self):
        # Test if the City instance has the proper attributes
        self.assertTrue(hasattr(self.city, 'id'))
        self.assertTrue(hasattr(self.city, 'created_at'))
        self.assertTrue(hasattr(self.city, 'updated_at'))
        self.assertTrue(hasattr(self.city, 'state_id'))
        self.assertTrue(hasattr(self.city, 'name'))

    def test_default_values(self):
        # Test if the default values of attributes are empty strings
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

    def test_str_representation(self):
        # Test if the __str__ method returns the expected string format
        expected_string = "[City] ({}) {}".format(self.city.id, self.city.__dict__)
        self.assertEqual(str(self.city), expected_string)

    def test_save_method_updates_updated_at(self):
        # Test if save method updates the updated_at attribute
        old_updated_at = self.city.updated_at
        self.city.save()
        self.assertNotEqual(old_updated_at, self.city.updated_at)
