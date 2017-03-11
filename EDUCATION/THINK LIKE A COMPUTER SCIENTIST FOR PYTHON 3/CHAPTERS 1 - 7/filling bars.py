import turtle

def draw_bar(t,height):
	
	''' get turtle t to draw one bar of height'''
	t.begin_fill() #fill bar with color set as a second parameter of turtle
	t.left(90)
	t.forward(height)
	t.write(" "+ str(height)) # will write bar's value on top of it
	t.right(90)
	t.forward(40)
	t.right(90)
	t.forward(height)
	t.left(90)
	t.end_fill() #stop filling a bar
	t.penup()			# separate the bars from each other
	t.forward(10) # small gap for before the  next bar
	t.pendown()


wn = turtle.Screen()
wn.bgcolor("lightblue")
wn.title("display bar chart")

tom = turtle.Turtle()
tom.pensize(1)
tom.speed(1)
tom.color("blue", "red")  # will change pen color to blue and fill color to red for 										  		#this turtle 

data = [48, 117, 200, 240, 160, 260, 220] # data values for the bar chart


for a in data:
	draw_bar(tom,a)
	
# wn.mainloop() this is commented for iphone use only
