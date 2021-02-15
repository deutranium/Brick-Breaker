paddle = "<========>"

ball = "⬤"

unbreakable_brick = "|_x_|"

brick = "|___|"

from variables import *
from random import randrange


class Paddle:
    def __init__ (self, width, height = 1):
        super().__init__()
        self.width = width
        self.height = height

        self.x = 1
        self.y = 6

        self.v = 1


    def move(self):
        self.x += self.v * SPEED

    def display(self, symbol, arr):
        y = self.y
        x = self.x

        h = self.height
        w = self.width

        for i in range(y, y+h):
            arr[i] = arr[i][:x] + "<" + "="*w + ">" + arr[i][x+w:]

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

        self.x = randrange(COLS)
        self.y = 1
    
        self.vx = 2
        self.vy = 1

    def move(self):
        self.x += self.vx
        self.y += self.vy

    def display(self):
        y = self.y
        x = self.x

        return ('\n'*y + ' '*x + ball)


