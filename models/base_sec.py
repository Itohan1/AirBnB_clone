#!/usr/bin/python3
"""Write a class BaseModel"""


from models.__init__ import storage
from datetime import datetime
import uuid


class BaseModel:
    """Public instance attributes id created_at, updated_at"""

    def __init__(self, *args, **kwargs):
        """initializes the instance attributes"""

        if kwargs:

            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'created_at' or key == 'updated_at':
                    if isinstance(value, datetime):
                        value = value.isoformat()
                        self.__dict__[key] = datetime.strptime(
                                value, '%Y-%m-%dT%H:%M:%S.%f')

                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """returns a string representation of the object"""

        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """saves the updated value of datetime"""

        self.updated_at = datetime.now()
        #storage.new(self.to_dict())
        storage.save()

    def to_dict(self):
        """creates dictionary representation of objects"""

        instance_dict_ = self.__dict__.copy()
        instance_dict_['__class__'] = self.__class__.__name__
        instance_dict_['created_at'] = self.created_at.isoformat()
        instance_dict_['updated_at'] = self.updated_at.isoformat()

        return (instance_dict_)
