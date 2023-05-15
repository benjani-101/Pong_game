from turtle import Turtle
from constants import PLAYER_1_X, PLAYER_2_X, SCREEN_WIDTH, SCREEN_HEIGHT


# paddle class is sub-class of Turtle
class Paddle(Turtle):
    def __init__(self, player_number):
        super().__init__()
        # reshape as rectangle of size 60 * 10
        self.shape('square')
        self.color('white')
        self.penup()
        self.turtlesize(stretch_wid=0.5, stretch_len=3)
        self.left(90)
        # initialized as player 1 or 2
        self.player_number = player_number
        try:
            if self.player_number == 1:
                self.setx(PLAYER_1_X)
            elif self.player_number == 2:
                self.setx(PLAYER_2_X)
        except ValueError:
            print("Paddle player number can only be 1 or 2")

    def up(self):
        # moves paddle up unless it is at edge of screen
        limit = SCREEN_HEIGHT/2 - 25
        if self.ycor() < limit:
            self.forward(10)

    def down(self):
        # moves paddle down unless it is at edge of screen
        limit = 0 - (SCREEN_HEIGHT / 2) + 25
        if self.ycor() > limit:
            self.backward(10)





