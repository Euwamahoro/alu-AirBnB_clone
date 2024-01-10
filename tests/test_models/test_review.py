#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.review import Review


class test_review(unittest.TestCase):
    """tests for class review"""
    review = Review()
    def test_init(self):
        self.assertIsInstance(review, Review)
        self.assertEqual(str(type(review)), "<class 'models.review.Review'>")
        self.assertEqual(review.place_id, "p")
        self.assertEqual(review.user_id, "p")
        self.assertEqual(review.text, "p")

if __name__ == "__main__":
    unittest.main()
