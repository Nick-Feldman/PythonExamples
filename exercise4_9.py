'''
Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which
 can compute the area.
'''

class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        area = self.length * self.width
        return area

rect = Rectangle(4, 5)


print(rect.area())
