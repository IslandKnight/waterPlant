

class SqTank:
    """A square tank or a rectangular tank"""
    def __init__(self, width, length, height):
        self.width = width
        self.length = length
        self.height = height
        self.volume = width * length * height
        self.area = width * length
        self.description = "Replace with tank description"
        self.operating_volume = (width * length * height) * .90

    def __str__(self):
        return f'The tank has a width of {self.width} a length of {self.length} and a height of {self.height},' \
               f'which gives a max volume of {self.volume} and an operating volume of {self.operating_volume}'
