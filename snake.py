from turtle import Turtle

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for i in range(3):
            snake = Turtle(shape="square")
            snake.color("white")
            snake.penup()
            snake.goto(x=(0 - (i * 20)), y=0)
            self.segments.append(snake)


    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.segments[0].forward(20)

    def snake_up(self):
        self.segments[0].setheading(90)

    def snake_down(self):
        self.segments[0].setheading(270)

    def snake_left(self):
        self.segments[0].setheading(180)

    def snake_right(self):
        self.segments[0].setheading(0)