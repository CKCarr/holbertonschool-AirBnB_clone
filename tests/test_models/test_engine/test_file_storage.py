#!/usr/bin/python3
""" Test file_storage module """

import unittest
from models import BaseModel
from models import storage
from models.engine.file_storage import FileStorage
import os


class TestFileStorage(unittest.TestCase):
    """ Class to test file storage engine an the methods it holds """

    def setUp(self):
        """ This method  is called before(sets up) each
        case is run
        """
        # Create a new FileStorage object before each test
        self.file_storage = FileStorage()
        # Create a new instance of the base model
        self.test_object = BaseModel()
        # Store this instance in the FileStorage
        self.file_storage.new(self.test_object)
        # generate the key for this instance
        self.key = "{}.{}".format(
            self.test_object.__class__.__name__, self.test_object.id)

    def test_all(self):
        """ Test the 'all' method of file storage
        - checks if it returns the dictionary containing our object.
        """
        self.assertEqual(self.file_storage.all()[self.key], self.test_object)

    def test_new(self):
        """ Test the 'new' method of File Storage class """
        self.assertIn(self.key, self.file_storage.all())
        self.assertEqual(self.file_storage.all()[self.key], self.test_object)

    def test_save_and_reload(self):
        """ test the 'save and 'reload' methods of FIle Storage Class
        - call the save method to write data to file
        - clear the data memory.
        - call the reload method to load data from the file"""
        self.file_storage.save()

        self.file_storage.clear()
        self.assertNotIn(self.key, self.file_storage.all())

        self.file_storage.reload()

        # Check if the data is correctly loaded
        self.assertIn(self.key, self.file_storage.all())
        self.assertEqual(
            self.test_object.to_dict(),
            self.file_storage.all()[self.key].to_dict())

    def test_file_path(self):
        """ Test if file path is set correctly """
        self.assertEqual(
            self.file_storage._FileStorage__file_path,
            "file.json")

    def tearDown(self):
        """ This method is called after each test is run and tears
        down the set up and any instance created """
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass


if __name__ == "__main__":
    unittest.main()
