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
"""
_images/star.png
Hints:
Try this on a piece of paper, moving and turning your cellphone as if it was a turtle. Watch how many complete rotations your cellphone makes before you complete the star. Since each full rotation is 360 degrees, you can figure out the total number of degrees that your phone was rotated through. If you divide that by 5, because there are five points to the star, you’ll know how many degrees to turn the turtle at each point.
You can hide a turtle behind its invisibility cloak if you don’t want it shown. It will still draw its lines if its pen is down. The method is invoked as tess.hideturtle() . To make the turtle visible again, use tess.showturtle() .
"""

import turtle
wn = turtle.Screen()

star = turtle.Turtle()
star.speed(1)
star.hideturtle()

for i in range(5):
    star.forward(250)
    star.right(144)

wn.mainloop()
