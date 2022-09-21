import time
from snake import Snake
from food import Food
from turtle import Screen
from scoreboard import ScoreBoard

s = Screen()
s.setup(600, 600)
s.bgcolor("black")
s.tracer(0)
s.update()

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

s.listen()
s.onkey(snake.up, "Up")
s.onkey(snake.down, "Down")
s.onkey(snake.left, "Left")
s.onkey(snake.right, "Right")

is_running = True
while is_running:
    s.update()
    time.sleep(0.1)
    snake.move()
    scoreboard.update_score()

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend_snake()

    if snake.head.xcor() > 295 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -295:
        scoreboard.reset()
        snake.reset()

    for i in snake.turtles[2:]:
        if snake.head.distance(i) < 10:
            scoreboard.reset()
            snake.reset()

s.exitonclick()
