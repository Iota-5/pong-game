from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.goto(-100, 230)
        self.write(self.l_score, align="center", font=("courier", 40, "normal"))
        self.goto(100, 230)
        self.write(self.r_score, align="center", font=("courier", 40, "normal"))

    def add_point_l(self):
        self.l_score += 1
        self.display_score()

    def add_point_r(self):
        self.r_score += 1
        self.display_score()

    def display_score(self):
        self.clear()
        self.goto(-100, 230)
        self.write(self.l_score, align="center", font=("courier", 40, "normal"))
        self.goto(100, 230)
        self.write(self.r_score, align="center", font=("courier", 40, "normal"))
