"""Modify the turtle bar chart program so that the bar for any value of 200
or more is filled with red, values between [100 and 200) are filled with yellow,
and bars representing values less than 100 are filled with green.

In the turtle bar chart program, what do you expect to happen if one or more
of the data values in the list is negative? Try it out. Change the program so
that when it prints the text value for the negative bars, it puts the text
below the bottom of the bar."""



import turtle

def draw_bar(t,height):

    """ use draw_br function to draw bars of data with turtle t of height and color dependant on the height"""
    if height >= 200:
        t.color("blue", "red")

    elif height >= 100 and height < 200:
        t.color("blue", "yellow")

    else:
        t.color("blue", "green")

    t.begin_fill()
    t.left(90)
    t.forward(height)

    if height >= 0:
        t.write(" "+ str(height)) # will write bar's value on top of it
        t.right(90)
        t.forward(40)
        t.right(90)
        t.forward(height)
        t.left(90)
        t.end_fill() #stop filling a bar

    else:

        t.penup()                 # could not force writing on the other side
        t.forward(-15)          # of the line so have to move turtle a bit down
        t.write(" "+ str(height)) # will write bar's value on below of it
        t.forward(15)
        t.pendown()
        t.right(90)
        t.forward(40)
        t.right(90)
        t.forward(height)
        t.left(90)
        t.end_fill() #stop filling a bar

    t.penup()			# separate the bars from each other
    t.forward(10)       # small gap for before the  next bar
    t.pendown()


wn = turtle.Screen()
wn.bgcolor("lightblue")
wn.title("display bar chart")

tom = turtle.Turtle()
tom.pensize(1)
tom.speed(1)

data = [-48, -117, 200, 240, 160, 260, 220] # data values for the bar chart


for a in data:
	draw_bar(tom,a)

wn.mainloop()  #this is commented for iphone use only
