from turtle import Turtle
import random
coord = [10, -10]

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.dx = random.choice(coord)
        self.dy = random.choice(coord)


    def move(self):
        x = self.xcor() + self.dx
        y = self.ycor() + self.dy
        self.goto(x, y)

    def bounce(self):
        self.dy *= -1.05

    def bounce1(self):
        self.dx *= -1.05

    def reset_ball(self):
        self.goto(0, 0)
        self.dx = random.choice(coord)
        self.dy = random.choice(coord)
        self.move()
