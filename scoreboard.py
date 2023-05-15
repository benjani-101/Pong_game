from turtle import Turtle
from constants import SCREEN_HEIGHT, SCREEN_WIDTH


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.pencolor('white')
        self.penup()
        self.hideturtle()
        self.goto(0 - (SCREEN_WIDTH / 4), SCREEN_HEIGHT / 2 - 50)
        self.write("Player 1: 0", align='center', font=("Verdana", 16, "normal"))
        self.goto(SCREEN_WIDTH / 4, SCREEN_HEIGHT / 2 - 50)
        self.write("Player 2: 0", align='center', font=("Verdana", 16, "normal"))
        self.score = [-1, -1]

    def update(self, player_index):
        self.score[player_index] += 1
        self.clear()
        self.goto(0 - (SCREEN_WIDTH / 4), SCREEN_HEIGHT / 2 - 50)
        self.write(f"Player 1: {self.score[0]}", align='center', font=("Verdana", 16, "normal"))
        self.goto(SCREEN_WIDTH / 4, SCREEN_HEIGHT / 2 - 50)
        self.write(f"Player 2: {self.score[1]}", align='center', font=("Verdana", 16, "normal"))

    def gameover(self):
        self.goto(0, 0)
        winner = self.score.index(max(self.score)) + 1
        self.write(f"GAME OVER!\nPlayer {winner} wins!\nPress Space Bar to play again", align='center', font=("Verdana", 30, "normal"))
        self.score = [-1, -1]