import datetime
import unittest
from models.user import User

class TestUser(unittest.TestCase):
    def test_attributes_types(self):
        user = User()
        self.assertIsInstance(user.id, str)
        self.assertIsInstance(user.created_at, datetime.datetime)
        self.assertIsInstance(user.updated_at, datetime.datetime)
        # Add more test cases specific to the User model

    def test_user_custom_attribute(self):
        user = User()
        user.username = "test_user"
        self.assertEqual(user.username, "test_user")

if __name__ == '__main__':
    unittest.main()
