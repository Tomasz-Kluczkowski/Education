import turtle

wn = turtle.Screen()

def koch(t, order, size):
    """ Make turtle t draw a Koch fractl of order and size.
    Leave the turtle facing the same direction.
    """

    if order == 0:  # the base is just a straight line

        t.forward(size)

    else:
        for angle in [60, -120, 60, 0]:
            koch(t, order-1, size/3)    #go 1/3 of the way
            t.left(angle)

def koch_snowflake(t, order, size):
    for i in range(3):
        koch(t, order, size)
        tur1.right(120)



tur1 = turtle.Turtle()
tur1.speed(0)

#koch(tur1, 1, 30)
koch_snowflake(tur1, 3, 60)


wn.mainloop()