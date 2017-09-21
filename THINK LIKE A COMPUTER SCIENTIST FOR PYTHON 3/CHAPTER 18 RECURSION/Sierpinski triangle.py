import turtle

wn = turtle.Screen()

def sierpinski_triangle(t, order, size):
    """ Generate Sierpinski equilateral triangle fractal using turtle 't' of 'order' and 'size' """
    if order == 0:
        for i in range(3):
            t.forward(size)
            t.left(120)
    else:
        sierpinski_triangle(t,order -1, size/2)
        t.forward(size/2)
        sierpinski_triangle(t,order -1, size/2)
        t.forward(size/2)
        t.left(120)
        t.forward(size/2)
        sierpinski_triangle(t, order -1, size/2)
        t.left(60)
        t.forward(size/2)
        t.left(60)
        t.forward(size/2)
        t.left(120)



tur1 = turtle.Turtle()
tur1.speed(0)

sierpinski_triangle(tur1, 3, 60)


wn.mainloop()











