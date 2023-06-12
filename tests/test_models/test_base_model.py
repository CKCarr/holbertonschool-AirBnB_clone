#!/usr/bin/python3
"""Unittest for base_model.py"""

import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class Test_Base_Model(unittest.TestCase):
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

    def test_create_with_to_dict(self):
        # Create the first BaseModel instance without arguments
        base_model1 = BaseModel()

        # Get the dictionary representation of the first instance
        base_model1_dict = base_model1.to_dict()

        # Create the second BaseModel instance
        # using the dictionary representation
        base_model2 = BaseModel(**base_model1_dict)

        # Assert that the two instances have the same attribute values
        self.assertEqual(base_model1.id, base_model2.id)
        self.assertEqual(base_model1.created_at, base_model2.created_at)
        self.assertEqual(base_model1.updated_at, base_model2.updated_at)


if __name__ == "__main__":
    unittest.main()
