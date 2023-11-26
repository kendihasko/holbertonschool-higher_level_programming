
#!/usr/bin/python3

# Importing libraries
from os import path
import json

"""
Base class manages
id attribute of all classes that extend
from Base.
"""

# Private class attribute

class Base:
    __nb_objects = 0

# If id  provided, assign to public instance attribute id
    def __init__(self, id=None):

        if id is not None:
            self.id = id

         # If id  not provided, increment and assign the new value to id
         else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
