#!/usr/bin/python3
""" test_base_model module """
import unittest
import pycodestyle
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """
    TestBaseModel class
    """
    def test_pep(self):
        """ test pep """
        style = pycodestyle.StyleGuide(quiet=True)
        files = ['models/base_models',
                 'test/test_models/test_base_model']
        result = style.check_files(files)
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).)")

    def test_module_doc(self):
        """ test module documentation """
        doc = __import__('models.base_model').__doc__
        self.assertGreater(len(doc), 1)

    def test_class_doc(self):
        """ test class documentation """
        doc = BaseModel.__doc__
        self.assertGreater(len(doc), 1)

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
