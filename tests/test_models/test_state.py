#!/usr/bin/python3
"""Unittest module for the class State"""


import unittest
from models.state import State
from datetime import datetime
import json


class TestState(unittest.TestCase):
    """Represent the class to test class State"""

    def setUp(self):
        """Setting up"""
        self.new = State()

    def tearDown(self):
        """Cleaning up after each test"""
        del self.new

    def test_default_attributes(self):
        """Test if the default attributes are set correctly."""

        self.assertEqual(self.state.name, '')

    def test_setting_attributes(self):
        """Test setting attributes of a State instance."""

        self.state.name = "Lagos"
        self.assertEqual(self.state.name, "Lagos")

    def test_to_dict(self):
        """Test the to_dict() method of State."""

        state_dict = self.state.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertEqual(state_dict['__class__'], 'State')
        self.assertTrue('id' in state_dict)
        self.assertTrue('created_at' in state_dict)
        self.assertTrue('updated_at' in state_dict)
        self.assertTrue('name' in state_dict)

    def test_str_rep(self):
        """Test the __str__() representation of State."""

        expected_str = "[State] ({}) {}".format(self.state.id,
                                                self.state.__dict__)
        self.assertEqual(str(self.state), expected_str)

    def test_instance_creation(self):
        """Test creating a State instance with parameters."""

        state = State(name="Port Harcourt")
        self.assertEqual(state.name, "Port Harcourt")

    def test_invalid_attribute_types(self):
        """Test setting invalid attribute types."""

        with self.assertRaises(TypeError):
            self.state.name = 123

    def test_state_attributes(self):
        state = State()
        self.assertEqual(state.name, '')

    def test_is_instance(self):
        """Check if an instance belongs to class State"""
        self.assertIsInstance(self.new, State)

    def test_if_str(self):
        """Check if the attribute is str"""
        self.assertIsInstance(self.new.name, str)


if __name__ == '__main__':
    unittest.main()
