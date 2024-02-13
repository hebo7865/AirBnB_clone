#!/usr/bin/python3
"""My Class."""

import json
from ..base_model import BaseModel
from ..user import User
from ..amenity import Amenity
from ..city import City
from ..place import Place
from ..state import State
from ..review import Review


class FileStorage:
    """Storage Class."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """To return all objects."""
        return FileStorage.__objects

    def new(self, obj):
        """To add new object to dictionary."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """To save object into file.json."""
        objs = {}
        for key, value in FileStorage.__objects.items():
            objs[key] = value.to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(objs, file, indent=4)

    def reload(self):
        """To get objects from file.json."""
        try:
            with open(self.__file_path, "r") as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name = value["__class__"]
                    del value["__class__"]
                    class_obj = eval(class_name)
                    self.new(class_obj(**value))
        except Exception:
            pass
