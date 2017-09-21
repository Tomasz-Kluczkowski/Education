#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Kilthar
#
# Created:     23-01-2017
# Copyright:   (c) Kilthar 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def circle_area(r):

    """calculates area of a cricle of radius r"""
    area = 3.14159*(r**2)
    return area

radius = float(input("Please enter radius"))

area_c = circle_area(radius)

print("The area of a circle of radius", radius, "=", area_c)
