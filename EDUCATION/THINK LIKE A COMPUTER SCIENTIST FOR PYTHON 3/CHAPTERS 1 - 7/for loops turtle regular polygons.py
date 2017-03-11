#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Kilthar
#
# Created:     20-01-2017
# Copyright:   (c) Kilthar 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
"""
Use for loops to make a turtle draw these regular polygons (regular means all sides the same lengths, all angles the same):
An equilateral triangle
A square
A hexagon (six sides)
An octagon (eight sides)
"""
import turtle

wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Polygons using for loop")

triangle = turtle.Turtle()
triangle.speed(1)

for i in range(3):
    triangle.forward(100)
    triangle.left(120)



square = turtle.Turtle()
square.color("blue")
square.speed(1)

for i in range(4):
    square.forward(200)
    square.left(90)

hexagon = turtle.Turtle()
hexagon.color("pink")
hexagon.speed(1)

for i in range(6):
    hexagon.forward(300)
    hexagon.left(60)

octagon = turtle.Turtle()
octagon.color("green")
octagon.speed(1)

for i in range(8):
    octagon.forward(150)
    octagon.left(45)




wn.mainloop()
