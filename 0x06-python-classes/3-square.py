#!/usr/bin/python3
'''
A class Square that defines a square
'''


class Square:
    '''
    Description for class square
    '''
    def __init__(self, size=0):
        '''
        Initializes a new Square object with a given size
        Args:
            size (int): The size of the square (default is 0)
        '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        '''
        Calculate the area of a square.

        Returns:
            int: The area of the square calculated as the square of the size.

        Example:
            If the size of the square is 5 units, the area will be 25 units^2.
        '''
        return self.__size ** 2
