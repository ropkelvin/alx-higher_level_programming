#!/usr/bin/python3
"""
Inherits from list
"""


class MyList(list):
    """
    This class extends the built-in list class
    and provides a method to print the items in a sorted order.
    """

    def print_sorted(self):
        """
        Sorts the list and prints the items in ascending order.
        """
        print(sorted(self))
