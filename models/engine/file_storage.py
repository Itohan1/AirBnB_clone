#!/usr/bin/python3
"""Defines the storage engine with the class FileStorage that stores all\
        valuesDefines the storage engine with the class\
        FileStorage that stores all values
"""
import json
import os


class FileStorage:
    """
    serializes instances to a JSON file and\
        deserializes JSON file to instances.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects.
        """

        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj With key <obj class name>.id."""

        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj.to_dict()

    def save(self):
        """Serializes __objects to the JSON file
        """

        with open(FileStorage.__file_path, 'w') as path:
            json.dump(FileStorage.__objects, path)

    def reload(self):
        """Deserializes the JSON file to __objects."""

        try:
            with open(FileStorage.__file_path, 'r') as file:
                FileStorage.__objects = json.load(file)
        except FileNotFoundError:
             pass
