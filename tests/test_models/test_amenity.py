#!/usr/bin/python3

import unittest
from models.state import State

class TestState(unittest.TestCase):
    def test_instance_attributes(self):
        state = State()
        self.assertTrue(hasattr(state, 'name'))

    def test_default_values(self):
        state = State()
        self.assertEqual(state.name, "")

    def test_custom_values(self):
        state = State(name="Test State")
        self.assertEqual(state.name, "Test State")

    def test_to_dict_method(self):
        state = State(name="Test State")
        state_dict = state.to_dict()
        self.assertTrue(isinstance(state_dict, dict))
        self.assertEqual(state_dict['__class__'], 'State')

if __name__ == '__main__':
    unittest.main()

