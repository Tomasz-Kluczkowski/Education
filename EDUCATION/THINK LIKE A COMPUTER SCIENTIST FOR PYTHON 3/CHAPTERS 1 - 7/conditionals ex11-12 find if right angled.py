#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Kilthar
#
# Created:     25-01-2017
# Copyright:   (c) Kilthar 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
"""Write a function is_rightangled which, given the length of three sides of a
 triangle, will determine whether the triangle is right-angled.
 Assume that the third argument to the function is always the longest side.
 It will return True if the triangle is right-angled, or False otherwise.

Hint: Floating point arithmetic is not always exactly accurate,
 so it is not safe to test floating point numbers for equality.
 If a good programmer wants to know whether x is equal or close enough to y,
  they would probably code it up as:

if  abs(x-y) < 0.000001:    # If x is approximately equal to y
    ...
Extend the above program so that the sides can be given to
the function in any order."""


def is_rightangled(side1,side2,side3):

    "checks if the triangle is right angled using pythagorean theorem c^2 = a^2 + b^2"
    c_side = max(side1,side2,side3)

    """we have to decide which of the variables is the maximum one, since we have not learned about
    obtaining index of a value in a list we have to do it the hard way and check for the variables value and determine which one it is"""

    if  c_side == side1:     # checks if side1 is the longest side

        a_side = side2
        b_side = side3
        return abs(c_side**2-(a_side**2+b_side**2)) < 0.000001

    elif c_side == side2:    # checks if side2 is the longest side

        a_side = side1
        b_side = side3
        return abs(c_side**2-(a_side**2+b_side**2)) < 0.000001

    else:                    # checks if side3 is the longest side

        a_side = side1
        b_side = side2
        return abs(c_side**2-(a_side**2+b_side**2)) < 0.000001



side1 = float(input("Please enter length of side1:"))
side2 = float(input("Please enter length of side2:"))
side3 = float(input("Please enter length of side3:"))

if is_rightangled(side1,side2,side3):
    print("The triangle is right angled")

else:

    print("The triangle is not right angled")


