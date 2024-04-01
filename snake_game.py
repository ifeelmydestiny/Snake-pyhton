from turtle import Turtle, Screen
from scoreboard import Scoreboard
screen = Screen()
move_distance = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
scoreboard = Scoreboard()


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]
        # self.snake_size = 3

    def create_snake(self):
        x = 0
        for i in range(3 + scoreboard.score):
            snake_b = Turtle(shape="square")
            snake_b.speed("fastest")
            snake_b.color("white")
            snake_b.penup()
            snake_b.goto(x, 0)
            x += 20
            self.snake.append(snake_b)

    def snake_move(self):
        for i in range(len(self.snake) - 1, 0, -1):
            self.snake[0].color("red")
            cor = self.snake[i - 1].position()
            self.snake[i].goto(cor[0], cor[1])
        self.snake[0].forward(move_distance)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
