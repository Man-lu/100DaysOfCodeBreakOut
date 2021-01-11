from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(1,7)
        self.color("white")
        self.penup()
        self.goto(0,-280)
        self.x_cor = 50


    def move_right(self):
        new_xcor = self.xcor() + self.x_cor
        if new_xcor < 500:
            self.goto(new_xcor,self.ycor())

    def move_left(self):
        new_xcor = self.xcor() - self.x_cor
        if new_xcor > - 500:
            self.goto(new_xcor,self.ycor())


