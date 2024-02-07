class Shape:
    def __init__(self):
        self.shape_area = 0

    def area(self):
        print(self.shape_area)

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        self.shape_area = self.length * self.length

class Rectangle(Square):
    def __init__(self, length, width):
        super().__init__(length)
        self.length = length
        self.width = width

    def area(self):
        self.shape_area = self.length * self.width


sq = Square(5)
rec = Rectangle(10, 20)
print(rec.shape_area)
rec.area()
print(rec.shape_area)
