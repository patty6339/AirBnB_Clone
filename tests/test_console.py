import unittest
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO


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


if __name__ == '__main__':
    unittest.main()
