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
wn = turtle.Screen()

clock = turtle.Turtle()
clock.speed(1)
# clock.hideturtle()
clock.shape("turtle")


for i in range(12):
    clock.penup()
    clock.forward(100)
    clock.pendown()
    clock.forward(25)
    clock.penup()
    clock.forward(25)
    clock.stamp()
    clock.penup()
    clock.forward(-150)
    clock.right(30)

wn.mainloop()
