#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      T Kluczlowski
#
# Created:     31/01/2017
# Copyright:   (c) T Kluczlowski 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import turtle

wn = turtle.Screen()
wn.bgcolor("blue")
wn.title("drunken pirate")

pirate = turtle.Turtle()
pirate.color("green")
pirate.pensize(4)
pirate.speed(1)

moves = [(160,230),(-43,100),(270,80),(-43,102)]

for (angle, steps) in moves:
    pirate.left(angle)
    pirate.forward(steps)

wn.mainloop()