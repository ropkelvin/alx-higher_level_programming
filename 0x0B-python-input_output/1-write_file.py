#!/usr/bin/python3
'''
 function that writes a string to a text file (UTF8)
 returns the number of characters written:
'''


def write_file(filename="", text=""):
    """
    Writes the provided text to a file.

    Args:
        filename (str): The name of the file to be written to.
                        Defaults to an empty string.
        text (str): The text to be written to the file.
                    Defaults to an empty string.

    """
    with open(filename, mode='w', encoding='utf-8') as a_file:
        a_file.write(text)
