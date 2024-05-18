import unittest
from models.user import User
from models.base_model import BaseModel

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User()

    def test_instance(self):
        self.assertIsInstance(self.user, BaseModel)
        self.assertIsInstance(self.user, User)

    def test_attributes(self):
        attributes = {
            'email': "",
            'password': "",
            'first_name': "",
            'last_name': ""
        }
        for attr, value in attributes.items():
            with self.subTest(attr=attr, value=value):
                self.assertTrue(hasattr(self.user, attr))
                self.assertEqual(getattr(self.user, attr), value)

if __name__ == '__main__':
    unittest.main()