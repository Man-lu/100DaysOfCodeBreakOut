from turtle import Turtle


class Brick:
    def __init__(self):
        self.all_bricks = []

    def create_brick(self, position):
        brick = Turtle()
        brick.shape("square")
        brick.shapesize(1, 2)
        brick.color("white")
        brick.penup()
        brick.goto(position)
        self.all_bricks.append(brick)




