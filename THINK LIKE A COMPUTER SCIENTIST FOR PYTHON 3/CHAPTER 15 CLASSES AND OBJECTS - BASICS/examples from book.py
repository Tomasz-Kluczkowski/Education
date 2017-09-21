class Point:
    """ point class represents and manipulates x,y coords. """
    def __init__(self):
        """ Create a new point at the origin """
        self.x = 0
        self.y = 0

p = Point()
q = Point()

print(p.x, p.y, q.x, q.y)

print("(x={0}, y={1})".format(p.x, p.y))
distance_squared_from_origin = p.x * p.x + p.y * p.y