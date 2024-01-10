#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
import datetime
from models.user import User

class test_user(unittest.TestCase):
    """tests for class User"""
    user = User()
    def test_init(self):
        self.assertIsInstance(self.user, User)
        self.assertEqual(str(type(user)), "<class 'models.user.User'>")
        self.assertEqual(str(type(user.id)), "<class 'str'>")
        self.assertTrue(self.us, 'id')
        self.assertTrue(self.us, 'first_name')
        self.assertTrue(self.us, 'last_name')
        self.assertTrue(self.us, 'email')
        self.assertTrue(self.us, 'password')

if __name__ == "__main__":
    unittest.main()
