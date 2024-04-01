import random
from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.shapesize(0.5, 0.5)
        self.refresh()

    def refresh(self):
        x = random.randint(-480, 480)
        y = random.randint(-380, 380)
        self.goto(x, y)
