import turtle

wn = turtle.Screen()



def sierpinski_triangle(t, order, size, color_change_depth = -1):
    """ Generate Sierpinski equilateral triangle fractal using turtle 't' of 'order' and 'size' """
    color = "red"

    if order == 0:
        for i in range(3):
            t.forward(size)
            t.left(120)


    else:


        if color_change_depth == 0:
            t.color("red")
        sierpinski_triangle(t,order -1, size/2, color_change_depth-1)

        t.penup()
        t.forward(size/2)
        t.pendown()
        if color_change_depth == 0:
            t.color("blue")
        sierpinski_triangle(t,order -1, size/2, color_change_depth-1)
        t.penup()
        t.left(120)
        t.forward(size/2)
        t.right(120)
        t.pendown()
        if color_change_depth == 0:
            t.color("green")
        sierpinski_triangle(t, order -1, size/2, color_change_depth-1)
        t.penup()
        t.right(120)
        t.forward(size/2)
        t.left(120)
        t.pendown()


tur1 = turtle.Turtle()
tur1.speed(0)
tur1.color("red")

sierpinski_triangle(tur1, 4, 360, 2)


wn.mainloop()











