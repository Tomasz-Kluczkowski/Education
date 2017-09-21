# This function allows creation of turtle generated polygons

def polygon_gen(t, n_s, size, c):
	"""where t - turtle, n_s - number of polygon's sides, size - size of the side, c - color"""
	for i in range(n_s):
		t.color(c)
		t.forward(size)
		t.left(360/n_s)
		

import turtle

wn = turtle.Screen()
wn.bgcolor("lightblue")
wn.title("Polygon testing")

tom = turtle.Turtle()
tom.pensize(1)
tom.speed(1)
tom.hideturtle()

"""
polygon_gen(tom, 3, 100, "red")
polygon_gen(tom, 4, 75, "blue")
polygon_gen(tom, 5, 50, "green")
"""
tom.penup()
tom.right(135)
tom.forward(75)
tom.left(135)
tom.pendown()

for i in range(3,21):
	polygon_gen(tom, i, 5+i*2, "red")

