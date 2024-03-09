#!/usr/bin/env python3
""""""

import json
import os

class FileStorage:
    """"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """"""

        return (FileStorage.__objects)

    def new(self, obj):
        """"""

        key = f"{obj['__class__']}.{obj['id']}"
        FileStorage.__objects[key] = obj

    def save(self):
        """"""

        #print(FileStorage.__objects)

        with open(FileStorage.__file_path, 'w') as path:
            json.dump(FileStorage.__objects, path)

    def reload(self):
        """"""
        try:
            with open(FileStorage.__file_path, 'r') as path:
                info = json.loads(path.read())
                FileStorage.__objects = info
        except FileNotFoundError:
            pass

