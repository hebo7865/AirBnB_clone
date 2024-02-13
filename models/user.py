#!/usr/bin/python3
"""My Class."""

from .base_model import BaseModel


class User(BaseModel):
    """User Class."""

    first_name = ""
    last_name = ""
    email = ""
    password = ""
