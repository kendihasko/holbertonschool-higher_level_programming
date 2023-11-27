#!/usr/bin/python3
"""
This module provides the Rectangle class, which inherits from Base.
"""

from models.base import Base


class Rectangle(Base):
    """
    Rectangle class inherits from Base.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle instance.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int, optional): X-coordinate of rectangle's position. Default=0
            y (int, optional): Y-coordinate of rectangle's position. Default=0
            id (int, optional): Identifier for rectangle. Defaults=None
        """
        super().__init__(id)

        self.check_integer_parameter(width, 'width')
        self.check_integer_parameter(height, 'height')
        self.check_integer_parameter(x, 'x')
        self.check_integer_parameter(y, 'y')

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Getter method for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width."""
        self.check_integer_parameter(value, 'width')
        self.__width = value

    @property
    def height(self):
        """Getter method for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height."""
        self.check_integer_parameter(value, 'height')
        self.__height = value

    @property
    def x(self):
        """Getter method for x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter method for x."""
        self.check_integer_parameter(value, 'x')
        self.__x = value

    @property
    def y(self):
        """Getter method for y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter method for y."""
        self.check_integer_parameter(value, 'y')
        self.__y = value

    def check_integer_parameter(self, value, parameter_name):
        """
        Validates if a parameter is an integer.

        Args:
            value: The value to check.
            parameter_name (str): The name of the parameter.

        Raises:
            TypeError: If the value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError(f"{parameter_name} must be an integer")
