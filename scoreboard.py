from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(x=0, y=300)
        self.turn = 3
        self.score = 0
        self.show_scoreboard()

    def show_scoreboard(self):
        self.clear()
        self.write(
            f'Turn: {self.turn}                Score: {self.score}',
            align='center',
            font=("Courier", 20, "normal")
        )

    def score_increase(self, color):
        if color == 'yellow':
            self.score += 1
        elif color == 'green':
            self.score += 3
        elif color == 'orange':
            self.score += 5
        elif color == 'red':
            self.score += 7
        self.show_scoreboard()

    def turn_decrease(self):
        self.turn -= 1
        self.show_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align='center', font=("Arial", 60, "bold"))

    def winner(self):
        self.game_over()
        self.goto(x=0, y=-100)
        self.write('You Win', align='center', font=("Arial", 50, "bold"))




