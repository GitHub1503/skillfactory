class Rectangle:
    def __init__(self, x, y, height, width):
        self.x = x
        self.y = y
        self.height = height
        self.width = width

    def __str__(self):
        return f'Rectangle: {self.x}, {self.y}, {self.height}, {self.width}'