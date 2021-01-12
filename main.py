from turtle import Screen
from paddle import Paddle
from ball import Ball
from brick import Brick
from scores import ScoreBoard

from bricks_positions import positions
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(1000,600)
screen.title("Breakout")
screen.tracer(0)

paddle = Paddle()
ball = Ball()
brick = Brick()
score = ScoreBoard()
life = ScoreBoard()
game_over = ScoreBoard()
life.update_lives()
score.update_score()

screen.listen()
screen.onkey(paddle.move_right, "Right")
screen.onkey(paddle.move_left, "Left")


game_on = True
destroyedBricks = []
while game_on and life.lives > 0:
    screen.update()
    time.sleep(0.1)
    ball.move()

    #Detect side walls
    if ball.xcor() > 470 or ball.xcor() < -470:
        ball.bounce_sides()

    # Detect Top wall
    if ball.ycor() > 280:
        ball.bounce_top()

    # Detect Paddle
    if ball.distance(paddle) < 60 and ball.ycor() < -260:
        ball.bounce_top()

    # Detect Bottom Wall
    if ball.ball_out_of_bounds():
        life.decrease_lives()
        paddle.goto(0, -280)

    # Detect and Destroy Individual Bricks
    for hit_brick in brick.bricks:
        if ball.distance(hit_brick) < 30:
            ball.bounce_top()
            score.increase_score()
            hit_brick.penup()
            hit_brick.goto(600, 0)
            destroyedBricks.append(hit_brick)

    if len(destroyedBricks) == len(brick.bricks) or life.lives == 0:
        game_over.game_over()
        game_on = False











screen.exitonclick()