#!/usr/bin/env python3
"""Write a class BaseModel that defines all common attributes/methods for other classes"""

from models.__init__ import storage
import datetime
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
                    if isinstance(value, datetime.datetime):
                        value = value.isoformat()
                    setattr(self, key, datetime.datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self.to_dict())

    def __str__(self):
        """"""

        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """"""

        self.updated_at = datetime.datetime.now()
        storage.new(self.to_dict())
        storage.save()

    def to_dict(self):
        """"""

        instance_dict_ = self.__dict__.copy()
        instance_dict_['__class__'] = self.__class__.__name__
        instance_dict_['created_at'] = self.created_at.isoformat()
        instance_dict_['updated_at'] = self.updated_at.isoformat()

        return (instance_dict_)
