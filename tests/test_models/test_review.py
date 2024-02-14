#!/usr/bin/python3

import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    def test_instance_attributes(self):
        review = Review()
        self.assertTrue(hasattr(review, 'place_id'))
        self.assertTrue(hasattr(review, 'user_id'))
        self.assertTrue(hasattr(review, 'text'))

    def test_default_values(self):
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_custom_values(self):
        review = Review(place_id="place_id", user_id="user_id", text="Review Text")
        self.assertEqual(review.place_id, "place_id")
        self.assertEqual(review.user_id, "user_id")
        self.assertEqual(review.text, "Review Text")

    def test_to_dict_method(self):
        review = Review(place_id="place_id", user_id="user_id", text="Review Text")
        review_dict = review.to_dict()
        self.assertTrue(isinstance(review_dict, dict))
        self.assertEqual(review_dict['__class__'], 'Review')

if __name__ == '__main__':
    unittest.main()

