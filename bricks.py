from turtle import Turtle

COLORS = ['red', 'orange', 'green', 'yellow']
COLOR_INDEX = 0


class Bricks:

    def __init__(self):
        self.all_bricks = []
        self.red_row = False
        self.orange_row = False
        self.make_brick()

    def brick(self, color, position):
        brick = Turtle(shape='square')
        brick.color(color)
        brick.shapesize(stretch_len=4.5, stretch_wid=2)
        brick.penup()
        brick.goto(position)
        self.all_bricks.append(brick)

    def make_brick(self):
        global COLOR_INDEX
        for y_pos in range(150, -50, -50):
            for x_pos in range(-650, 700, 100):
                self.brick(COLORS[COLOR_INDEX], (x_pos, y_pos))

            COLOR_INDEX += 1
