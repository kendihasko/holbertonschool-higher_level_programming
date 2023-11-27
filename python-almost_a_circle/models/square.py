#!/usr/bin/python3
'''
This module provides the Square class, which inherits from Rectangle.
'''

from models.rectangle import Rectangle


class Square(Rectangle):
    '''
    Square class inherits from Rectangle.
    '''

    def __init__(self, size, x=0, y=0, id=None):
        '''
        Initializes a Square instance.

        Args:
            size (int): Size of the square.
            x (int, optional): X-coordinate of square's position. Default=0
            y (int, optional): Y-coordinate of square's position. Default=0
            id (int, optional): Identifier for square. Defaults=None
        '''
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        '''Getter method for size.'''
        return self.width

    @size.setter
    def size(self, value):
        '''Setter method for size.'''
        self.width = value
        self.height = value

    def __str__(self):
        '''Returns a string representation of the Square instance.'''
        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.size}'
