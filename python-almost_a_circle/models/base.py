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
    '''
    Writes the JSON string representation of list_objs to a file.

    Args:
        cls (class): The class itself, used to access class-level methods and attributes.
        list_objs (list): List of instances that inherit from the class.

    Returns:
        int: The number of characters written to the file.

    Description:
        This method writes the JSON string representation of the instances in the
        list_objs to a file. If list_objs is None, it writes an empty list ("[]")
        as a JSON string to ensure that the file exists and contains valid JSON
        syntax, even if there are no instances to serialize.

        Note:
        If list_objs is None, an empty list is passed to cls.to_json_string([])
        to ensure proper handling of edge cases.
    '''
    filename = cls.__name__ + '.json'

    with open(filename, mode='w', encoding='utf-8') as f:
        if list_objs is None:
            return f.write(cls.to_json_string([]))

        json_attrs = [obj.to_dictionary() for obj in list_objs]

        return f.write(cls.to_json_string(json_attrs))
