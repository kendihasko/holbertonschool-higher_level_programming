#!/usr/bin/python3
"""
...
"""

from models.base import Base


class Rectangle(Base):
    """
    ...
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        ...
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
