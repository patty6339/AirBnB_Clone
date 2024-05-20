import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()
        self.my_model = BaseModel()
        self.my_model.name = "Holberton"
        self.my_model.my_number = 89
        self.storage.new(self.my_model)

    def test_all(self):
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        self.assertIn("BaseModel." + self.my_model.id, self.storage.all())

    def test_save(self):
        self.storage.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_reload(self):
        self.storage.reload()
        self.assertIn("BaseModel." + self.my_model.id, self.storage.all())

    def test_new_adds_to_objects(self):
        initial_storage = FileStorage()
        initial_storage.new(self.my_model)
        self.assertIn("BaseModel." + self.my_model.id, initial_storage.all())

    def test_new_does_not_add_duplicates(self):
        initial_storage = FileStorage()
        initial_storage.new(self.my_model)
        initial_storage.new(self.my_model)
        self.assertEqual(len(initial_storage.all()), 1)
        self.assertIn("BaseModel." + self.my_model.id, initial_storage.all())


if __name__ == '__main__':
    unittest.main()
