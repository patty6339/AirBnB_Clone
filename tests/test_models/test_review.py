import unittest
from models.review import Review
from models.base_model import BaseModel

class TestReview(unittest.TestCase):
    def setUp(self):
        self.review = Review()

    def test_instance(self):
        self.assertIsInstance(self.review, BaseModel)
        self.assertIsInstance(self.review, Review)

    def test_attributes(self):
        attributes = {
            'place_id': "",
            'user_id': "",
            'text': ""
        }
        for attr, value in attributes.items():
            with self.subTest(attr=attr, value=value):
                self.assertTrue(hasattr(self.review, attr))
                self.assertEqual(getattr(self.review, attr), value)

if __name__ == '__main__':
    unittest.main()