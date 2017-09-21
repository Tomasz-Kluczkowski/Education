class Point:
    """ Point classs represents and manipulates x, y coords """
    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y


    def distance_from_origin(self):
        """ Compute my distance from the origin """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5


    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)


    def halfway(self, target):
        """ Return the halfway point between myself and the target """
        mx = (self.x + target.x) / 2
        my = (self.y + target.y) / 2
        return Point(mx, my)


    def reflect_x(self):
        """ Return reflection of the point about the X axis """
        return Point(self.x, -self.y)


    def slope_from_origin(self):
        """ Return the slope from origin to the point """
        return self.y / self.x


    def get_line_to_point(self, target):
        """ Return coefficients a and b of a line joining two points (y = ax + b)"""
        a = (target.y - self.y) / (target.x - self.x)
        b = target.y - a * target.x
        return (a, b)


    def mid_circle(self,p2,p3,p4):
        """ Finds and returns a mid point of a circle to which four points self,p2,p3,p4 belong """
        line1_parameters = self.get_line_to_point(p2)
        line1_halfpoint = self.halfway(p2)
        a_p1 = -1/line1_parameters[0]
        b_p1 = line1_halfpoint.y - a_p1 * line1_halfpoint.x

        line2_parameters = p3.get_line_to_point(p4)
        line2_halfpoint = p3.halfway(p4)
        a_p2 = -1/line2_parameters[0]
        b_p2 = line2_halfpoint.y - a_p2 * line2_halfpoint.x

        intersect_x = round(((b_p1 - b_p2) / (a_p2 - a_p1)), 2)
        intersect_y = round(((a_p2 * intersect_x + b_p2)), 2)

        intersect_point = Point(intersect_x, intersect_y)

        return intersect_point


class Rectangle:
    """ A class to manufacture rectangle objects """

    def __init__(self, posn, w, h):
        """ Initialize rectangle at posn, with width w, height h """
        self.corner = posn
        self.width = w
        self.heigth = h

    def __str__(self):
        return "({0}, {1}, {2})".format(self.corner, self.width, self.heigth)


    def grow(self, delta_width, delta_height):
        """ Grow or shrink this object by the deltas """
        self.width += delta_width
        self.heigth += delta_height


    def move(self, dx, dy):
        """ Move this object by the deltas """
        self.corner.x += dx
        self.corner.y += dy



def same_coordinates(p1, p2):
    return (p1.x == p2.x) and (p1.y == p2.y)





box = Rectangle(Point(0, 0), 100, 200)
bomb = Rectangle(Point(100, 80), 5, 10)
print("box: ", box)
print("bomb: ", bomb)
