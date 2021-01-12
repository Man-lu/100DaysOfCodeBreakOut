from turtle import Turtle
from random import choice
from bricks_positions import positions

colors = ["red", "blue", "yellow", "green"]


class Brick:
    def __init__(self):
        self.bricks = []
        self.create_brick()

    def create_brick(self):
        for position in positions:
            brick = Turtle()
            brick.shape("square")
            brick.shapesize(1, 2)
            brick.color(choice(colors))
            brick.penup()
            brick.goto(position)
            self.bricks.append(brick)


    # def destroy_brick(self):
    #     brick.penup()
    #     self.goto(1000, 1000)
