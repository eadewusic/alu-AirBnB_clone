import unittest
from models.city import City

class TestCity(unittest.TestCase):
    def test_attributes_types(self):
        city = City()
        self.assertIsInstance(city.id, str)
        self.assertIsInstance(city.created_at, datetime)
        self.assertIsInstance(city.updated_at, datetime)

    def test_city_custom_attribute(self):
        city = City()
        city.population = 1000000
        self.assertEqual(city.population, 1000000)

if __name__ == '__main__':
    unittest.main()
