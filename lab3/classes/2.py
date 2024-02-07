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


sq = Square(5)
print(sq.shape_area)
