#!/usr/bin/python3

import unittest
from models.city import City

class TestCity(unittest.TestCase):
    def test_instance_attributes(self):
        city = City()
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertTrue(hasattr(city, 'name'))

    def test_default_values(self):
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_custom_values(self):
        city = City(state_id="state_id", name="City Name")
        self.assertEqual(city.state_id, "state_id")
        self.assertEqual(city.name, "City Name")

    def test_to_dict_method(self):
        city = City(state_id="state_id", name="City Name")
        city_dict = city.to_dict()
        self.assertTrue(isinstance(city_dict, dict))
        self.assertEqual(city_dict['__class__'], 'City')

if __name__ == '__main__':
    unittest.main()

