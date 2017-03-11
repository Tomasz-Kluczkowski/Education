from unit_testing import test


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
        self.height = h

    def __str__(self):
        return "({0}, {1}, {2})".format(self.corner, self.width, self.height)


    def grow(self, delta_width, delta_height):
        """ Grow or shrink this object by the deltas """
        self.width += delta_width
        self.height += delta_height


    def move(self, dx, dy):
        """ Move this object by the deltas. """
        self.corner.x += dx
        self.corner.y += dy


    def area(self):
        """ Returns area of the rectangle. """
        return self.width * self.height


    def perimeter(self):
        """ Returns perimeter of the rectangle. """
        return 2 * (self.width + self.height)


    def flip(self):
        """ Swaps width with height """
        (self.width, self.height) = (self.height, self.width)


    def contains(self, p1):
        """ Returns True if p1 is within the rectangle """
        return ((p1.x >= self.corner.x and p1.x < (self.corner.x + self.width)) and
               (p1.y >= self.corner.y and p1.y < (self.corner.y + self.height)))

    def collides(self, r1):
        """ Returns True if two rectangles overlap. We assume they have open upper bounds """
        # we have to detect which rectangle is smaller to check if its points
        # are included in the bigger one as it may be entirely within the bigger one
        rec1 = self
        rec2 = r1
        if self.area() < rec2.area():       # if r1 is bigger than self swap them around for further checking
            (rec1, rec2) = (rec2, rec1)

        # now we have to check if corners of the smaller rectangle belong within the bigger one
        right_x = rec2.corner.x + rec2.width - 0.000001     # the right side is open bound so never reaches the x + width x coordinate
        bottom_y = rec2.corner.y + rec2.height - 0.000001 # the bottom side is open bound so never reaches the y + height y coordinate

        # top - left corner
        if rec1.contains(rec2.corner):
            return True
        # top - right corner
        elif rec1.contains(Point(right_x, rec2.corner.y)):
            return True
        # bottom - left corner
        elif rec1.contains(Point(rec2.corner.x, bottom_y)):
            return True
        # bottom - right corner
        elif rec1.contains(Point(right_x, bottom_y)):
            return True
        else:
            return False





def same_coordinates(p1, p2):
    return (p1.x == p2.x) and (p1.y == p2.y)


box = Rectangle(Point(0, 0), 100, 200)
bomb = Rectangle(Point(100, 80), 5, 10)
print("box: ", box)
print("bomb: ", bomb)
r = Rectangle(Point(0,0), 10, 5)
test(r.area(), 50)
test(r.perimeter(), 30)
test((r.width == 10 and r.height == 5), True)
r.flip()
test((r.width == 5 and r.height == 10), True)
r = Rectangle(Point(0, 0), 10, 5)
test(r.contains(Point(0, 0)), True)
test(r.contains(Point(3, 3)), True)
test(not r.contains(Point(3, 7)), True)
test(not r.contains(Point(3, 5)), True)
test(r.contains(Point(3, 4.999999)), True)
test(not r.contains(Point(-3, -3)), True)
rec1 = Rectangle(Point(1,1), 4, 3)
rec2 = Rectangle(Point(3,2), 1, 1)
test(rec1.collides(rec2), True)