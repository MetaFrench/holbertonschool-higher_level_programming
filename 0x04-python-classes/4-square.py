#!/usr/bin/python3
"""square class"""


class Square:
    """This class defines a square"""
    def __init__(self, size=0):
        """This initializes a square with a size"""
        self.size(size)
        # if type(size) != int:
        #     raise TypeError("size must be an integer")
        # if size < 0:
        #     raise ValueError("size must be >= 0")
        # self.__size = size

    def area(self):
        """Prints area"""
        return self.__size ** 2

    @property
    def size(self):
        """Getter for a square's size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for a square's size"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Method to print a square"""
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            print(self.__size * "#", end="")
            print()
