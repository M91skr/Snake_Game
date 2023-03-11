"""---------------------------------------- Snake Game ----------------------------------------
This project is a **Snake Game**.
In this competition, the user helps the hungry snake to reach its food by using the arrow keys on the keyboard.
More food equals more points.
"""

# ---------------------------------------- Add Required Library ----------------------------------------

import time
from turtle import Screen

from food import Food
from scoreboard import Scoreboard
from snake import Snake

# ---------------------------------------- Play Space Creation ----------------------------------------

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# ---------------------------------------- Adding Snake, Food and Scoreboard into the Game Space -----------------------

snake = Snake()
food = Food()
scoreboard = Scoreboard()

# ---------------------------------------- Define the Function of Arrow Keys ----------------------------------------

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# ---------------------------------------- Game Running ----------------------------------------

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # ---------------------------------------- Successful Ending Definition ----------------------------------------

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()

    # ---------------------------------------- Unsuccessful Ending Definition ----------------------------------------

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

    for seg in snake.segment:
        if seg == snake.head:
            pass
        elif snake.head.distance(seg) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
