#!/usr/bin/python3
'''
A module that tests different behaviors
of the Square class
'''
import unittest
import pep8
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    '''
    A class to test the Square Class
    '''

    def test_pep8_base(self):
        '''
        Test that checks PEP8
        '''
        style_checker = pep8.StyleGuide(quit=True)
        check_result = style_checker.check_files(['models/square.py'])
        self.assertEqual(
            check_result.total_errors, 0,
            'Found code style errors (and warnings).'
        )

    def test_getter(self):
        '''
        Test the getter method for size
        '''
        square_instance = Square(5)
        self.assertEqual(square_instance.size, 5)

    def test_setter(self):
        '''
        Test the setter method for size
        '''
        square_instance = Square(5)
        square_instance.size = 8
        self.assertEqual(square_instance.size, 8)

    def test_string(self):
        '''
        Test setting size with a string
        '''
        square_instance = Square(3)

        with self.assertRaises(TypeError):
            square_instance.size = "Hi"

    def test_negative(self):
        '''
        Test setting size with a negative value
        '''
        square_instance = Square(6)

        with self.assertRaises(ValueError):
            square_instance.size = -5

    def test_zero(self):
        '''
        Test setting size with a zero value
        '''
        square_instance = Square(6)

        with self.assertRaises(ValueError):
            square_instance.size = 0

    def test_decimal(self):
        '''
        Test setting size with a decimal value
        '''
        square_instance = Square(6)

        with self.assertRaises(TypeError):
            square_instance.size = 1.5

    def test_tuple(self):
        '''
        Test setting size with a tuple
        '''
        square_instance = Square(7)

        with self.assertRaises(TypeError):
            square_instance.size = (2, 8)

    def test_empty(self):
        '''
        Test setting size with an empty value
        '''
        square_instance = Square(7)

        with self.assertRaises(TypeError):
            square_instance.size = ''

    def test_none(self):
        '''
        Test setting size with None
        '''
        square_instance = Square(5)

        with self.assertRaises(TypeError):
            square_instance.size = None

    def test_list(self):
        '''
        Test setting size with a list
        '''
        square_instance = Square(4)

        with self.assertRaises(TypeError):
            square_instance.size = [4, 7]

    def test_dict(self):
        '''
        Test setting size with a dictionary
        '''
        square_instance = Square(5)

        with self.assertRaises(TypeError):
            square_instance.size = {"hi": 5, "world": 8}

    def test_width(self):
        '''
        Test updating width and height when changing size
        '''
        square_instance = Square(5)
        square_instance.size = 6
        self.assertEqual(square_instance.width, 6)
        self.assertEqual(square_instance.height, 6)

    def test_to_dictionary(self):
        '''
        Test the to_dictionary method
        '''
        Base._Base__nb_objects = 0

        square_instance = Square(10, 2, 1, 9)
        square_dict = square_instance.to_dictionary()
        expected = {'id': 9, 'x': 2, 'size': 10, 'y': 1}
        self.assertEqual(square_dict, expected)

        square_instance = Square(1, 0, 0, 9)
        square_dict = square_instance.to_dictionary()
        expected = {'id': 9, 'x': 0, 'size': 1, 'y': 0}
        self.assertEqual(square_dict, expected)

        square_instance.update(5, 5, 5, 5)
        square_dict = square_instance.to_dictionary()
        expected = {'id': 5, 'x': 5, 'size': 5, 'y': 5}
        self.assertEqual(square_dict, expected)

