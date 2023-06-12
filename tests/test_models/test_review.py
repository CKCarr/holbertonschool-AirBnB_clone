#!/usr/bin/python3

"""Unittest for Review class"""

import unittest
import os
import models
from models.review import Review
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage


class Test_Review(unittest.TestCase):
    """ Test Review class """

    def setUp(self):
        """
        This method set up an instance of User before each test
        """
        # Initialize a new storage instance for each test
        storage.reload()
        FileStorage.clear()
        # Create an instance of review
        self.review = Review()

    def tearDown(self):
        """
        This method cleans up after each test
        """
        del self.review

    def test_review_inheritance(self):
        """
        This method checks if Review class inherits from BaseModel
        """
        self.assertIsInstance(self.review, Review)
        self.assertIsInstance(self.review, BaseModel)

    def test_review_attributes(self):
        """ Test Review attributes """
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertTrue(hasattr(self.review, "text"))
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_place_id_attr(self):
        """ Test place_id attribute """
        self.assertEqual(self.review.place_id, "")
        self.review.place_id = "123456"
        self.assertEqual(self.review.place_id, "123456")
        self.assertEqual(type(self.review.place_id), str)

    def test_user_id_attr(self):
        """ Test user_id attribute """
        self.assertEqual(self.review.user_id, "")
        self.review.user_id = "123456"
        self.assertEqual(self.review.user_id, "123456")
        self.assertEqual(type(self.review.user_id), str)

    def test_text_attr(self):
        """"
        This method tests the text attribute
        """
        self.assertEqual(self.review.text, "")
        self.review.text = "This is a review"
        self.assertEqual(self.review.text, "This is a review")
        self.assertEqual(type(self.review.text), str)


if __name__ == "__main__":
    unittest.main()
