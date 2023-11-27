#!/usr/bin/python3

'''
Base class manages id attribute of all classes that extend from Base.
'''

# Importing libraries
from os import path
import json


class Base:
    __nb_objects = 0
    """
    ...
    """
    def __init__(self, id=None):

        if id is not None:
            # If id  provided, assign to public instance attribute id
            self.id = id

        else:
            Base.__nb_objects += 1
            # If id  not provided, increment and assign the new value to id
            self.id = Base.__nb_objects
