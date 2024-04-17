#!/usr/bin/python3
'''
function that appends a string at the end of a text file (UTF8)
and returns the number of characters added
'''


def append_write(filename="", text=""):
    """
    Appends the provided text to a file
    and returns the number of characters written.

    Args:
        filename (str): The name of the file to be appended to.
                        Defaults to an empty string.
        text (str): The text to be appended to the file.
                    Defaults to an empty string.

    Returns:
        int: The number of characters that were written to the file.
    """
    with open(filename, mode='a', encoding='utf-8') as a_file:
        return a_file.write(text)
