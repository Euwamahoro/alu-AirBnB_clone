#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
import datetime
from models.place import Place

class test_place(unittest.TestCase):
   """tests for class Place"""
    place = Place()
    def test_init(self):
        self.assertEqual(str(type(place)), "<class 'models.place.Place'>")
        self.assertTrue(self.place,"name")
        self.assertTrue(self.place,"user_id")
        self.assertTrue(self.place,"city_id")
        self.assertTrue(self.place,"amenity_ids")
        self.assertTrue(self.place,"number_rooms")
        self.assertTrue(self.place,"number_bathrooms")
        self.assertTrue(self.place,"created_at")
         self.assertTrue(self.place,"price_by_night")
        self.assertTrue(self.place,"description")
        self.assertTrue(self.place,"latitude")
        self.assertTrue(self.place,"longitude")


if __name__ == "__main__":
    unittest.main()
