class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height


    def get_area(self):
        return self.width * self.height


class Square:
    def __init__(self, a):
        self.a = a

    def get_area_square(self):
        return self.a ** 2


class Circle:
    def __init__(self, r):
        self.r = r

    def get_area_circle(self):
        return 3.14 * self.r ** 2