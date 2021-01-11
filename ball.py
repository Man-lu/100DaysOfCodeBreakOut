from turtle import Turtle

import time


start_position = (0,-260)

speed = 10
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        # self.goto(start_position,-260)
        self.goto(start_position)
        self.x_cor = 10
        self.y_cor = 10


    def move(self):
        new_x_cor = self.xcor() + self.x_cor
        new_y_cor = self.ycor() + self.y_cor
        self.goto(new_x_cor,new_y_cor)

    def bounce_sides(self):
        self.x_cor *= -1

    def bounce_top(self):
        self.y_cor *= -1

    def ball_out_of_bounds(self):
        if self.ycor() < -300:
            time.sleep(0.6)
            self.goto(start_position)
            self.bounce_top()
            return True
        else:
            return False



