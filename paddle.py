from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_len=10, stretch_wid=0.5)
        self.color('blue')
        self.penup()
        self.setpos(x=0, y=-300)
        self.upper_wall = False

    def move_right(self):
        self.forward(30)

    def move_left(self):
        self.backward(30)

    def reset_position(self):
        self.goto(x=0, y=-300)

    def half_size(self):
        self.shapesize(stretch_len=5)

