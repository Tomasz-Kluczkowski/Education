import turtle

wn = turtle.Screen()

def cesaro(t, order, size, user_angle):
    """ Make turtle t draw a Cesaro torn line fractal of order and size.
    Leave the turtle facing the same direction.
    """
    tear_angle = -90 + user_angle
    if order == 0:  # the base is just a straight line
        t.forward(size)

    else:
        for angle in [tear_angle, -2 * tear_angle, tear_angle, 0]:
            cesaro(t, order-1, size/2, user_angle)    #go 1/3 of the way
            t.left(angle)

def cesaro_square(t, order, size, user_angle):
    """ Generates a Cesaro square fractal of 'order' and 'size' using turtle 't'. """
    for i in range(4):
        cesaro(t, order, size/2, user_angle)
        t.left(-90)


tur1 = turtle.Turtle()
tur1.speed(0)

#cesaro(tur1, 5, 80)
cesaro_square(tur1, 3, 400, 5)


wn.mainloop()