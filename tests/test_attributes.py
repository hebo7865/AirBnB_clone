#!/usr/bin/python3
"""Unit tests for project objs."""

import unittest

from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.city import City
from models.review import Review
from models.state import State


class TestObjs(unittest.TestCase):
    """Test for objs."""

    def test_BaseModel_attribute(self):
        """Test attribute for BaseModel Objs."""
        self.assertEqual(datetime, type(BaseModel().created_at))
        self.assertEqual(str, type(BaseModel().id))

    def test_User_attribute(self):
        """Test attribute for User Objs."""
        self.assertEqual(datetime, type(User().created_at))
        self.assertEqual(str, type(User().id))

    def test_Amenity_attribute(self):
        """Test attribute for Amenity Objs."""
        self.assertEqual(datetime, type(Amenity().created_at))
        self.assertEqual(str, type(Amenity().id))

    def test_Place_attribute(self):
        """Test attribute for Place Objs."""
        self.assertEqual(datetime, type(Place().created_at))
        self.assertEqual(str, type(Place().id))

    def test_City_attribute(self):
        """Test attribute for City Objs."""
        self.assertEqual(datetime, type(City().created_at))
        self.assertEqual(str, type(City().id))

    def test_Review_attribute(self):
        """Test attribute for Review Objs."""
        self.assertEqual(datetime, type(Review().created_at))
        self.assertEqual(str, type(Review().id))

    def test_State_attribute(self):
        """Test attribute for State Objs."""
        self.assertEqual(datetime, type(State().created_at))
        self.assertEqual(str, type(State().id))
