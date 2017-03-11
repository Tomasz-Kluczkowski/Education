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
draw a pretty spiral of squares
WE CAN DIVIDE the main object into 4 squares joined together and the rotated by 360/number of squares
in our case 20. Rotation angle is 360/20 = 18
"""


import turtle
__import__("turtle").__traceable__ = False

def spiral_square(t,number):
    """t - turtle, number - number of times a set of 4 squares must be drawn"""

           # draw the given amount of squares

    for n in range(number):



        for i in range(4):

            t.forward(100)
            t.left(90)

        """rotate each following square by 360 / number of squares drawn"""

        t.left(360/number)


wn = turtle.Screen()        # set up window
wn.bgcolor("green")
wn.title("Moving square")


tom = turtle.Turtle() # set up our turtle
tom.color("red")
tom.speed(10)

spiral_square(tom, 20) # call our funtion and draw number of squares

wn.mainloop()
