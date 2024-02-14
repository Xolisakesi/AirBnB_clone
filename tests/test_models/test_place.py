import unittest
from models.place import Place

class TestPlace(unittest.TestCase):
    def test_instance_attributes(self):
        place = Place()
        self.assertTrue(hasattr(place, 'city_id'))
        self.assertTrue(hasattr(place, 'user_id'))
        self.assertTrue(hasattr(place, 'name'))
        self.assertTrue(hasattr(place, 'description'))
        self.assertTrue(hasattr(place, 'number_rooms'))
        self.assertTrue(hasattr(place, 'number_bathrooms'))
        self.assertTrue(hasattr(place, 'max_guest'))
        self.assertTrue(hasattr(place, 'price_by_night'))
        self.assertTrue(hasattr(place, 'latitude'))
        self.assertTrue(hasattr(place, 'longitude'))
        self.assertTrue(hasattr(place, 'amenity_ids'))

    def test_default_values(self):
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_custom_values(self):
        place = Place(city_id="city_id", user_id="user_id", name="Place Name",
                      description="Description", number_rooms=3, number_bathrooms=2,
                      max_guest=4, price_by_night=100, latitude=40.7128, longitude=-74.0060,
                      amenity_ids=["amenity_id1", "amenity_id2"])
        self.assertEqual(place.city_id, "city_id")
        self.assertEqual(place.user_id, "user_id")
        self.assertEqual(place.name, "Place Name")
        self.assertEqual(place.description, "Description")
        self.assertEqual(place.number_rooms, 3)
        self.assertEqual(place.number_bathrooms, 2)
        self.assertEqual(place.max_guest, 4)
        self.assertEqual(place.price_by_night, 100)
        self.assertEqual(place.latitude, 40.7128)
        self.assertEqual(place.longitude, -74.0060)
        self.assertEqual(place.amenity_ids, ["amenity_id1", "amenity_id2"])

    def test_to_dict_method(self):
        place = Place(city_id="city_id", user_id="user_id", name="Place Name",
                      description="Description", number_rooms=3, number_bathrooms=2,
                      max_guest=4, price_by_night=100, latitude=40.7128, longitude=-74.0060,
                      amenity_ids=["amenity_id1", "amenity_id2"])
        place_dict = place.to_dict()
        self.assertTrue(isinstance(place_dict, dict))
        self.assertEqual(place_dict['__class__'], 'Place')

if __name__ == '__main__':
    unittest.main()

