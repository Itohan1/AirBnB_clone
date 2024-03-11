#!/usr/bin/python3
"""A unittests for models/user.py"""

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Unittests class for the user"""

    def setUp(self):
        """Set up User instance for tests"""
        self.instance = User()

    def test_init_attributes(self):
        """Check init attribute values"""

        email = self.instance.email
        password = self.instance.password
        first_name = self.instance.first_name
        last_name = self.instance.last_name

        self.assertEqual(email, "")
        self.assertEqual(password, "")
        self.assertEqual(first_name, "")
        self.assertEqual(last_name, "")

    def test_set_attributes(self):
        """Check for correct attribute values once set"""

        self.instance.email = "belloamadi@gmail.com"
        self.instance.password = "123"
        self.instance.first_name = "John"
        self.instance.last_name = "Adam"

        self.assertEqual(self.instance.email, "belloamadi@gmail.com")
        self.assertEqual(self.instance.password, "123")
        self.assertEqual(self.instance.first_name, "John")
        self.assertEqual(self.instance.last_name, "Adam")


if __name__ == "__main__":
    unittest.main()
