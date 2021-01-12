from turtle import Turtle

FONT = ("Courier", 18, "normal")
GO_FONT = ("Courier", 30, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.lives = 3
        self.color("white")
        self.hideturtle()
        self.penup()

    def update_score(self):
        self.goto(300,-250)
        self.write(f"Score: {self.score}", align="left", font=FONT)

    def update_lives(self):
        self.goto(300,-220)
        self.write(f"Lives: {self.lives}", align="left", font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.goto(300,-250)
        self.write(f"Score: {self.score}", align="left", font=FONT)

    def decrease_lives(self):
        self.clear()
        self.lives -= 1
        self.goto(300,-220)
        self.write(f"Lives: {self.lives}", align="left", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=GO_FONT)
