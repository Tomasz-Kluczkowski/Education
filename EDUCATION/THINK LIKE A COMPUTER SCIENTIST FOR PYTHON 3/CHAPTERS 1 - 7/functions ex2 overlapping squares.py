#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Kilthar
#
# Created:     22-01-2017
# Copyright:   (c) Kilthar 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
"""
Write a void (non-fruitful) function to draw a square.
Use it in a program to draw the image shown below.
Assume each side is 20 units.
(Hint: notice that the turtle has already moved away from the ending point of the last square when the program ends.)
"""


import turtle
__import__("turtle").__traceable__ = False

def overlapping_square(t,number):
    """t - turtle, number - number of times a square must be drawn and overlap"""

    for n in range(number):     # draw the given amount of squares

        for i in range(4):      # draw a square which increases in size
            t.forward(20+40*n)
            t.left(90)

        """ this next set of lines moves us to the new location after drawing of each square
            note that the indentation means this instruction is carried
            out after the square is drawn - it is nested in the first
            for loop not the second """

        t.penup()
        t.right(90)
        t.forward(20)
        t.right(90)
        t.forward(20)
        t.right(180)
        t.pendown()


wn = turtle.Screen()        # set up window
wn.bgcolor("green")
wn.title("Moving square")


tom = turtle.Turtle() # set up our turtle
tom.color("red")
tom.speed(10)

overlapping_square(tom, 5) # call our funtion and draw number of squares

wn.mainloop()
