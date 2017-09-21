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
"""9. Write a void function to draw a star, where the length of each side is 100 units. (Hint:
You should turn the turtle by 144 degrees at each point.)"""
import turtle

def pentagram(t,number, dislocation, angle):
    """draw using turtle t, a number of pentagrams,
    dislocated from each other and with an angle between them"""

    for p in range(number):


        for i in range(5):
            t.forward(100)
            t.right(144)

        t.penup()
        t.forward(dislocation)
        t.right(angle)
        t.pendown()


wn = turtle.Screen()        # set up window
wn.bgcolor("green")
wn.title("pentagrams moving")

tom = turtle.Turtle() # set up our turtle
tom.color("red")
tom.speed(10)


""" call our funtion and draw pentagrams using turtle tom"""

pentagram(tom, 5, 350, 144)

wn.mainloop()
