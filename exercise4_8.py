'''
Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area.
'''

import math
class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area =  self.radius ** 2 * math.pi
        return area

circle = Circle(5)

print(circle.area())
