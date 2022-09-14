#!/usr/bin/python3
""" 0-rectangle Module """


class Rectangle():
    """This class defines a rectangle"""
    def __init__(self, width=0, height=0):
        """This initializes a rectangle with a width and height"""
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if 0 in (self.__width, self.__height):
            return 0
        return 2*self.__width + 2*self.
