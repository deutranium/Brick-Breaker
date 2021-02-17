paddle = "<========>"

ball = "⬤"

unbreakable_brick = "|_x_|"

brick = "|___|"

import variables as V
from random import randrange


class Paddle:
    def __init__ (self, width, height = 1):
        super().__init__()
        self.width = width
        self.height = height

        self.x = 0
        self.v = 0


    def move(self):
        self.x += self.v * V.SPEED

    def display(self):
        x = self.x

        w = self.width

        
        arr = [" "]*x + ["<"] + ["="]*w + [">"]

        return arr

class Brick:
    def __init__ (self, width=1, height=1):
        super().__init__()

        self.width = 1
        self.height = 1

        self.x = 1
        self.y = 1

    def display(self):
        y = self.y
        x = self.x

        return ('\n'*y + ' '*x + brick)

class Ball:
    def __init__ (self):
        super().__init__()
        self.width = 0
        self.height = 0

        self.x = 5
        self.y = 5
        self.vx = 2
        self.vy = 1        

    def move(self):
        # V.GAME_ARR[self.y][self.x] = "."
        self.x = (self.vx + self.x)%V.COLS
        self.y = (self.vy + self.y)%V.ROWS

    def display(self):
        y = self.y
        x = self.x

        return ball


