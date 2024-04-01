import time
from turtle import Screen
from snake_game import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=1000, height=800)
screen.bgcolor("black")
screen.title("Snake game 🐍🐍🐍")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.snake_move()
    if snake.head.distance(food) < 20:
        snake.create_snake()
        scoreboard.clear_()
        food.refresh()

    if snake.head.xcor() > 480 or snake.head.xcor() < -480 or snake.head.ycor() > 380 or snake.head.ycor() < -380:
        scoreboard.game_over()
        game_on = False
        print(f"You loose. Final score is {scoreboard.score}")
    if scoreboard.score > 1:
        for snake_ in snake.snake:
            if snake_ == snake.head:
                pass
            elif snake.head.distance(snake_) < 10:
                scoreboard.game_over()
                game_on = False
                print(f"You loose. Final score is {scoreboard.score}")

screen.exitonclick()
