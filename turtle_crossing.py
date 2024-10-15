import turtle as t

class Go_Turtle(t.Turtle):

    def __init__(self):
        super(Go_Turtle, self).__init__()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.penup()
        self.return_to_start()

    def return_to_start(self):
        self.goto(0,-280)


    def move(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def at_finish(self):
        if self.ycor() > 290:
            self.return_to_start()
            return True
        else:
            return False


