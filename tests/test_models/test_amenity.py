import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """
    TestAmenity class to test the Amenity class
    """

    def setUp(self):
        """
        Set up for the tests
        """
        self.amenity = Amenity()

    def tearDown(self):
        """
        Cleaning up after each test
        """
        del self.amenity

    def test_is_instance(self):
        """
        Test for instantiation
        """
        self.assertIsInstance(self.amenity, Amenity)

    def test_is_subclass(self):
        """
        Test if Amenity is a subclass of BaseModel
        """
        self.assertTrue(issubclass(self.amenity.__class__, BaseModel))

    def test_name_attr(self):
        """
        Test Amenity has attribute name, and it's an empty string
        """
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))
        self.assertEqual(amenity.name, "")


if __name__ == "__main__":
    unittest.main()
