import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    def setUp(self):
        self.place = Place()

    def test_instance(self):
        self.assertIsInstance(self.place, BaseModel)
        self.assertIsInstance(self.place, Place)

    def test_attributes(self):
        attributes = {
            'city_id': "",
            'user_id': "",
            'name': "",
            'description': "",
            'number_rooms': 0,
            'number_bathrooms': 0,
            'max_guest': 0,
            'price_by_night': 0,
            'latitude': 0.0,
            'longitude': 0.0,
            'amenity_ids': []
        }
        for attr, value in attributes.items():
            with self.subTest(attr=attr, value=value):
                self.assertTrue(hasattr(self.place, attr))
                self.assertEqual(getattr(self.place, attr), value)


if __name__ == '__main__':
    unittest.main()
