#!/usr/bin/python3
"""Unit tests for project objs."""

import unittest

from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.city import City
from models.review import Review
from models.state import State


class TestObjs(unittest.TestCase):
    """Test for objs."""

    def test_BaseModel_type(self):
        """Test type for BaseModel Objs."""
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_User_type(self):
        """Test type for User Objs."""
        self.assertEqual(User, type(User()))

    def test_Amenity_type(self):
        """Test type for Amenity Objs."""
        self.assertEqual(Amenity, type(Amenity()))

    def test_Place_type(self):
        """Test type for Place Objs."""
        self.assertEqual(Place, type(Place()))

    def test_City_type(self):
        """Test type for City Objs."""
        self.assertEqual(City, type(City()))

    def test_Review_type(self):
        """Test type for Review Objs."""
        self.assertEqual(Review, type(Review()))

    def test_State_type(self):
        """Test type for State Objs."""
        self.assertEqual(State, type(State()))
