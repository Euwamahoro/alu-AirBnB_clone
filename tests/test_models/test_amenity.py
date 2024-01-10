#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
import datetime
from models.amenity import Amenity


class test_amenity(unittest.TestCase):
    """tests for class amenity"""
    amenity = Amenity()
    def test_init(self):
        self.assertEqual(amenity.name, "amenity")
        self.assertEqual(
            str(type(amenity)), "<class 'models.amenity.Amenity'>")
        self.assertTrue(self.amenity, 'created_at')
        self.assertTrue(self.amenity, 'updated_at')

if __name__ == "__main__":
    unittest.main()i
