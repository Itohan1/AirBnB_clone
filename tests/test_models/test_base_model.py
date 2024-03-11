#!/usr/bin/python3
""" Module that test all class, function and instances of the BaseModel"""


import unittest
from models.base_model import BaseModel
from datetime import datetime
import os
import uuid
from models import storage


class TestBaseModel(unittest.TestCase):
    """ Test cases for the BaseModel"""

    def test_attributes(self):
        """ Test BaseModel attrributes"""

        base_model = BaseModel()
        self.assertTrue(hasattr(base_model, 'id'))
        self.assertIsInstance(base_model.id, str)

        self.assertTrue(hasattr(base_model, 'created_at'))
        self.assertIsInstance(base_model.created_at, datetime)
        self.assertTrue(hasattr(base_model, 'updated_at'))
        self.assertIsInstance(base_model.updated_at, datetime)

    def test_init(self):
        """ Test initialization of BaseModel"""

        base_model = BaseModel()
        self.assertIsNotNone(base_model.id)
        self.assertIsInstance(base_model.created_at, datetime)
        self.assertIsInstance(base_model.updated_at, datetime)

    def test_str(self):
        """Test string representation of BaseModel."""

        base_model = BaseModel()
        expected = f"[BaseModel] ({base_model.id}) {base_model.__dict__}"
        self.assertEqual(str(base_model), expected)

    def test_save(self):
        """ Test the saveing function of the BaseModel"""

        base_model = BaseModel()
        old_updated_at = base_model.updated_at
        base_model.save()
        self.assertNotEqual(base_model.updated_at, old_updated_at)

    def test_to_dict(self):
        """ Test the conversion to dictionary object"""

        base_model = BaseModel()

        instance_dict = base_model.to_dict()
        self.assertIn('__class__', instance_dict)
        self.assertIn('created_at', instance_dict)
        self.assertIn('updated_at', instance_dict)
        self.assertIn('id', instance_dict)

    def test_storage(self):
        """  Test the storage of the BaseModel"""

        self.assertIsInstance(storage.all(), dict)
        self.assertIn(f"BaseModel.{base_model.id}", storage.all())

    def test_uuid_format(self):
        """ Test that id is a valid UUID"""
        base_model = BaseModel()
        try:
            uuid.UUID(base_model.id, version=4)
        except ValueError:
            self.fail("Invalid UUID format for id")


if __name__ == '__main__':
    unittest.main()
