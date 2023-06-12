#!/usr/bin/python3
""" This module writes Unittest for User class """

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """ This class TestUser defines Unittest for User class """

    def setUp(self):
        """
        This method set up an instance of User before each test
        """
        self.user = User()

    def tearDown(self):
        """
        This method cleans up after each test
        """
        del self.user

    def test_user_inherits_from_BaseModel(self):
        """
        This method checks if User class inherits from BaseModel
        """
        self.assertIsInstance(self.user, User)

    def test_user_attributes(self):
        """
        This method checks the user attributes:
        checks if it has the attribute:
        email, password, first_name, last_name
        """
        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "password"))
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.email, "")

    def test_email_attr(self):
        """
        This method tests the email attribute
        """
        self.assertTrue(hasattr(self.user, "email"))
        self.assertEqual(self.user, "")
        self.user.email = "user@example.com"
        self.assertIsInstance(self.user.email, str)
        self.asserEqual(self.user.email, "user@example.com")

    def test_password_attr(self):
        """
        This method tests the password attribute
        """
        self.assertTrue(hasattr(self.user, "password"))
        self.assertEqual(self.user.password, "")
        self.user.password = "password123"
        self.assertIsInstance(self.user.password, str)
        self.assertEqual(self.user.password, "password123")

    def test_first_name_attr(self):
        """
        This method tests the first_name attribute
        """
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertEqual(self.user.first_name, "")
        self.user.first_name = "Betty"
        self.assertIsInstance(self.user.first_name, str)
        self.assertEqual(self.user.first_name, "Betty")

    def test_last_name_attr(self):
        """
        This method tests the last_name attribute
        """
        self.assertTrue(hasattr(self.user, "last_name"))
        self.assertEqual(self.user.last_name, "")
        self.user.last_name = "Holberton"
        self.assertIsInstance(self.user.last_name, str)
        self.assertEqual(self.user.last_name, "Holberton")


if __name__ == "__main__":
    unittest.main()
