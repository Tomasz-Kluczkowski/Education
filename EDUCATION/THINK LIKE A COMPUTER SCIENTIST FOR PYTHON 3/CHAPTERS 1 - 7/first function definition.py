#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Kilthar
#
# Created:     21-01-2017
# Copyright:   (c) Kilthar 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import turtle

def draw_square(t,sz):
    """first function definition, parameter t is substituted by turtle alex, parameter sz is the side of the square"""
    for i in range(4):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Alex meets function")

alex = turtle.Turtle()
alex.speed(1)

draw_square(alex,50)
draw_square(alex,100)

wn.mainloop()
