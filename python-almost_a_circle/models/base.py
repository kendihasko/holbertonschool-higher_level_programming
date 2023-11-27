#!/usr/bin/python3

# Importing libraries
from os import path
import json

"""
Base class manages
id attribute of all classes that extend
from Base.
"""

class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id  # If id  provided, assign to public instance attribute id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects  # If id  not provided, increment and assign the new value to id
