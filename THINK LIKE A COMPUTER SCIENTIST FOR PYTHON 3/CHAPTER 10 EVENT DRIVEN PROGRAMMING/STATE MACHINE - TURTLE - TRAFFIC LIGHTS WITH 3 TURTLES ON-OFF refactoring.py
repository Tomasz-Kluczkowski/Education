import turtle

"""
Simple program simulating traffic light changes. Notes:
My idea is to convert the color changing into bit reading so that color on/off is just a bit on/off (1/0)
and code 3 lights that way 1,0,0 then 1,1,0 then 0,1,0 then 0,0,1 as per exercise
There should be a function for coloring all 3 turtles based on 0,0,0 arguments
Make lists of colors and base color on index in the list ix = 0 which can be
parameter in the function means OFF color, ix = 1 , second item in
the list means ON color of the light.
"""

def draw_housing():
    """ Draw a nice housing to hold the trafic lights"""
    tess.pensize(3)
    tess.color("black", "darkgrey")
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40, 180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()


def shut_down():
    """just an Escape key handler"""
    wn.bye()


def turtle_colors(a,b,c, time):
    """This function colors all 3 turtles as requested by the advance_machine function.
    Parameter a,b,c is off/on (0/1) state for each turtle representing a traffic light.
    We change color by using arguments a,b,c as indexes in the color lists for each turtle.
    OFF color is first in the list then ON color.
    Time parameter causes the state_num variable to change to the next one on timer event"""
    tess_colors = ["dark green", "lime green"]
    alex_colors = ["peru", "orange"]
    tom_colors = ["firebrick", "red"]
    tess.fillcolor(tess_colors[a])
    alex.fillcolor(alex_colors[b])
    tom.fillcolor(tom_colors[c])
    wn.ontimer(advance_state_machine, time)


def advance_state_machine():
    """ this function switches between 4 possible states of the traffic light"""
    global state_num        # allows to use a global variable state_num, will not create a local one

    if state_num == 0:      # transition from state 0 to 1, green & orange on, red off
        turtle_colors(1, 1, 0, 1000)
        state_num = 1

    elif state_num == 1:    # transition from state 1 to 2, green off, orange on, red off
        turtle_colors(0, 1, 0, 1000)
        state_num = 2

    elif state_num == 2:    # transition from state 1 to 3, green off, orange off, red on
        turtle_colors(0, 0, 1, 2000)
        state_num = 3

    elif state_num == 3:    # transition from state 3 to 0, green on, orange off, red off
        turtle_colors(1, 0, 0, 3000)
        state_num = 0


turtle.setup(500,500) #window size
wn = turtle.Screen()
wn.title("Traffic lights!")
wn.bgcolor("lightgreen")

""" lets set up turtles and their positions next"""
tess = turtle.Turtle()
alex = turtle.Turtle()
tom = turtle.Turtle()

turtles = [tess,alex,tom]

draw_housing()
pos_offset = 0

for i in turtles:

    # position turtles onto the place in the traffic light housing but keep them hidden
    i.hideturtle()
    i.penup()
    i.forward(40)
    i.left(90)
    i.forward(50+pos_offset)
    i.shape("circle")
    i.shapesize(3)
    # move the following turtles in the list up on the housing
    pos_offset += 70

# this variable holds the current state of the machine
state_num = 0

for i in turtles:   # reveal all the turtles
    i.showturtle()

wn.onkey(shut_down, "Escape")
advance_state_machine()
wn.listen()
wn.mainloop()