#!/usr/bin/python3
"""Unittest for base_model.py"""

import unittest
from datetime import datetime
from base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """Class for testing BaseModel"""
    def test_save(self):
        """Test save method"""
        base_model = BaseModel()
        base_model.save()
        current_time = datetime.now()
        self.assertEqual(base_model.updated_at.date(), current_time.date())
        self.assertEqual(base_model.updated_at.hour, current_time.hour)
        self.assertEqual(base_model.updated_at.minute, current_time.minute)
        self.assertEqual(base_model.updated_at.second, current_time.second)

    def test_to_dict(self):
        """ Test to_dict method
        """
        base_model = BaseModel()
        base_model_dict = base_model.to_dict()
        self.assertIsInstance(base_model_dict, dict)
        self.assertIn("id", base_model_dict)
        self.assertIn("created_at", base_model_dict)
        self.assertIn("updated_at", base_model_dict)
        self.assertIn("__class__", base_model_dict)
        self.assertEqual(base_model_dict["__class__"], "BaseModel")

    def test_id(self):
        """ Test id attribute """
        base_model = BaseModel()
        self.assertIsInstance(base_model.id, str)

    def test_created_at(self):
        """ Test created_at attribute """
        base_model = BaseModel()
        self.assertIsInstance(base_model.created_at, datetime)

    def test_str(self):
        """ Test __str__ method """
        base_model = BaseModel()
        base_model_str = str(base_model)
        self.assertIsInstance(base_model_str, str)
        self.assertIn(base_model.__class__.__name__, base_model_str)
        self.assertIn(base_model.id, base_model_str)
        self.assertIn(str(base_model.__dict__), base_model_str)

if __name__ == "__main__":
    unittest.main()
