from net import Net
from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard
display=Screen()
display.setup(width=800,height=600)
display.bgcolor("black")
display.title("Pong")
display.tracer(0)

net=Net()
ball=Ball()
score=ScoreBoard()
r_paddle=Paddle(370,0)
l_paddle=Paddle(-380,0) 
game_is_on=True

display.listen()
display.onkeypress(r_paddle.go_up, "Up")
display.onkeypress(r_paddle.go_down, "Down")
display.onkeypress(l_paddle.go_up, "w")
display.onkeypress(l_paddle.go_down, "s")
while game_is_on:
    display.update()
    time.sleep(ball.move_speed)
    ball.move()
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
    if ball.distance(r_paddle) <50 and ball.xcor()>350 or ball.distance(l_paddle) <50 and ball.xcor()<-360:
        ball.bounce_x()
    if ball.xcor()>390:
        ball.reset_position()
        score.r_point()
    if ball.xcor()<-390:
        ball.reset_position()
        score.l_point()
    
    
    
    












display.exitonclick()