#!/usr/bin/python3
"""
Define unittests for 'console.py'
unittest classes:
    TestHBNBCommand_prompting
    TestHBNBCommand_help
    TestHBNBCommand_exit
    TestHBNBCommand_create
    TestHBNBCommand_show
    TestHBNBCommand_all
    TestHBNBCommand_destroy
    TestHBNBCommand_update
"""

from unittest.mock import patch
from io import StringIO
import unittest
import os
from console import HBNBCommand
from models import storage
from models.engine.file_storage import FileStorage


class TestHBNBCommandPrompting(unittest.TestCase):
    """
    Unittests to test the prompting behavior of HBNB command interpreter.
    """

    def test_prompt(self):
        with patch("builtins.input", return_value="quit") as mock_input:
            with patch("sys.stdout", new=StringIO()) as mock_output:
                HBNBCommand().cmdloop()
        self.assertEqual(mock_output.getvalue(), "(hbnb) ")


class TestHBNBCommandHelp(unittest.TestCase):
    """
    Unittests to test the help command of HBNB command interpreter.
    """

    def test_help(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("help")
            self.assertNotEqual(output.getvalue(), "")


class TestHBNBCommandExit(unittest.TestCase):
    """
    Unittests to test the exit command of HBNB command interpreter.
    """

    def test_exit(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("quit"))
            self.assertEqual(output.getvalue(), "")


class TestHBNBCommandCreate(unittest.TestCase):
    """
    Unittests to test the create command of HBNB command interpreter.
    """

    def test_create(self):
        classes = ["BaseModel", "User", "State", "City", "Place", "Amenity", "Review"]
        for class_name in classes:
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(f"create {class_name}"))
                self.assertNotEqual(output.getvalue(), "")


class TestHBNBCommandShow(unittest.TestCase):
    """
    Unittests to test the show command of HBNB command interpreter.
    """

    def test_show(self):
        classes = ["BaseModel", "User", "State", "City", "Place", "Amenity", "Review"]
        for class_name in classes:
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(f"create {class_name}"))
                test_id = output.getvalue().strip()
                with patch("sys.stdout", new=StringIO()) as output:
                    self.assertFalse(HBNBCommand().onecmd(f"show {class_name} {test_id}"))
                    self.assertNotEqual(output.getvalue(), "")


class TestHBNBCommandAll(unittest.TestCase):
    """
    Unittests to test the all command of HBNB command interpreter.
    """

    def test_all(self):
        classes = ["BaseModel", "User", "State", "City", "Place", "Amenity", "Review"]
        for class_name in classes:
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(f"create {class_name}"))
                with patch("sys.stdout", new=StringIO()) as output:
                    self.assertFalse(HBNBCommand().onecmd(f"all {class_name}"))
                    self.assertNotEqual(output.getvalue(), "")


class TestHBNBCommandDestroy(unittest.TestCase):
    """
    Unittests to test the destroy command of HBNB command interpreter.
    """

    def test_destroy(self):
        classes = ["BaseModel", "User", "State", "City", "Place", "Amenity", "Review"]
        for class_name in classes:
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(f"create {class_name}"))
                test_id = output.getvalue().strip()
                with patch("sys.stdout", new=StringIO()) as output:
                    self.assertFalse(HBNBCommand().onecmd(f"destroy {class_name} {test_id}"))
                    self.assertNotEqual(output.getvalue(), "")


class TestHBNBCommandUpdate(unittest.TestCase):
    """
    Unittests to test the update method of HBNB command interpreter.
    """

    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_update_missing_attr_name_space_notation(self):
        correct = "** attribute name missing **"
        classes = ["BaseModel", "User", "State", "City", "Place", "Amenity", "Review"]
        for class_name in classes:
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(f"create {class_name}"))
                test_id = output.getvalue().strip()
                test_cmd = f"update {class_name} {test_id}"
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(test_cmd))
                self.assertEqual(correct, output.getvalue().strip())

    def test_update_missing_attr_name_dot_notation(self):
        correct = "** attribute name missing **"
        classes = ["BaseModel", "User", "State", "City", "Place", "Amenity", "Review"]
        for class_name in classes:
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(f"create {class_name}"))
                test_id = output.getvalue().strip()
                test_cmd = f"{class_name}.update({{}})".format(test_id)
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(test_cmd))
                self.assertEqual(correct, output.getvalue().strip())

    def test_update_missing_attr_value_space_notation(self):
        correct = "** value missing **"
        classes = ["BaseModel", "User", "State", "City", "Place", "Amenity", "Review"]
        for class_name in classes:
            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd(f"create {class_name}")
                test_id = output.getvalue().strip()
            with patch("sys.stdout", new=StringIO()) as output:
                test_cmd = f"update {class_name} {test_id} attr_name"
                self.assertFalse(HBNBCommand().onecmd(test_cmd))
                self.assertEqual(correct, output.getvalue().strip())

    def test_update_missing_attr_value_dot_notation(self):
        correct = "** value missing **"
        classes = ["BaseModel", "User", "State", "City", "Place", "Amenity", "Review"]
        for class_name in classes:
            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd(f"create {class_name}")
                test_id = output.getvalue().strip()
            with patch("sys.stdout", new=StringIO()) as output:
                test_cmd = f"{class_name}.update({{"'0'": None}})".format(test_id)
                self.assertFalse(HBNBCommand().onecmd(test_cmd))
                self.assertEqual(correct, output.getvalue().strip())

    def test_update_valid_str_attr_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            test_id = output.getvalue().strip()
        test_cmd = f"update Place {test_id} name 'California'"
        self.assertFalse(HBNBCommand().onecmd(test_cmd))
        test_dict = storage.all()["Place.{test_id}"].__dict__
        self.assertEqual("California", test_dict["name"])

    def test_update_valid_str_attr_dot_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            test_id = output.getvalue().strip()
        test_cmd = f"Place.update({{'{0}': 'New York'}})".format(test_id)
        self.assertFalse(HBNBCommand().onecmd(test_cmd))
        test_dict = storage.all()["Place.{test_id}"].__dict__
        self.assertEqual("New York", test_dict["name"])

    def test_update_valid_int_attr_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            test_id = output.getvalue().strip()
        test_cmd = f"update Place {test_id} max_guest 99"
        self.assertFalse(HBNBCommand().onecmd(test_cmd))
        test_dict = storage.all()["Place.{test_id}"].__dict__
        self.assertEqual(99, test_dict["max_guest"])

    def test_update_valid_int_attr_dot_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            test_id = output.getvalue().strip()
        test_cmd = f"Place.update({{'{0}': 99}})".format(test_id)
        self.assertFalse(HBNBCommand().onecmd(test_cmd))
        test_dict = storage.all()["Place.{test_id}"].__dict__
        self.assertEqual(99, test_dict["max_guest"])

    def test_update_valid_float_attr_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            test_id = output.getvalue().strip()
        test_cmd = f"update Place {test_id} floaty 98.5"
        self.assertFalse(HBNBCommand().onecmd(test_cmd))
        test_dict = storage.all()["Place.{test_id}"].__dict__
        self.assertEqual(98.5, test_dict["floaty"])

    def test_update_valid_float_attr_dot_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            test_id = output.getvalue().strip()
            test_cmd = f"Place.update({{'{0}': 99.9}})".format(test_id)
        self.assertFalse(HBNBCommand().onecmd(test_cmd))
        test_dict = storage.all()["Place.{test_id}"].__dict__
        self.assertEqual(99.9, test_dict["floaty"])

    def test_update_valid_list_attr_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            test_id = output.getvalue().strip()
        test_cmd = f"update Place {test_id} my_list [1, 2, 3]"
        self.assertFalse(HBNBCommand().onecmd(test_cmd))
        test_dict = storage.all()["Place.{test_id}"].__dict__
        self.assertEqual([1, 2, 3], test_dict["my_list"])

    def test_update_valid_list_attr_dot_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            test_id = output.getvalue().strip()
        test_cmd = f"Place.update({{'{0}': [1, 2, 3]}})".format(test_id)
        self.assertFalse(HBNBCommand().onecmd(test_cmd))
        test_dict = storage.all()["Place.{test_id}"].__dict__
        self.assertEqual([1, 2, 3], test_dict["my_list"])

    def test_update_valid_dict_attr_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            test_id = output.getvalue().strip()
        test_cmd = f"update Place {test_id} my_dict {{'a': 1, 'b': 2}}"
        self.assertFalse(HBNBCommand().onecmd(test_cmd))
        test_dict = storage.all()['Place.{test_id}'].__dict__
        self.assertEqual({'a': 1, 'b': 2}, test_dict["my_dict"])

    def test_update_valid_dict_attr_dot_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            test_id = output.getvalue().strip()
        test_cmd = f"Place.update({{"'0'": {{'a': 1, 'b': 2}}}})".format(test_id)
        self.assertFalse(HBNBCommand().onecmd(test_cmd))
        test_dict = storage.all()["Place.{test_id}"].__dict__
        self.assertEqual({'a': 1, 'b': 2}, test_dict["my_dict"])


if __name__ == "__main__":
    unittest.main()
