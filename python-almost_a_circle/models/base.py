#!/usr/bin/python3

"""
Contains a Base class to manage
the id attribute of all classes that extend
from Base.
"""

# Importing libraries
from os import path
import json

# Private class attribute
class Base:
    __nb_objects = 0

# If id is provided, assign it to the public instance attribute id
     def __init__(self, id=None):

         if id is not None:
         self.id = id

      # If id  not provided, increment and assign the new value to id 
         else:
             Base.__nb_objects += 1
             self.id = Base.__nb_objects

