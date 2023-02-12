#!/usr/bin/python3
"""
test_amenity module
"""
from models.amenity import Amenity
import pycodestyle
from unittest import TestCase


class TestAmenity(TestCase):
    """
    TestAmenity class
    """

    def test_pep(self):
        """ test pep """
        style = pycodestyle.StyleGuide(quiet=True)
        files = ['models/amenity', 'tests/test_model/test_amenity']
        result = style.check_files(files)
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_doc(self):
        """ test module documentation """
        doc = __import__('models.amenity').__doc__
        self.assertGreater(len(doc), 1)

    def test_class_doc(self):
        """ test class documentation """
        doc = Amenity.__doc__
        self.assertGreater(len(doc), 1)
