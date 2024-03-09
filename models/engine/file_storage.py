#!/usr/bin/python3
"""Defines the storage engine with the class FileStorage that stores all valuesDefines the storage engine with the class FileStorage that stores all values
"""

import json
import os

class FileStorage:
    """
    serializes instances to a JSON file and deserializes JSON file to instances:serializes\
    instances to a JSON file and deserializes JSON file to instances.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects.
        """

        return (FileStorage.__objects)

    def new(self, obj):
        """"""

        key = f"{obj['__class__']}.{obj['id']}"
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file
        """

        #print(FileStorage.__objects)

        with open(FileStorage.__file_path, 'w') as file:
            json.dump(FileStorage.__objects, file)

    def reload(self):
        """Deserializes the JSON file to __objects."""

        try:
            with open(FileStorage.__file_path, 'r') as file:
                info = json.loads(file)
                FileStorage.__objects = info
        except FileNotFoundError:
            pass

