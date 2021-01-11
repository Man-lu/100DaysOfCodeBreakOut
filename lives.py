# from turtle import Turtle
#
# FONT = ("Courier", 18, "normal")
#
# class Lives(Turtle):
#     def __init__(self):
#         super().__init__()
#         self.lives = 3
#         self.color("white")
#         self.hideturtle()
#         self.penup()
#         self.goto(300, 220)
#         self.update_lives()
#
#     def update_lives(self):
#         self.write(f"Lives: {self.lives}", align="left", font=FONT)
#
#     def decrease_lives(self):
#         self.clear()
#         self.lives -= 1
#         self.write(f"Score: {self.lives}", align="left", font=FONT)