import unittest
from models.place import Place

class TestPlace(unittest.TestCase):
    def test_attributes_types(self):
        place = Place()
        self.assertIsInstance(place.id, str)
        self.assertIsInstance(place.created_at, datetime)
        self.assertIsInstance(place.updated_at, datetime)

    def test_place_custom_attribute(self):
        place = Place()
        place.location = "City Center"
        self.assertEqual(place.location, "City Center")

if __name__ == '__main__':
    unittest.main()
