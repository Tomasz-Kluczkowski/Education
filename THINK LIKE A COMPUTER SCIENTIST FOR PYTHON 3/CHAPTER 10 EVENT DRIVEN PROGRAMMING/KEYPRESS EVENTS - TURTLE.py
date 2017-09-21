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
wn.title("Handling keypresses!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
p_size = 1 # initial pen size for tess

# event handlers functions

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


def tess_red():
    tess.color("red")


def tess_green():
    tess.color("green")


def tess_blue():
    tess.color("blue")


def tess_pen_size_up():
    global p_size       # use global variable p_size
    if p_size < 20:
        p_size += 1
        tess.pensize(p_size)


def tess_pen_size_down():
    global p_size       # use global variable p_size
    if p_size > 1:
        p_size -= 1
        tess.pensize(p_size)


def tess_draw_circle():
    tess.circle(100)

# next lines "wire up" keypreses to the handling functions
wn.onkey(h1, "Up")
wn.onkey(h2, "Left")
wn.onkey(h3, "Right")
wn.onkey(h4, "Escape")
wn.onkey(h5, "Down")
wn.onkey(tess_red, "r")
wn.onkey(tess_green, "g")
wn.onkey(tess_blue, "b")
wn.onkey(tess_pen_size_up, "+")
wn.onkey(tess_pen_size_down, "-")
wn.onkey(tess_draw_circle, "c")



# now we tell window to start listening for events
# if any of the keys that we're monitoring is pressed, its handler will be called.

wn.listen()
wn.mainloop()

