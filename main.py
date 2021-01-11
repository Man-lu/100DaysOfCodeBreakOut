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
score = ScoreBoard((300,-250))
life = ScoreBoard((300,-220))
game_over = ScoreBoard((0,0))
life.update_lives()
score.update_score()

for position in positions:
    brick.create_brick(position)


screen.listen()
screen.onkey(paddle.move_right, "Right")
screen.onkey(paddle.move_left, "Left")


game_on = True

while game_on and life.lives > 0:
    time.sleep(0.1)
    screen.update()
    ball.move()
    for b in brick.all_bricks:
        if b.distance(ball) < 30:
            b.undo()
            ball.bounce_top()
            score.increase_score()



    if ball.xcor() > 470 or ball.xcor() < -470:
        ball.bounce_sides()
    if ball.ycor() > 280:
        ball.bounce_top()

    if ball.distance(paddle) < 50 and ball.ycor() < -250:
        ball.bounce_top()

    if len(brick.all_bricks) == 0:
        game_on = False

    if ball.ball_out_of_bounds():
        life.decrease_lives()
        paddle.goto(0, -280)

if life.lives == 0 or len(brick.all_bricks) == 0:
    game_over.game_over()









screen.exitonclick()