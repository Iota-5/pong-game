from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.penup()
        self.goto(x, 0)

    def go_up(self):
        y_cor = self.ycor()
        self.goto(self.xcor(), y_cor + 20)

    def go_down(self):
        y_cor = self.ycor()
        self.goto(self.xcor(), y_cor - 20)
