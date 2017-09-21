#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      T Kluczlowski
#
# Created:     07/02/2017
# Copyright:   (c) T Kluczlowski 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import turtle

turtle.setup(400,500) #window size
wn = turtle.Screen()
wn.title("Using a timer to get events")
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("purple")


def h1():
    tess.forward(100)
    tess.left(56)
    wn.ontimer(h1, 60)

h1()
wn.mainloop()

