#!/usr/bin/python3
"""A class amenity that inherits from the BaseModel"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class that inherits from BaseModel"""

    def __init__(self, *args, **kwargs):
        """Initialize Amenity instance"""

        super().__init__(*args, **kwargs)
        self.name = kwargs.get('name', '')
