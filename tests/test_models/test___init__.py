import unittest
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()

    def test_reload(self):
        self.storage.reload()
        self.assertIsNotNone(self.storage._FileStorage__objects)
        self.assertIsNotNone(self.storage._FileStorage__file_path)


if __name__ == '__main__':
    unittest.main()