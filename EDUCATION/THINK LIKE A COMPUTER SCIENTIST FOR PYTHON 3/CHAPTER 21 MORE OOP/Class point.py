class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        """Dot product of multiplying vectors"""
        return self.x * other.x + self.y * other.y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def __rmul__(self, other):
        """Scalar multiplication"""
        return Point(other * self.x, other * self.y)


p1 = Point(3, 4)
p2 = Point(5, 7)
print(p1 * p2)
print(2 * p2)


