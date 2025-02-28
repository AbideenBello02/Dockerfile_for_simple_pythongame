from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="left", font=("Courier", 24, "normal"))

    def increment_score(self):
        self.score += 1
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 24, "normal"))
