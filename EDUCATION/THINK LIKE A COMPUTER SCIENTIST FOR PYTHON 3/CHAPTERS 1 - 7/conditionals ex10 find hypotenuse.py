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
"""Write a function find_hypot which, given the length of two sides
 of a right-angled triangle, returns the length of the hypotenuse.
 (Hint: x ** 0.5 will return the square root.) """

def find_hypot(len1, len2):

    "calulates the length of the hypotenuse of a right angled triangle with two sides len1 and len2 at the right angle side"

    hypot = ((len1**2)+(len2**2))**0.5
    return hypot

side1 = float(input("Please enter length of the first side:"))
side2 = float(input("Please enter length of the second side:"))

hypotenuse = find_hypot(side1,side2)

print("The lenght of the hypotenuse is:", hypotenuse)