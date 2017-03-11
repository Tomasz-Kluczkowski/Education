""" This function allows creation of turtle generated polygons
Write a void function draw_equitriangle(t, sz) which calls draw_poly
from the previous question to have its turtle draw a equilateral triangle."""




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


def draw_equitriangle(t,sz):
    """using previously defined function polygon_gen call and draw an equitriangle
       t - turtle, sz - side size, we call previously defined function polygon_gen
       and substitute n_3 with 3, sz with called side size and set manually color to blue"""
    polygon_gen(t, 3, sz, "green")


draw_equitriangle(tom, 100)

wn.mainloop()