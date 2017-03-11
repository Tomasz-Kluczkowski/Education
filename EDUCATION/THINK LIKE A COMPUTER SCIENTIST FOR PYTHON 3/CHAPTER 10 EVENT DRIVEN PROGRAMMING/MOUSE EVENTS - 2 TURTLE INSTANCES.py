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
wn.title("Handling mouse clicks!")
wn.bgcolor("lightgreen")

tess = turtle.Turtle()  # create two turtles
tess.color("purple")

alex = turtle.Turtle()
alex.color("blue")
alex.forward(100)       # separate turtles

# event handlers functions

def handler_for_tess(x, y):
    wn.title("Tess clicked at {0}, {1}".format(x, y))
    tess.left(42)
    tess.forward(30)

def handler_for_alex(x, y):
    wn.title("Alex clicked at {0}, {1}".format(x, y))
    alex.right(84)
    alex.forward(50)

tess.onclick(handler_for_tess)
alex.onclick(handler_for_alex)

wn.mainloop()

