from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.score = 0
        self.goto(0, 350)
        self.write(f"Scoreboard: {self.score}", align="center", font=("Arial", 24, "normal"))
        self.clear()

    def clear_(self):
        self.clear()
        self.score += 1
        self.goto(0, 350)
        self.write(f"Scoreboard = {self.score}", align="center", font=("courier", 24, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("courier", 24, "normal"))
