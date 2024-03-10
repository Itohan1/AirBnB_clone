#!/usr/bin/python3
""" Module that test all class, function and instances of the BaseModel"""


import unittest
from models.base_model import BaseModel
from models.__init__ import storage
from datetime import datetime
import os


class TestBaseModel(unittest.TestCase):
    """ Test cases for the BaseModel"""

    def setUp(self):
        """   """

        self.model = BaseModel()

    def tearDown(self):
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_init(self):
        """ Test initialization of BaseModel"""

        self.assertIsNotNone(self.model.id)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    
    def test_str(self):
        """Test string representation of BaseModel."""
        
        base_model = BaseModel()
        expected = f"[BaseModel] ({self.model.id}) {self.model.__dict__}"
        self.assertEqual(str(self.model), expected)
        
    def test_save(self):
        """ Test the saveing function of the BaseModel"""

        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(self.model.updated_at, old_updated_at)

    
    def test_to_dict(self):
        """ Test the conversion to dictionary object"""

        instance_dict = self.model.to_dict()
        self.assertIn('__class__', instance_dict)
        self.assertIn('created_at', instance_dict)
        self.assertIn('updated_at', instance_dict)
        self.assertIn('id', instance_dict) 

    
    def test_storage(self):
        """  Test the storage of the BaseModel"""

        self.assertIsInstance(storage.all(), dict)
        self.assertIn(f"BaseModel.{self.model.id}", storage.all())
