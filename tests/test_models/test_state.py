import unittest
from models.state import State
from models.base_model import BaseModel

class TestState(unittest.TestCase):
    def setUp(self):
        self.state = State()

    def test_instance(self):
        self.assertIsInstance(self.state, BaseModel)
        self.assertIsInstance(self.state, State)

    def test_attributes(self):
        self.assertTrue(hasattr(self.state, 'name'))
        self.assertEqual(self.state.name, "")

if __name__ == '__main__':
    unittest.main()