#!/usr/bin/python3
"""test for console"""
import unittest
from unittest.mock import patch
from io import StringIO
import pep8
import os
import json
import console
import tests
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestConsole(unittest.TestCase):
    """this will test the console"""

    @classmethod
    def setUpClass(cls):
        """setup for the test"""
        cls.consol = HBNBCommand()
        cls.storage = FileStorage()

    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down"""
        del cls.consol

    def tearDown(self):
        """Remove temporary file (file.json) created as a result"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_console(self):
        """Pep8 console.py"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(["console.py"])
        self.assertEqual(p.total_errors, 0, 'fix Pep8')

    def test_docstrings_in_console(self):
        """checking for docstrings"""
        self.assertIsNotNone(console.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)
        self.assertIsNotNone(HBNBCommand.count.__doc__)
        self.assertIsNotNone(HBNBCommand.strip_clean.__doc__)
        self.assertIsNotNone(HBNBCommand.default.__doc__)

    def test_emptyline(self):
        """Test empty line input"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("\n")
            self.assertEqual('', f.getvalue())

    def test_quit(self):
        """test quit command inpout"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("quit")
            self.assertEqual('\n', f.getvalue())

    def test_create(self):
        """Test create command inpout"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("create")
            self.assertEqual(
                "** class name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("create asdfsfsd")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            "Count number of objects, create State, compare counts"
            countb = len(self.storage.all().keys())
            self.consol.onecmd("create State name='California'")
            counta = len(self.storage.all().keys())
            self.assertGreater(counta, countb)
            "save State ID for city creation"
            state_id = f.getvalue().strip("\n")
        with patch('sys.stdout', new=StringIO()) as f:
            """test output of all after creation"""
            self.consol.onecmd("all State")
            self.assertEqual("[[State]", f.getvalue()[:8])
            stateObj_id = "State.{}".format(state_id)
            self.assertEqual(type(self.storage.all()[stateObj_id].name), str)
            self.assertEqual(self.storage.all()[stateObj_id].name, "California")
        with patch('sys.stdout', new=StringIO()) as f:
            "Count number of objects, create City, compare counts"
            countb = len(storage.all().keys())
            self.consol.onecmd('''create City
                               name="San Francisco"
                               state_id="{}"'''.format(state_id))
            counta = len(storage.all().keys())
            self.assertGreater(counta, countb)
            "save City ID for Place creation"
            city_id = f.getvalue().strip("\n")
        with patch('sys.stdout', new=StringIO()) as f:
            """test output of all after creation"""
            self.consol.onecmd("all City")
            self.assertEqual("[[City]", f.getvalue()[:7])
            cityObj_id = "City.{}".format(city_id)
            self.assertEqual(type(storage.all()[cityObj_id].name), str)
            self.assertEqual(storage.all()[cityObj_id].name, "San Francisco")
            self.assertEqual(type(storage.all()[cityObj_id].state_id), str)
            self.assertEqual(storage.all()[cityObj_id].state_id, "{}"
                             .format(state_id))
        with patch('sys.stdout', new=StringIO()) as f:
            "Count number of objects, create User, compare counts"
            countb = len(storage.all().keys())
            self.consol.onecmd("create User email='California' password='CA'")
            counta = len(storage.all().keys())
            self.assertGreater(counta, countb)
            "save User ID for place creation"
            user_id = f.getvalue().strip("\n")
        with patch('sys.stdout', new=StringIO()) as f:
            """test output of all after creation"""
            self.consol.onecmd("all User")
            self.assertEqual("[[User]", f.getvalue()[:7])
            userObj_id = "User.{}".format(user_id)
            self.assertEqual(type(storage.all()[userObj_id].email), str)
            self.assertEqual(storage.all()[stateObj_id].email, "California")
            self.assertEqual(type(storage.all()[userObj_id].password), str)
            self.assertEqual(storage.all()[stateObj_id].password, "CA")
        with patch('sys.stdout', new=StringIO()) as f:
            countb = len(storage.all().keys())
            self.consol.onecmd('create Place city_id="{}" user_id="{}"\
                               name="My_little_house" number_rooms=4\
                               number_bathrooms=2 max_guest=10\
                               price_by_night=300 latitude=37.773972\
                               longitude=-122.431297'.format(city_id, user_id))
            pla_id = f.getvalue().strip("\n")
            counta = len(storage.all().keys())
            self.assertGreater(counta, countb)
            placeObj_id = "Place.{}".format(pla_id)
            self.assertEqual(type(storage.all()[placeObj_id].name), str)
            self.assertEqual(storage.all()[placeObj_id].name,
                             "My little house")
            self.assertEqual(type(storage.all()[placeObj_id].city_id), str)
            self.assertEqual(storage.all()[placeObj_id].city_id, "{}".city_id)
            self.assertEqual(type(storage).all()[placeObj_id].user_id, str)
            self.assertEqual(storage.all()[placeObj_id].user_id,
                             "{}".format(user_id))
            self.assertEqual(type(storage.all()[placeObj_id].number_rooms),
                             int)
            self.assertEqual(storage.all()[placeObj_id].number_rooms, 4)
            self.assertEqual(type(storage.all()[placeObj_id].number_bathrooms),
                             int)
            self.assertEqual(stoarage.all()[placeObj_id].number_bathrooms, 2)
            self.assertEqual(type(storage.all()[placeObj_id].max_guest), int)
            self.assertEqual(FileStorage().all()[placeObj_id].max_guest, 10)
            self.assertEqual(type(storage.all()[placeObj_id].price_by_night),
                             int)
            self.assertEqual(storage.all()[placeObj_id].price_by_night, 300)
            self.assertEqual(type(FileStorage().all()[placeObj_id].latitude),
                             float)
            self.assertEqual(storage.all()[placeObj_id].latitude, 37.773972)
            self.assertEqual(type(storage().all()[placeObj_id].longitude),
                             float)
            self.assertEqual(storage.all()[placeObj_id].longitude, -122.431297)
            self.consol.onecmd('destroy User {}'.format(user_id))
            self.consol.onecmd('destroy City {}'.format(city_id))
            self.consol.onecmd('destroy State {}'.format(state_id))
            self.consol.onecmd('destroy Place {}'.format(pla_id))

    def test_show(self):
        """Test show command inpout"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("show")
            self.assertEqual(
                "** class name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("show asdfsdrfs")
            self.assertEqual(
                "** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("show BaseModel")
            self.assertEqual(
                "** instance id missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("show BaseModel abcd-123")
            self.assertEqual(
                "** no instance found **\n", f.getvalue())

    def test_destroy(self):
        """Test destroy command inpout"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("destroy")
            self.assertEqual(
                "** class name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("destroy Galaxy")
            self.assertEqual(
                "** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("destroy User")
            self.assertEqual(
                "** instance id missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("destroy BaseModel 12345")
            self.assertEqual(
                "** no instance found **\n", f.getvalue())

    def test_all(self):
        """Test all command inpout"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("all asdfsdfsd")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("all State")
            self.assertEqual("[]\n", f.getvalue())

    def test_update(self):
        """Test update command inpout"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("update")
            self.assertEqual(
                "** class name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("update sldkfjsl")
            self.assertEqual(
                "** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("update User")
            self.assertEqual(
                "** instance id missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("update User 12345")
            self.assertEqual(
                "** no instance found **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("all User")
            obj = f.getvalue()
        my_id = obj[obj.find('(')+1:obj.find(')')]
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("update User " + my_id)
            self.assertEqual(
                "** attribute name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("update User " + my_id + " Name")
            self.assertEqual(
                "** value missing **\n", f.getvalue())

    def test_z_all(self):
        """Test alternate all command input"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("asdfsdfsd.all()")
            self.assertEqual(
                "** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("State.all()")
            self.assertNotEqual("[]\n", f.getvalue())

    def test_z_count(self):
        """Test count command input"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("asdfsdfsd.count()")
            self.assertEqual(
                "** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("State.count()")
            self.assertEqual("1\n", f.getvalue())

    def test_z_show(self):
        """Test alternate show command input"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("safdsa.show()")
            self.assertEqual(
                "** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("BaseModel.show(abcd-123)")
            self.assertEqual(
                "** no instance found **\n", f.getvalue())

    def test_destroy(self):
        """Test alternate destroy command input"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("Galaxy.destroy()")
            self.assertEqual(
                "** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("User.destroy(12345)")
            self.assertEqual(
                "** no instance found **\n", f.getvalue())

    def test_update(self):
        """Test alternate destroy command inpout"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("sldkfjsl.update()")
            self.assertEqual(
                "** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("User.update(12345)")
            self.assertEqual(
                "** no instance found **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("all User")
            obj = f.getvalue()
        my_id = obj[obj.find('(')+1:obj.find(')')]
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("User.update(" + my_id + ")")
            self.assertEqual(
                "** attribute name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("User.update(" + my_id + ", name)")
            self.assertEqual(
                "** value missing **\n", f.getvalue())

if __name__ == "__main__":
    unittest.main()
