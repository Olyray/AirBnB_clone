#!/usr/bin/python3
"""
test_city module
"""
from models.city import City
from unittest import TestCase
import pycodestyle


class TestCity(TestCase):
    """
    TestCity class
    """

    def test_pep(self):
        """ test pep """
        style = pycodestyle.StyleGuide(quiet=True)
        files = ['models/city', 'tests/test_models/test_city']
        result = style.check_files(files)
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_doc(self):
        """ test module documentation """
        doc = __import__('models.city').__doc__
        self.assertGreater(len(doc), 1)

    def test_class_doc(self):
        """ test class documentation """
        doc = City.__doc__
        self.assertGreater(len(doc), 1)
