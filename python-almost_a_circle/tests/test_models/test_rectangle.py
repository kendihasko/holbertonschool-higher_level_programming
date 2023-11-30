#!/usr/bin/python3
'''
A module that tests different behaviors
of the Base class
'''
import unittest
import pep8
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    '''
    A class to test the Rectangle Class
    '''
    def test_pep8_base(self):
        '''
        Test that checks PEP8
        '''
        style_checker = pep8.StyleGuide(quit=True)
        check_result = style_checker.check_files(['models/rectangle.py'])
        self.assertEqual(
            check_result.total_errors, 0,
            'Found code style errors (and warnings).'
        )

    def test_rectangle_subclass(self):
        '''
        Test if Rectangle class inherits from
        Base class
        '''
        self.assertTrue(issubclass(Rectangle, Base))

    def test_parameters(self):
        '''
        Test parameters for Rectangle class
        '''
        rect1 = Rectangle(10, 2)
        rect2 = Rectangle(2, 10)
        rect3 = Rectangle(10, 2, 0, 0, 12)

        self.assertEqual(rect1.id, 4)
        self.assertEqual(rect1.width, 10)
        self.assertEqual(rect1.height, 2)
        self.assertEqual(rect1.x, 0)
        self.assertEqual(rect1.y, 0)
        self.assertEqual(rect2.id, 5)
        self.assertEqual(rect2.width, 2)
        self.assertEqual(rect2.height, 10)
        self.assertEqual(rect2.x, 0)
        self.assertEqual(rect2.y, 0)
        self.assertEqual(rect3.id, 12)
        self.assertEqual(rect3.width, 10)
        self.assertEqual(rect3.height, 2)
        self.assertEqual(rect3.x, 0)
        self.assertEqual(rect3.y, 0)

        with self.assertRaises(TypeError):
            rect4 = Rectangle()

    def test_string(self):
        '''
        Test string parameters for a
        Rectangle class
        '''
        with self.assertRaises(TypeError):
            Rectangle('Purple', 'Violet')

    def test_type_param(self):
        '''
        Test different types of parameters
        for a Rectangle class
        '''
        with self.assertRaises(TypeError):
            Rectangle(1.01, 3)
            raise TypeError()

        with self.assertRaises(ValueError):
            Rectangle(-234234242, 45)
            raise ValueError()

        with self.assertRaises(TypeError):
            Rectangle('Purple', 4)
            raise TypeError()

        with self.assertRaises(TypeError):
            Rectangle(True, 4)
            raise TypeError()

        with self.assertRaises(TypeError):
            Rectangle(5, 1.76)
            raise TypeError()

        with self.assertRaises(TypeError):
            Rectangle(5, "Red")
            raise TypeError()

        with self.assertRaises(TypeError):
            Rectangle(5, False)
            raise TypeError()

        with self.assertRaises(ValueError):
            Rectangle(5, -4798576398576)
            raise ValueError

        with self.assertRaises(TypeError):
            Rectangle(5, 1, 1.50)
            raise TypeError()

        with self.assertRaises(TypeError):
            Rectangle(5, 6, 'Blue')
            raise TypeError()

        with self.assertRaises(TypeError):
            Rectangle(5, 7, False)
            raise TypeError()

        with self.assertRaises(ValueError):
            Rectangle(5, 7, -4798576398576)
            raise ValueError()

        with self.assertRaises(TypeError):
            Rectangle(5, 1, 1, 1.53)
            raise TypeError()

        with self.assertRaises(TypeError):
            Rectangle(5, 6, 5, 'Blue')
            raise TypeError()

        with self.assertRaises(TypeError):
            Rectangle(5, 7, 7, False)
            raise TypeError()

        with self.assertRaises(ValueError):
            Rectangle(5, 9, 5, -4798576398576)
            raise ValueError()
