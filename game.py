from turtle import Screen
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
import time


class Game():
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, SLEEP_TIME):
        # initialize screen
        self.screen = Screen()
        self.screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        # set background colour
        self.screen.bgcolor('black')
        self.screen.title("PONG 🏓🏓🏓")
        # switch off tracer to gain better control of animation - will only update when screen.update() method called
        self.screen.tracer(False)

        # create paddles
        player_1_paddle = Paddle(1)
        player_2_paddle = Paddle(2)
        self.paddles = [player_1_paddle, player_2_paddle]
        self.sleep_time = SLEEP_TIME

        # initialize scoreboard
        self.scoreboard = Scoreboard()

        # set up point
        self.live_point = False
        self.ball = Ball()
        self.start_heading = 0

        # set screen to receive inputs
        self.screen.listen()
        self.screen.onkeypress(key="w", fun=self.paddles[0].up)
        self.screen.onkeypress(key="s", fun=self.paddles[0].down)
        self.screen.onkeypress(key="Up", fun=self.paddles[1].up)
        self.screen.onkeypress(key="Down", fun=self.paddles[1].down)
        self.screen.onkeypress(key="space", fun=self.play_point)
        self.screen.exitonclick()

    def play_point(self):
        # if statement to reset if game already played
        if self.scoreboard.score == [-1, -1]:
            self.scoreboard.update(0)
            self.scoreboard.update(1)
        if not self.live_point:
            self.live_point = True
            # set ball starting state
            self.ball.setheading(self.start_heading)
            self.ball.goto(0, 0)
            # set paddle starting states
            for paddle in self.paddles:
                paddle.sety(0)
            while self.live_point:
                self.ball.forward(5)
                # property used to govern when bounce can happen
                self.ball.paddle_bounce_state += 1
                self.ball.wall_bounce_state += 1
                for i, paddle in enumerate(self.paddles):
                    # detect if ball is at paddle line
                    if self.ball.at_paddle_line(paddle):
                        y_dist = abs(self.ball.ycor() - paddle.ycor())
                        # detect if ball has hit paddle, in which case bounce off paddle
                        if y_dist <= 35:
                            self.ball.bounce_paddle(paddle)
                        # if ball not hit paddle, it's the end of the point
                        else:
                            winner_idx = abs(i - 1)
                            # update scoreboard and reset ball and paddle
                            self.scoreboard.update(winner_idx)
                            self.live_point = False
                            # ball will be directed at losing paddle at start of next turn
                            if winner_idx == 0:
                                self.start_heading = 0
                            else:
                                self.start_heading = 180
                            # first to 4 points wins
                            if self.scoreboard.score[winner_idx] == 4:
                                self.scoreboard.gameover()
                # detect for wall bounce
                if abs(self.ball.ycor()) >= self.screen.screensize()[1]-10:
                    self.ball.wall_bounce()
                # update screen
                self.screen.update()
                time.sleep(self.sleep_time)
