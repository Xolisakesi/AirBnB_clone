#!/usr/bin/python3

import unittest
from models.user import User

class TestUser(unittest.TestCase):
    def test_instance_attributes(self):
        user = User()
        self.assertTrue(hasattr(user, 'email'))
        self.assertTrue(hasattr(user, 'password'))
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertTrue(hasattr(user, 'last_name'))

    def test_default_values(self):
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_custom_values(self):
        user = User(email="test@example.com", password="password123", first_name="John", last_name="Doe")
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.password, "password123")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")

    def test_to_dict_method(self):
        user = User(email="test@example.com", password="password123", first_name="John", last_name="Doe")
        user_dict = user.to_dict()
        self.assertTrue(isinstance(user_dict, dict))
        self.assertEqual(user_dict['__class__'], 'User')

if __name__ == '__main__':
    unittest.main()

