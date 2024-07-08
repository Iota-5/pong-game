from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time

l_paddle = Paddle(-350)
r_paddle = Paddle(350)
ball = Ball()
Screen = Screen()
Screen.bgcolor("black")
Screen.setup(width=800, height=600)
Screen.title("Pong")
Screen.tracer(0)
Score = Score()

Screen.listen()
Screen.onkey(l_paddle.go_up, "w")
Screen.onkey(l_paddle.go_down, "s")
Screen.onkey(r_paddle.go_up, "Up")
Screen.onkey(r_paddle.go_down, "Down")

game_on = True
while game_on:
    time.sleep(0.08)
    Screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.xcor() > 340 and ball.distance(r_paddle) < 50:
        ball.bounce1()

    if ball.xcor() > -340 and ball.distance(l_paddle) < 50:
        ball.bounce1()

    if ball.xcor() > 350:
        ball.reset_ball()
        Score.add_point_l()

    if ball.xcor() < -350:
        ball.reset_ball()
        Score.add_point_r()

Screen.exitonclick()
