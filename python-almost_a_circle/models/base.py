#!/usr/bin/python3

# Importing libraries
from os import path
import json

class Base:
    """Base class for managing id attribute.

    Attributes:
        __nb_objects (int): A private class attribute to keep track of the number of instances.

    Args:
        id (int, optional): The id to assign to the instance. If None, a new id is generated.

    Attributes:
        id (int): The public instance attribute representing the id.

    Methods:
        __init__: Initializes a new instance of the Base class.

    Example:
        Create an instance with a specific id:
        >>> b = Base(id=5)
        >>> print(b.id)
        5

        Create an instance with a generated id:
        >>> b = Base()
        >>> print(b.id)
        1
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a new instance of the Base class.

        Args:
            id (int, optional): The id to assign to the instance. If None, a new id is generated.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

