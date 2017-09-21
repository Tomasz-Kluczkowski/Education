import turtle

# idea is to convert the color changing into bit reading so that color on/off is just a bit on/off (1/0)
# and code 3 lights that way 1,0,0 then 1,1,0 then 0,1,0 thn 0,0,1

turtle.setup(400,500) #window size
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")

tess = turtle.Turtle()  # green light
alex = turtle.Turtle()  # orange light
tom = turtle.Turtle()   # red light


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
    wn.bye()


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

alex.penup()
# position alex onto the place where the green light should be
alex.forward(40)
alex.left(90)
alex.forward(120)
# turn alex into a big green circle
alex.shape("circle")
alex.shapesize(3)
alex.fillcolor("orange")

tom.penup()
# position tom onto the place where the green light should be
tom.forward(40)
tom.left(90)
tom.forward(190)
# turn tom into a big green circle
tom.shape("circle")
tom.shapesize(3)
tom.fillcolor("red")

#traffic light is a state machine with three states,
# green, orange, red. We number these states 0, 1, 2
# When machine changes statem we change tess' position and her fillcolor

# this variable holds the current state of the machine
state_num = 0


def advance_state_machine():
    global state_num        # allows to use a global variable state_num, will not create a local one
    if state_num == 0:      # transition from state 0 to 1
        tess.fillcolor("lime green")
        alex.fillcolor("orange")
        tom.fillcolor("firebrick")
        state_num = 1
        wn.ontimer(advance_state_machine, 1000)

    elif state_num == 1:    # transition from state 1 to 2
        tess.fillcolor("dark green")
        alex.fillcolor("orange")
        tom.fillcolor("firebrick")
        state_num = 2
        wn.ontimer(advance_state_machine, 1000)

    elif state_num == 2:    # transition from state 1 to 2
        tess.fillcolor("dark green")
        alex.fillcolor("peru")
        tom.fillcolor("red")
        state_num = 3
        wn.ontimer(advance_state_machine, 2000)

    elif state_num == 3:    # transition from state 2 to 0
        tess.fillcolor("lime green")
        alex.fillcolor("peru")
        tom.fillcolor("firebrick")
        state_num = 0
        wn.ontimer(advance_state_machine, 3000)

#    wn.ontimer(advance_state_machine, 2000) # function call itself on a timer repeatedly

# bind the even handler to the space key.
# wn.onkey(advance_state_machine, "space")
wn.onkey(shut_down, "Escape")

advance_state_machine()
wn.listen()
wn.mainloop()