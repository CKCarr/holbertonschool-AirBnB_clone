#!/usr/bin/python3

"""Unittest for State class"""

import unittest
from models.state import State


class Test_State(unittest.TestCase):
    """
    Class for testing State class
    """

    def setUp(self):
        """"
        Method to set the start point
        """
        self.state = State()

    def tearDown(self):
        """
        Method to clean up after each test
        """
        del self.state

    def test_state_attributes(self):
        """
        Method to test the attributes of State class
        """
        self.assertTrue(hasattr(self.state, "name"))
        self.assertEqual(self.state.name, "")

    def test_name_attr(self):
        """ Method to test the name attribute """
        self.assertTrue(hasattr(self.state, "name"))
        self.assertEqual(self.state.name, "")
        self.state.name = "California"
        self.assertIsInstance(self.state.name, str)
        self.assertEqual(self.state.name, "California")


if __name__ == "__main__":
    unittest.main()
