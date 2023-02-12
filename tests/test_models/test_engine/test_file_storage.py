#!/usr/bin/python3
""" test_file_storage module """
from unittest import TestCase
import pycodestyle
from models.engine.file_storage import FileStorage


class TestFileStorage(TestCase):
    """
    TestFileStorage class
    """

    def pep(self):
        """ test pep """
        style = pycodestyle.StyleGuide(quiet=True)
        files = ['models/engine/file_storage',
            'test/test_models/test_engine/test_file_storage']
        result = style.check_files(files)
        self.assertEqual(result.total_errors, 0,
            "Found code style errors (and warning).")

    def test_module_doc(self):
        """
        test module documentation
        """
        doc = __import__('models/engine/file_storage').__doc__
        self.assertGreater(len(doc), 1)

    def test_class_doc(self):
        """
        test class documentation
        """
        doc = TestFileStorage.__doc__
        self.assertGreater(len(doc), 1)
