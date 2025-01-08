#!/usr/bin/python3
"""
Module for BaseModel unittest
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBasemodel(unittest.TestCase):
    """
    Unittest for BaseModel
    """

    def test_init(self):
        """
        Test for init
        """
        my_model = BaseModel()

        self.assertIsNotNone(my_model.id)
        self.assertIsNotNone(my_model.created_at)
        self.assertIsNotNone(my_model.updated_at)

    def test_save(self):
        """
        Test for save method
        """
        my_model = BaseModel()

        initial_updated_at = my_model.updated_at

        my_model.save()  # Call save method to update the timestamp
        updated_updated_at = my_model.updated_at

        # Ensure updated_at is modified after save
        self.assertNotEqual(initial_updated_at, updated_updated_at)
        self.assertTrue(updated_updated_at > initial_updated_at)

    def test_to_dict(self):
        """
        Test for to_dict method
        """
        my_model = BaseModel()

        my_model_dict = my_model.to_dict()

        self.assertIsInstance(my_model_dict, dict)

        self.assertEqual(my_model_dict["__class__"], 'BaseModel')
        self.assertEqual(my_model_dict['id'], my_model.id)
        self.assertEqual(my_model_dict['created_at'], my_model.created_at.isoformat())
        self.assertEqual(my_model_dict["updated_at"], my_model.updated_at.isoformat())


    def test_str(self):
        """
        Test for string representation
        """
        my_model = BaseModel()

        self.assertTrue(str(my_model).startswith('[BaseModel]'))

        self.assertIn(my_model.id, str(my_model))

        self.assertIn(str(my_model.__dict__), str(my_model))


if __name__ == "__main__":
    unittest.main()
