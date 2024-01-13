import datetime
import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    def test_attributes_types(self):
        review = Review()
        self.assertIsInstance(review.id, str)
        self.assertIsInstance(review.created_at, datetime.datetime)
        self.assertIsInstance(review.updated_at, datetime.datetime)

    def test_review_custom_attribute(self):
        review = Review()
        review.rating = 5
        self.assertEqual(review.rating, 5)

if __name__ == '__main__':
    unittest.main()
