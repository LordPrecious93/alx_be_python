# polymorphism_demo.py
import math

class Shape:
    """Base class for shapes."""
    
    def area(self):
        """Method to be overridden in subclasses."""
        raise NotImplementedError("Subclass must implement this method")

class Rectangle(Shape):
    """Rectangle class inherits from Shape."""
    
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Override the area method to calculate the area of a rectangle."""
        return self.length * self.width

class Circle(Shape):
    """Circle class inherits from Shape."""
    
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Override the area method to calculate the area of a circle."""
        return math.pi * self.radius ** 2

