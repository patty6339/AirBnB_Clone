import unittest
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO

from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        self.cli = HBNBCommand()

    def test_do_quit(self):
        self.assertTrue(self.cli.do_quit(''))

    def test_do_EOF(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.cli.do_EOF(''))
            self.assertEqual(f.getvalue(), '\n')

    def test_emptyline(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.emptyline()
            self.assertEqual(f.getvalue(), '')

    def test_help_show(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("help show")
            actual_output = f.getvalue()
            print(actual_output)
            expected_output = (
                'Show command to retrieve an object from a '
                'string representation'
            )
            self.assertTrue(expected_output in actual_output)

    def test_create_BaseModel(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("create BaseModel")
            new_id = f.getvalue().strip()
            self.assertIn("BaseModel." + new_id, storage.all())

    def test_show_BaseModel(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("create BaseModel")
            new_id = f.getvalue().strip()
            self.cli.onecmd(f"show BaseModel {new_id}")
            # self.assertIn(f"BaseModel.{new_id}", f.getvalue())

    def test_destroy_BaseModel(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("create BaseModel")
            new_id = f.getvalue().strip()
            self.cli.onecmd(f"destroy BaseModel {new_id}")
            self.assertNotIn("BaseModel." + new_id, storage.all())

    def test_all_BaseModel(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("create BaseModel")
            new_id = f.getvalue().strip()
            self.cli.onecmd("all BaseModel")
            self.assertIn(f"{new_id}", f.getvalue())

    def test_update_BaseModel(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("create BaseModel")
            new_id = f.getvalue().strip()
            self.cli.onecmd(f"update BaseModel {new_id} name Test")
            self.cli.onecmd(f"show BaseModel {new_id}")
            self.assertIn("'name': 'Test'", f.getvalue())

    def test_class_all(self):
        classes = [BaseModel, Review, User, State, City, Amenity, Place]
        for cls in classes:
            with self.subTest(cls=cls):
                with patch('sys.stdout', new=StringIO()) as f:
                    self.cli.onecmd(f"create {cls.__name__}")
                    new_id = f.getvalue().strip()
                    self.cli.onecmd(f"{cls.__name__}.all()")
                    self.assertIn(f"{new_id}", f.getvalue())

    def test_class_count(self):
        classes = [BaseModel, User]
        for cls in classes:
            with self.subTest(cls=cls):
                with patch('sys.stdout', new=StringIO()) as f:
                    self.cli.onecmd(f"create {cls.__name__}")
                    self.cli.onecmd(f"{cls.__name__}.count()")
                    # self.assertEqual(f.getvalue().strip(), '1')


if __name__ == '__main__':
    unittest.main()
