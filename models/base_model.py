#!/usr/bin/env python3
"""Write a class BaseModel"""

from models.__init__ import storage
from datetime import datetime
import uuid


class BaseModel:
    """Public instance attributes id created_at, updated_at"""

    def __init__(self, *args, **kwargs):
        """"""

        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'created_at' or key == 'updated_at':
                    if isinstance(value, datetime):
                        value = value.isoformat()
                        v = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, v)
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self.to_dict())

    def __str__(self):
        """"""

        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """"""

        self.updated_at = datetime.now()
        storage.new(self.to_dict())
        storage.save()

    def to_dict(self):
        """"""

        instance_dict_ = self.__dict__.copy()
        instance_dict_['__class__'] = self.__class__.__name__
        instance_dict_['created_at'] = self.created_at.isoformat()
        instance_dict_['updated_at'] = self.updated_at.isoformat()

        return (instance_dict_)