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
import math


wn = turtle.Screen()
wn.bgcolor("blue")
wn.title("drunken pirate")

pirate = turtle.Turtle()
pirate.color("green")
pirate.pensize(4)
pirate.speed(1)

inside = 100*math.sqrt(2)

moves = [(0,100),(90,100),(90,100),(90,100),(135,inside),(90,inside/2),(90,inside/2),(90,inside)]

for (angle, steps) in moves:
    pirate.left(angle)
    pirate.forward(steps)

wn.mainloop()