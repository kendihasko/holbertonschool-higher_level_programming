#!/usr/bin/python3

'''
This module provides the Base class for managing the id attribute.
'''

# Importing libraries
from os import path
import json


class Base:
    '''
This docstring describes the Base class.
    '''

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            # If id  provided, assign to public instance attribute id
            self.id = id
        else:
            Base.__nb_objects += 1
            # If id  not provided, increment and assign the new value to id
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''Returns the JSON string representation of list_dictionaries.'''
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''Writes the JSON string representation of list_objs to a file.'''
        filename = cls.__name__ + ".json"
        json_string = cls.to_json_string(
           [obj.to_dictionary() for obj in list_objs]
        )
        with open(filename, 'w') as file:
            file.write(json_string)
