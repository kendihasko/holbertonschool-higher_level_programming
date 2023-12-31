#!/usr/bin/python3
'''
A module that tests different behaviors
of the Base class
'''
import unittest
import pep8
import os
from test_models.test_base import Base
from test_models.test_rectangle import Rectangle
from test_models.test_square import Square


class TestBase(unittest.TestCase):
    '''
    A class to test the Base Class
    '''
    def test_pep8_base(self):
        '''
        Test that checks PEP8
        '''
        syntax = pep8.StyleGuide(quit=True)
        check = syntax.check_files(['models/base.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Found code style errors (and warnings)."
        )

    def test_id_positive(self):
        '''
        Test for a positive Base Class id
        '''
        base_instance = Base(123)
        self.assertEqual(base_instance.id, 123)
        base_instance = Base(456)
        self.assertEqual(base_instance.id, 456)

    def test_id_negative(self):
        '''
        Test for a negative Base Class id
        '''
        base_instance = Base(-789)
        self.assertEqual(base_instance.id, -789)
        base_instance = Base(-101112)
        self.assertEqual(base_instance.id, -101112)

    def test_id_none(self):
        '''
        Test for a None Base Class id
        '''
        base_instance = Base()
        self.assertEqual(base_instance.id, 1)
        base_instance = Base(None)
        self.assertEqual(base_instance.id, 2)

    def test_string_id(self):
        base_instance = Base('Guido van Rossum')
        self.assertEqual(base_instance.id, 'Guido van Rossum')
        base_instance = Base('Life is better with Python')
        self.assertEqual(base_instance.id, 'Life is better with Python')

    def test_to_json_string(self):
        '''
        Test the to_json_string method
        '''
        rect_instance = Rectangle(10, 7, 2, 8, 42)
        rect_data = rect_instance.to_dictionary()
        json_data = Base.to_json_string([rect_data])
        self.assertEqual(type(json_data), str)

    def test_empty_to_json_string(self):
        '''
        Test for empty data on the to_json_string method
        '''
        empty_data = []
        json_data = Base.to_json_string(empty_data)
        self.assertEqual(json_data, "[]")

        empty_data = None
        json_data = Base.to_json_string(empty_data)
        self.assertEqual(json_data, "[]")

    def test_instance(self):
        '''
        Test a Base Class instance
        '''
        base_instance = Base()
        self.assertEqual(type(base_instance), Base)
        self.assertTrue(isinstance(base_instance, Base))

    def test_normal_to_json_string(self):
        '''
        Test a normal to_json_string functionality
        '''
        rect_data = {'id': 42, 'x': 15, 'y': 10, 'width': 5, 'height': 5}
        json_data = Base.to_json_string([rect_data])

        self.assertTrue(isinstance(rect_data, dict))
        self.assertTrue(isinstance(json_data, str))
        self.assertCountEqual(
            json_data,
            '{{"id": 42, "x": 15, "y": 10, "width": 5, "height": 5}}'
        )

    def test_wrong_to_json_string(self):
        '''
        Test wrong functionality of the
        to_json_string method
        '''
        json_data = Base.to_json_string(None)
        self.assertEqual(json_data, "[]")

        warn = ("to_json_string() missing 1 required positional argument: " +
                "'list_dictionaries'")

        with self.assertRaises(TypeError) as msg:
            Base.to_json_string()

        self.assertEqual(warn, str(msg.exception))

        warn = "to_json_string() takes 1 positional argument but 2 were given"

        with self.assertRaises(TypeError) as msg:
            Base.to_json_string([{43, 87}], [{22, 17}])

        self.assertEqual(warn, str(msg.exception))

    def test_wrong_save_to_file(self):
        '''
        Test the save_to_file method
        '''
        with self.assertRaises(AttributeError) as msg:
            Base.save_to_file([Base(1), Base(2)])

        self.assertEqual(
             "'Base' object has no attribute 'to_dictionary'",
             str(msg.exception)
        )

    def test_load_from_file(self):
        '''
        Test the load_from_file method
        '''
        if os.path.exists("Base.json"):
            os.remove("Base.json")

        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

        if os.path.exists("Square.json"):
            os.remove("Square.json")

        rect_output = Rectangle.load_from_file()
        self.assertEqual(rect_output, [])

        square_output = Square.load_from_file()
        self.assertEqual(square_output, [])

        warn = "load_from_file() takes 1 positional argument but 2 were given"

        with self.assertRaises(TypeError) as msg:
            Rectangle.load_from_file('Guido van Rossum')

        self.assertEqual(warn, str(msg.exception))

    def test_create(self):
        '''
        Test the create method
        '''
        with self.assertRaises(TypeError) as msg:
            warn = Rectangle.create('Guido van Rossum')

        self.assertEqual(
            "create() takes 1 positional argument but 2 were given",
            str(msg.exception)
        )

