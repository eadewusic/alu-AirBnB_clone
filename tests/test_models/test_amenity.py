import datetime
import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    def test_attributes_types(self):
        amenity = Amenity()
        self.assertIsInstance(amenity.id, str)
        self.assertIsInstance(amenity.created_at, datetime.datetime)  # Use datetime.datetime here
        self.assertIsInstance(amenity.updated_at, datetime.datetime)  # Use datetime.datetime here

    def test_amenity_custom_attribute(self):
        amenity = Amenity()
        amenity.category = "Entertainment"
        self.assertEqual(amenity.category, "Entertainment")

if __name__ == '__main__':
    unittest.main()
