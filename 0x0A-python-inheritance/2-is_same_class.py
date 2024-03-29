#!/usr/bin/python3
"""Determines if an object is an instance of a specific class."""


def is_same_class(obj, a_class):
    """
    Returns True if the object is an instance of the specified class, otherwise returns False.
    """
    return type(obj) == a_class

