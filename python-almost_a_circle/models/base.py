#!/usr/bin/python3
#!/usr/bin/python3
"""

Contains a Base class to manage
the id attribute of all classes that extend
from Base.

"""
from os import path
import json

""" Private class attribute """

class Base:
    __nb_objects = 0


    def __init__(self, id=None):
        if id is not None:
            # If id is provided, assign it to the public instance attribute id
            self.id = id
        else:
            # If id is not provided, increment __nb_objects and assign the new value to id
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
