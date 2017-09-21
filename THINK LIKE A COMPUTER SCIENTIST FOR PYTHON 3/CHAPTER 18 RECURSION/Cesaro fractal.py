import turtle

wn = turtle.Screen()

def cesaro(t, order, size):
    """ Make turtle t draw a Cesaro torn line fractal of order and size.
    Leave the turtle facing the same direction.
    """
    if order == 0:  # the base is just a straight line
        t.forward(size)

    else:
        for angle in [-85, 170, -85, 0]:
            cesaro(t, order-1, size/2)    #go 1/3 of the way
            t.left(angle)



tur1 = turtle.Turtle()
tur1.speed(0)

cesaro(tur1, 5, 80)


wn.mainloop()