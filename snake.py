from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]

    def create_snake(self):
        for i in range(3):
            self.add_turtle((i*-20, 0))

    def add_turtle(self, position):
        new_turtle = Turtle("square")
        new_turtle.penup()
        new_turtle.speed("fastest")
        new_turtle.color("white")
        new_turtle.goto(position)
        self.turtles.append(new_turtle)

    def reset(self):
        for i in self.turtles:
            i.goto(1000, 1000)
        self.turtles.clear()
        self.create_snake()
        self.head = self.turtles[0]

    def extend_snake(self):
        self.add_turtle((self.turtles[-1].xcor(), self.turtles[-1].ycor()))

    def move(self):
        for i in range(len(self.turtles) - 1, 0, -1):
            new_x = self.turtles[i - 1].xcor()
            new_y = self.turtles[i - 1].ycor()
            self.turtles[i].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

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
