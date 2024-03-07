class Rectangle:
    def __init__(self, height, width):
        if height <= 0:
            raise NonPositiveDigitException("The height mast be more then 0")
        elif width <= 0:
            raise NonPositiveDigitException("The width mast be more then 0")
        else:
            self.height = height
            self.width = width

    def rectArea(self):
        return self.height * self.width

class NonPositiveDigitException(ValueError):
    pass