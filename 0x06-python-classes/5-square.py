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
        self.size = size

    @property
    def size(self):
        '''
        Getter method to retrieve the size of the square.
        '''
        return self.__size

    @size.setter
    def size(self, value):
        '''
        Setter method to set the size of the square.
        Args:
            value (int): The new size value to set
        If size is 0, prints a newline.
        '''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        if value == 0:
            print('\n')
        self.__size = value

    def area(self):
        '''
        Calculate the area of a square.

        Returns:
            int: The area of the square calculated as the square of the size.

        Example:
            If the size of the square is 5 units, the area will be 25 units^2.
        '''
        return self.__size ** 2

    def my_print(self):
        """
        Print a square pattern based on the size attribute.

        If size is greater than 0,
        prints a square pattern of '#' based on the size.
        """

        if self.__size > 0:
            for i in range(self.__size):
                print('#' * self.__size)
