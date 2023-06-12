#!/usr/bin/python3

"""Unittest for Amenity class"""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class Test_Amenity(unittest.TestCase):
    """ Class to test Amenity class """

    def setUp(self):
        """
        This method set up an instance of Amenity before each test
        """
        # Initialize a new storage instance for each test
        storage.reload()
        FileStorage.clear()
        # Create an instance of Amenity
        self.amenity = Amenity()

    def tearDown(self):
        """
        This method cleans up after each test
        """
        del self.amenity

    def test_amenity_inheritance(self):
        """ Test if Amenity class inherits from BaseModel """
        self.assertIsInstance(self.amenity, Amenity)
        self.assertIsInstance(self.amenity, BaseModel)

    def test_amenity_attributes(self):
        """ Test Amenity attributes """
        self.assertTrue(hasattr(self.amenity, "name"))
        self.assertEqual(self.amenity.name, "")

    def test_amenity_name_attr(self):
        """ Test name attribute """
        self.assertEqual(self.amenity.name, "")
        self.amenity.name = "Wifi"
        self.assertEqual(self.amenity.name, "Wifi")
        self.assertEqual(type(self.amenity.name), str)

if __name__ == "__main__":
    unittest.main()
