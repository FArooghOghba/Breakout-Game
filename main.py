from turtle import Screen
from paddle import Paddle
from ball import Ball
from bricks import Bricks
from scoreboard import Scoreboard
import time


HORIZONTAL_WALL_LIMIT = 670
VERTICAL_WALL_LIMIT = 330
HOR_PADDLE_LIMIT_CON = 100
VER_PADDLE_LIMIT_CON = 15


def game():

    # ------------------------------- Screen Setup ------------------------------- #
    screen = Screen()
    screen.setup(width=1400, height=700)
    screen.title('The Break Out Game')
    screen.bgcolor('black')
    screen.listen()
    screen.tracer(0)

    paddle = Paddle()
    ball = Ball()
    bricks = Bricks()
    scoreboard = Scoreboard()

    screen.onkey(fun=paddle.move_right, key='Right')
    screen.onkey(fun=paddle.move_left, key='Left')

    is_game_on = True
    while is_game_on:
        global HOR_PADDLE_LIMIT_CON

        screen.update()
        ball.move()
        time.sleep(ball.speed_up)

        # --------------------- Configure Horizontal Wall Limits --------------------- #
        if ball.xcor() > HORIZONTAL_WALL_LIMIT or ball.xcor() < -HORIZONTAL_WALL_LIMIT:
            ball.x_bounce()

        # --------------------- Configure Upper Wall Limit --------------------- #
        if ball.ycor() > VERTICAL_WALL_LIMIT:
            ball.y_bounce()

            # Half the paddle after hitting the top wall
            if paddle.upper_wall is False:
                paddle.half_size()
                HOR_PADDLE_LIMIT_CON = 50
                paddle.upper_wall = True

        # --------------------- Collision Ball With Paddle --------------------- #
        if paddle.xcor() - HOR_PADDLE_LIMIT_CON <= ball.xcor() <= paddle.xcor() + HOR_PADDLE_LIMIT_CON and paddle.ycor() - VER_PADDLE_LIMIT_CON <= ball.ycor() <= paddle.ycor() + VER_PADDLE_LIMIT_CON:
            ball.y_bounce()

        # --------------------- Configure Bottom Wall Limit --------------------- #
        if ball.ycor() < -VERTICAL_WALL_LIMIT:
            scoreboard.turn_decrease()
            ball.reset_position()
            paddle.reset_position()

            if scoreboard.turn == 0:
                scoreboard.game_over()
                is_game_on = False

        # --------------------- Collision Ball With Bricks --------------------- #
        for brick in bricks.all_bricks:
            if brick.xcor() - 46 <= ball.xcor() <= brick.xcor() + 46 and brick.ycor() - 21 <= ball.ycor() <= brick.ycor() + 21:
                ball.hit += 1
                brick.goto(x=0, y=400)
                bricks.all_bricks.remove(brick)
                ball.y_bounce()
                scoreboard.score_increase(brick.color()[0])

                # Increase the speed if the number of hit is divisible by 4
                if ball.hit != 0 and ball.hit % 4 == 0:
                    ball.increase_speed()

                # Increase the speed after hit red row
                if brick.color()[0] == 'red' and bricks.red_row is False:
                    ball.increase_speed()
                    bricks.red_row = True

                # Increase the speed after hit orange row
                if brick.color()[0] == 'orange' and bricks.orange_row is False:
                    ball.increase_speed()
                    bricks.orange_row = True

        if len(bricks.all_bricks) == 0:
            scoreboard.winner()
            is_game_on = False

    screen.exitonclick()


if __name__ == '__main__':
    game()
