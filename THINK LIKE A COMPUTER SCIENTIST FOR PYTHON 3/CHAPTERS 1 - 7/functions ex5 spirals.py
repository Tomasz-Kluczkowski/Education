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
draw 2 spirals, they only differ by rotation angle so make it universal
We start from length 0 , increase length,
rotate right 90 and add angle given to the function
"""


import turtle
__import__("turtle").__traceable__ = False

def spiral(t,number, angle):
    """t - turtle, number - number of times spiral rotates,
       angle - rotation angle of entire spiral"""


    for n in range(number):

        t.forward(0+10*n)
        t.right(90-angle)


wn = turtle.Screen()        # set up window
wn.bgcolor("green")
wn.title("Moving square")

tom = turtle.Turtle() # set up our turtle
tom.color("red")
tom.speed(10)


""" call our funtion and draw a spiral using turtle tom,
number of sides and additional rotation angle"""

spiral(tom, 100, 1)

wn.mainloop()
