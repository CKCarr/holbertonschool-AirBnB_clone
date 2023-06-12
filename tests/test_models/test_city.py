#!/usr/bin/python3

"""Unittest for City class"""

import unittest
from models.city import City
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class Test_City(unittest.TestCase):
    """ Class to test City class """

    def setUp(self):
        """
        This method set up an instance of City before each test
        """
        # Initialize a new storage instance for each test
        storage.reload()
        FileStorage.clear()
        # Create an instance of City
        self.city = City()

    def tearDown(self):
        """
        This method cleans up after each test
        """
        del self.city

    def test_city_inheritance(self):
        """ Test if City class inherits from BaseModel """
        self.assertIsInstance(self.city, City)
        self.assertIsInstance(self.city, BaseModel)

    def test_city_attributes(self):
        """ Test City attributes """
        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertTrue(hasattr(self.city, "name"))
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

    def test_city_state_id_attr(self):
        """ Test state_id attribute """
        self.assertEqual(self.city.state_id, "")
        self.city.state_id = "123456"
        self.assertEqual(self.city.state_id, "123456")
        self.assertEqual(type(self.city.state_id), str)

    def test_city_name_attr(self):
        """ Test name attribute """
        self.assertEqual(self.city.name, "")
        self.city.name = "San Francisco"
        self.assertEqual(self.city.name, "San Francisco")
        self.assertEqual(type(self.city.name), str)

if __name__ == "__main__":
    unittest.main()
