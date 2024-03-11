#!/usr/bin/python3
"""Uniitest module for models/amenity"""


import unittest
from models.amenity import Amenity
import json


class TestAmenity(unittest.TestCase):
    """Test case for the class Amenity"""

    def setUp(self):
        """Set up a new Amenity instance for each test"""
        self.new = Amenity()

    def tearDown(self):
        """Cleaning up after each test"""
        del self.new

    def test_amenity_attributes(self):
        """Check the attributes"""

        amenity = Amenity()
        self.assertEqual(amenity.name, '')

    def test_is_instance(self):
        """Check if attributes are of a correct type"""
        self.assertIsInstance(self.new, Amenity)

    def test_if_str(self):
        """Check if the attribute is str"""
        self.assertIsInstance(self.new.name, str)

    def test_default_attributes(self):
        """Test if the default attributes are set correctly."""
        self.assertEqual(self.amenity.name, '')

    def test_setting_attributes(self):
        """Test setting attributes of an Amenity instance."""
        self.amenity.name = "Wifi"
        self.assertEqual(self.amenity.name, "Wifi")

    def test_to_dict(self):
        """Test the to_dict() method of Amenity."""
        amenity_dict = self.amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict)
        self.assertEqual(amenity_dict['__class__'], 'Amenity')
        self.assertTrue('id' in amenity_dict)
        self.assertTrue('created_at' in amenity_dict)
        self.assertTrue('updated_at' in amenity_dict)
        self.assertTrue('name' in amenity_dict)

    def test_str_rep(self):
        """Test the __str__() representation of Amenity."""
        expected_str = "[Amenity] ({}) {}".format(self.amenity.id,
                                                  self.amenity.__dict__)
        self.assertEqual(str(self.amenity), expected_str)

    def test_instance_creation(self):
        """Test creating an Amenity instance with parameters."""
        amenity = Amenity(name="Pool")
        self.assertEqual(amenity.name, "Pool")

    def test_invalid_attribute_types(self):
        """Test setting invalid attribute types."""
        with self.assertRaises(TypeError):
            self.amenity.name = 123


if __name__ == '__main__':
    unittest.main()
