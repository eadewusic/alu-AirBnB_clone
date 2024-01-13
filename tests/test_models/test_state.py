import unittest
from models.state import State

class TestState(unittest.TestCase):
    def test_attributes_types(self):
        state = State()
        self.assertIsInstance(state.id, str)
        self.assertIsInstance(state.created_at, datetime)
        self.assertIsInstance(state.updated_at, datetime)

    def test_state_custom_attribute(self):
        state = State()
        state.capital = "Capital City"
        self.assertEqual(state.capital, "Capital City")

if __name__ == '__main__':
    unittest.main()
