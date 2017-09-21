import turtle

turtle.setup(400,500) #window size
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")

tess = turtle.Turtle()


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


draw_housing()

tess.penup()
# position tess onto the place where the green light should be
tess.forward(40)
tess.left(90)
tess.forward(50)
# turn tess into a big green circle
tess.shape("circle")
tess.shapesize(3)
tess.fillcolor("green")

#traffic light is a state machine with three states,
# green, orange, red. We number these states 0, 1, 2
# When machine changes statem we change tess' position and her fillcolor

# this variable holds the current state of the machine
state_num = 0


def advance_state_machine():
    global state_num        # allows to use a global variable state_num, will not create a local one
    if state_num == 0:      # transition from state 0 to 1
        tess.forward(70)
        tess.fillcolor("orange")
        state_num = 1
    elif state_num == 1:    # transition from state 1 to 2
        tess.forward(70)
        tess.fillcolor("red")
        state_num = 2
    elif state_num == 2:    # transition from state 2 to 0
        tess.back(140)
        tess.fillcolor("green")
        state_num = 0
    wn.ontimer(advance_state_machine, 1000) # function call itself on a timer repeatedly

# bind the even handler to the space key.
# wn.onkey(advance_state_machine, "space")

advance_state_machine()
# wn.listen()
wn.mainloop()