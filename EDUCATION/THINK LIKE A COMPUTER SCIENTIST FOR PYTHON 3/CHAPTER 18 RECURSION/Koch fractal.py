import turtle

wn = turtle.Screen()

def koch(t, order, size):
    """ Make turtle t draw a Koch fractl of order and size.
    Leave the turtle facing the same direction.
    """
    angle_mod = 0
    if order == 0:  # the base is just a straight line
        t.left(0)
        t.forward(size)

    else:
        for angle in [60, -120, 60, 0]:
            koch(t, order-1, size)    #go 1/3 of the way
            t.left(angle + 60 * (order-1))



tur1 = turtle.Turtle()
tur1.speed(0)

koch(tur1, 3, 10)


wn.mainloop()