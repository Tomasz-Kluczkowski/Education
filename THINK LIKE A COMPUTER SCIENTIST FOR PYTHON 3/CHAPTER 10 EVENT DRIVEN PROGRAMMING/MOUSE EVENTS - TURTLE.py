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
wn.title("How to handle mouse clicks on the window!")
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("purple")
tess.pensize(3)
tess.shape("circle")

# event handlers functions

def move_to_click(x, y):
    wn.title("Got mouse click at coords {0}, {1}".format(x, y))
    tess.goto(x, y)

def h1():
    tess.forward(30)


def h2():
    tess.left(30)

def h3():
    tess.right(30)

def h4():
    wn.bye()            # close down turtle window

def h5():
    tess.backward(30)

# next lines "wire up" keypreses to the handling functions
wn.onkey(h1, "Up")
wn.onkey(h2, "Left")
wn.onkey(h3, "Right")
wn.onkey(h4, "Escape")
wn.onkey(h5, "Down")
wn.onclick(move_to_click)

# now we tell window to start listening for events
# if any of the keys that we're monitoring is pressed, its handler will be called.

wn.listen()
wn.mainloop()

