#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.state import State

"""tests for class State"""

class test_state(unittest.TestCase):
    state = State()
    def test_init(self):
        """tests"""
        self.assertIsInstance(state, State)
        self.assertEqual(str(type(state)), "<class 'models.state.State'>")
       
    def test_name(self):
        """tests name"""
        state.name = "Eastern Cape"
        self.assertEqual(state.name, "Eastern Cape")

if __name__ == "__main__":
    unittest.main()
