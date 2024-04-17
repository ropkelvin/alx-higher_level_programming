#!/usr/bin/python3
'''
 function that creates an Object from a “JSON file”:
'''
import json


def load_from_json_file(filename):
    """
    Load data from a JSON file.

    This function opens a file with the given filename,
    reads the JSON data from it, and returns the data.

    Args:
        filename (str): The name of the file to be read.

    Returns:
        The data read from the JSON file.
    """
    with open(filename, mode='r', encoding='utf-8') as a_file:
        return json.load(a_file)
