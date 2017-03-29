import turtle

class TurtleGtx(turtle.Turtle):
    pass

    def __init__(self):
        import random
        rng = random.Random()
        self.dist_limit = rng.randrange(150,1000)
        # turtle.Turtle.__init__(self)
        super().__init__()
        self.dist_travelled = 0

    def forward(self, distance):
        if self.dist_travelled > self.dist_limit:
            raise ValueError("Maximum allowed distance {0} travelled. "
                             "You have a flat tyre :). Try to call to fix_tyre method".format(self.dist_limit))
        super().forward(distance)
        # turtle.Turtle.forward(self, distance)
        self.dist_travelled += abs(distance)
        self.write(self.dist_travelled)

    def jump(self, distance):
        self.penup()
        self.forward(distance)
        self.pendown()
        self.write(self.dist_travelled)

    def fix_tyre(self):
        self.dist_travelled = 0

tom = TurtleGtx()
tom.color("red")
cla = TurtleGtx()
cla.color("green")
wn = turtle.Screen()
# tom.penup()
# tom.forward(100)
# tom.pendown()
cla.forward(-100)
tom.jump(200)
cla.jump(-100)
tom.left(90)
tom.forward(100)
cla.right(90)
cla.jump(200)
tom.left(45)
tom.forward(-50)
cla.right(60)
cla.forward(100)
wn.mainloop()