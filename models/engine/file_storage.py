#!/usr/bin/python3
"""My Class."""

import json
from datetime import datetime


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
        self.__objects[key] = obj.__dict__

    def save(self):
        """To save object into file.json."""
        for key, value in FileStorage.__objects.items():
            for i, j in value.items():
                if i in ["created_at", "updated_at"]:
                    value[i] = value[i].isoformat()
        with open(self.__file_path, "w") as file:
            json.dump(FileStorage.__objects, file)

    def reload(self):
        """To get objects from file.json."""
        try:
            with open(self.__file_path, "r") as file:
                data = json.load(file)
                for i in data.values():
                    i["created_at"] = datetime.fromisoformat(i["created_at"])
                    i["updated_at"] = datetime.fromisoformat(i["updated_at"])
            FileStorage.__objects = data
        except Exception:
            pass
