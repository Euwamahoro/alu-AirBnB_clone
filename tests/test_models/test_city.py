#!/usr/bin/python3
import unittest
from models.city import Cityi
from models.base_model import BaseModel


class test_city(unittest.TestCase):
    """tests for class City"""
    
    city = City()
    def test_init(self):

        self.assertIsInstance(city, City)
        self.assertEqual(
            str(type(city)), "<class 'models.city.City'>")
        self.assertEqual(city.name, "Mthatha")

if __name__ == "__main__":
    unittest.main()
