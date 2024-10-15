import turtle as t
ALIGNMENT = "center"
FONT = ("Arial", 13, "bold")
class Score(t.Turtle):

    def __init__(self):
        self.level = 1
        super(Score, self).__init__()
        self.create_level()


    def create_level(self):
        self.clear()
        self.penup()
        self.hideturtle()
        self.goto(-260,260)
        self.write(f"Level {self.level}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, move=False, font=("arial", 20, "bold"))

    def update(self):
        self.level += 1
        self.create_level()

