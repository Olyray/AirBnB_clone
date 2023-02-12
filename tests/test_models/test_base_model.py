#!/usr/bin/python3
"""This is the unittest for the base model"""

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """ Things to test:
        1. Check whether ID is a string
        2. Whether ID is unique
        3. Check whether created_at and updated_at are datetime
        4. Check that str prints in correct format
        5. Check that they are strings
    """
    def test_id_string(self):
        """
        Check whether ID is a string
        """
        b1 = BaseModel()
        self.assertEqual(isinstance(b1.id, str), True)

    def test_id_unique(self):
        """
        Check whether ID is unique
        """
        first_model = BaseModel()
        second_model = BaseModel()
        self.assertNotEqual(first_model.id, second_model.id)

    def test_created_at_date_time(self):
        """
        Check whether created_at is a datetime object
        """
        third_model = BaseModel()
        self.assertEqual(isinstance(third_model.created_at, datetime), True)

    def test_updated_at_date_time(self):
        """
        Check whether updated_at is a datetime object
        """
        fourth_model = BaseModel()
        self.assertEqual(isinstance(fourth_model.updated_at, datetime), True)

    def test_created_at_is_string(self):
        """
        Check whether created_at is a string
        """
        fifth_model = BaseModel()
        my_dict = fifth_model.to_dict()
        self.assertEqual(isinstance(my_dict["created_at"], str), True)

    def test_updated_at_is_string(self):
        """
        Check whether updated at is a string
        """
        sixth_model = BaseModel()
        my_dict = sixth_model.to_dict()
        self.assertEqual(isinstance(my_dict["updated_at"], str), True)
