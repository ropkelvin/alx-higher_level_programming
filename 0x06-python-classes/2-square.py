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
