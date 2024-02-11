#!/usr/bin/python3
"""My Class."""

from uuid import uuid4
from datetime import datetime
from time import sleep
import models


class BaseModel:
    """Base Class."""

    def __init__(self, *args, **kwargs):
        """Class Constructor."""
        if kwargs:
            self.id = kwargs["id"]
            self.created_at = kwargs["created_at"]
            self.updated_at = kwargs["updated_at"]
        else:
            time = datetime.now()
            self.id = str(uuid4())
            self.created_at = time
            self.updated_at = time
        models.storage.new(self)

    def save(self):
        """To save object into file.json."""
        self.updated_at = datetime.now()
        created, updated = self.created_at, self.updated_at
        models.storage.save()
        self.created_at = created
        self.updated_at = updated

    def to_dict(self):
        """To convert object into dictionary."""
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        return my_dict

    def __str__(self):
        """To representation."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
