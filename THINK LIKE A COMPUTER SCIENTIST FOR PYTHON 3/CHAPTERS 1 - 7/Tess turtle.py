#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Kilthar
#
# Created:     19-01-2017
# Copyright:   (c) Kilthar 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import turtle
wn_bg_color = input("Please specify background color")
tess_color = input("Please specify turtle's color")
tess_pensize = input("Please specify turtle's pensize")

wn = turtle.Screen()
wn.bgcolor(wn_bg_color)
wn.title("Hello, Tess!")

"""tess = turtle.Turtle()
tess.color(tess_color)
tess.pensize(int(tess_pensize))

tess.forward(50)
tess.left(120)
tess.forward(50)"""

alex = turtle.Turtle()
alex.color(tess_color)
alex.pensize(int(tess_pensize))

for i in range(4):
    alex.forward(50)
    alex.left(90)

test_turtle = alex

wn.mainloop()
