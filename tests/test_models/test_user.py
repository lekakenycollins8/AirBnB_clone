#!/usr/bin/python3


import unittest
from models.user import User  # Import your User class


class TestUser(unittest.TestCase):

    def setUp(self):
        # Create a sample User instance for testing
        self.user = User()

    def test_attributes(self):
        # Test if the User instance has the proper attributes
        self.assertTrue(hasattr(self.user, 'id'))
        self.assertTrue(hasattr(self.user, 'created_at'))
        self.assertTrue(hasattr(self.user, 'updated_at'))
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertTrue(hasattr(self.user, 'last_name'))

    def test_default_values(self):
        # Test if the default values of attributes are empty strings
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_str_representation(self):
        # Test if the __str__ method returns the expected string format
        expected_string = "[User] ({}) {}".format(self.user.id, self.user.__dict__)
        self.assertEqual(str(self.user), expected_string)

    def test_save_method_updates_updated_at(self):
        # Test if save method updates the updated_at attribute
        old_updated_at = self.user.updated_at
        self.user.save()
        self.assertNotEqual(old_updated_at, self.user.updated_at)
    

if __name__ == '__main__':
    unittest.main()
