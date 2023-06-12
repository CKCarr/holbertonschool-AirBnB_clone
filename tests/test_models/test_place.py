#!/usr/bin/python3

"""Unittest for Place class"""

import unittest
from models.place import Place
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class Test_Place(unittest.TestCase):
    """ class to test Place class """

    def setUp(self):
        """
        This method set up an instance of User before each test
        """
        # Initialize a new storage instance for each test
        storage.reload()
        FileStorage.clear()
        # Create an instance of Place
        self.place = Place()

    def tearDown(self):
        """
        This method cleans up after each test
        """
        del self.place

    def test_place_inheritance(self):
        """ Test if Place class inherits from BaseModel """
        self.assertIsInstance(self.place, Place)
        self.assertIsInstance(self.place, BaseModel)

    def test_place_attributes(self):
        """ test place attributes """
        self.assertTrue(hasattr(self.place, "city_id"))
        self.assertTrue(hasattr(self.place, "user_id"))
        self.assertTrue(hasattr(self.place, "name"))
        self.assertTrue(hasattr(self.place, "description"))
        self.assertTrue(hasattr(self.place, "number_rooms"))
        self.assertTrue(hasattr(self.place, "number_bathrooms"))
        self.assertTrue(hasattr(self.place, "max_guest"))
        self.assertTrue(hasattr(self.place, "price_by_night"))
        self.assertTrue(hasattr(self.place, "latitude"))
        self.assertTrue(hasattr(self.place, "longitude"))
        self.assertTrue(hasattr(self.place, "amenity_ids"))
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])

    def test_place_city_id_attr(self):
        """ test city_id attribute """
        self.assertEqual(self.place.city_id, "")
        self.place.city_id = "123456"
        self.assertEqual(self.place.city_id, "123456")
        self.assertEqual(type(self.place.city_id), str)

    def test_place_user_id_attr(self):
        """ test user_id attribute """
        self.assertEqual(self.place.user_id, "")
        self.place.user_id = "123456"
        self.assertEqual(self.place.user_id, "123456")
        self.assertEqual(type(self.place.user_id), str)

    def test_place_name_attr(self):
        """ test name attribute """
        self.assertEqual(self.place.name, "")
        self.place.name = "San Francisco"
        self.assertEqual(self.place.name, "San Francisco")
        self.assertEqual(type(self.place.name), str)

    def test_place_description_attr(self):
        """ test description attribute """
        self.assertEqual(self.place.description, "")
        self.place.description = "Beautiful city"
        self.assertEqual(self.place.description, "Beautiful city")
        self.assertEqual(type(self.place.description), str)

    def test_place_number_rooms_attr(self):
        """ test number_rooms attribute """
        self.assertEqual(self.place.number_rooms, 0)
        self.place.number_rooms = 4
        self.assertEqual(self.place.number_rooms, 4)
        self.assertEqual(type(self.place.number_rooms), int)

    def test_place_number_bathrooms_attr(self):
        """ test number_bathrooms attribute """
        self.assertEqual(self.place.number_bathrooms, 0)
        self.place.number_bathrooms = 2
        self.assertEqual(self.place.number_bathrooms, 2)
        self.assertEqual(type(self.place.number_bathrooms), int)

    def test_place_max_guest_attr(self):
        """ test max_guest attribute """
        self.assertEqual(self.place.max_guest, 0)
        self.place.max_guest = 6
        self.assertEqual(self.place.max_guest, 6)
        self.assertEqual(type(self.place.max_guest), int)

    def test_place_price_by_night_attr(self):
        """ test price_by_night attribute """
        self.assertEqual(self.place.price_by_night, 0)
        self.place.price_by_night = 150
        self.assertEqual(self.place.price_by_night, 150)
        self.assertEqual(type(self.place.price_by_night), int)

    def test_place_latitude_attr(self):
        """ test latitude attribute """
        self.assertEqual(self.place.latitude, 0.0)
        self.place.latitude = 37.7749
        self.assertEqual(self.place.latitude, 37.7749)
        self.assertEqual(type(self.place.latitude), float)

    def test_place_longitude_attr(self):
        """ test longitude attribute """
        self.assertEqual(self.place.longitude, 0.0)
        self.place.longitude = 122.4194
        self.assertEqual(self.place.longitude, 122.4194)
        self.assertEqual(type(self.place.longitude), float)

    def test_place_amenity_ids_attr(self):
        """ test amenity_ids attribute """
        self.assertEqual(self.place.amenity_ids, [])
        self.place.amenity_ids = ["123456", "234567"]
        self.assertEqual(self.place.amenity_ids, ["123456", "234567"])
        self.assertEqual(type(self.place.amenity_ids), list)

if __name__ == "__main__":
    unittest.main()
