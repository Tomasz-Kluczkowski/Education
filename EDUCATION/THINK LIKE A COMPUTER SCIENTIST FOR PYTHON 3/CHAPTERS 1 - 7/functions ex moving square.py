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

def moving_square(t,number):
    """t - turtle, number - number of times a square must be drawn"""

    for n in range(number):     # draw the given amount of squares

        for i in range(4):      # draw a square
            t.forward(20)
            t.left(90)

        t.penup()           # this moves us to the new location after drawing of each square
        t.forward(50)       # note that the indentation means this instruction is carried
        t.pendown()         # out after the square is drawn - it is nested in the first
                            # for loop not the second

wn = turtle.Screen()        # set up window
wn.bgcolor("green")
wn.title("Moving square")


tom = turtle.Turtle() # set up our turtle
tom.color("red")

moving_square(tom, 5) # call our funtion and draw 5 squares

wn.mainloop()
