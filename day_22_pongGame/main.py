from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle(350,0)
l_paddle = Paddle(-350,0)

ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(l_paddle.go_up, "w" )
screen.onkey(l_paddle.go_down, "s")

screen.onkey(r_paddle.go_up, "o" )
screen.onkey(r_paddle.go_down, "l")



game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.120)
    ball.move()

    #Detect collision with wall
    if ball.ycor() == 280 or ball.ycor() == -280:
        ball.bounce_y()

    #Detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() > -320:
        ball.bounce_x()
    
    #Detect when r_paddle misses
    
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.r_point()
        

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.l_point()


screen.exitonclick()