import time
from turtle import Screen

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

screen = Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

l_paddle = Paddle((-380,0))
r_paddle = Paddle((380,0))

ball = Ball()

score = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.travel()

    #Collision with wall
    if ball.ycor() >= 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Collision with paddle
    if ball.xcor() > 350 and ball.distance(r_paddle) < 50 or ball.xcor() < -350 and ball.distance(l_paddle) < 50:
        ball.bounce_x()

    #Ball is missed
    if ball.xcor() > 370:
        print("r_paddle missed")
        ball.reset_position()
        score.l_point()


    if ball.xcor() < -370:
        print("l_paddle missed")
        ball.reset_position()
        score.r_point()

screen.exitonclick()




