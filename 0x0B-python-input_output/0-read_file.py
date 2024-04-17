#!/usr/bin/python3
'''
 function that reads a text file (UTF8) and prints it to stdout
'''


def read_file(filename=""):
    """
    Reads and prints the content of a file.

    Args:
        filename (str): The name of the file to be read.
        Defaults to an empty string.

    """
    with open(filename, mode='r', encoding='utf-8') as a_file:
        print(a_file.read())
