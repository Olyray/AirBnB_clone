#!/usr/bin/python3
"""
test_user module
"""
from unittest import TestCase
import pycodestyle
from models.user import user


class TestUser(TestCase):
    """
    TestUser class
    """

    def test_pep(self):
        """ test pep """
        style = pycodestyle.StyleGuide(quiet=True)
        files = ['models/user', 'test/test_models/test_user']
        result = style.check_files(files)
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_doc(self):
        """ test module documentation """
        doc = __import__('models.user').__doc__
        self.assertGreater(len(doc), 1)

    def test_class_doc(self):
        """ test class documentation """
        doc = User.__doc__
        self.assertGreater(len(doc), 1)
