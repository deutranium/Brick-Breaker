import random, time

import variables as V

powerup_types = [

]

class PowerUp:
    def __init__ (self, x, y):
        super().__init__()

        self.x = x
        self.y = y

        self.vy = 1

        V.POWERUPS.append(self)
        self.time = time.time()

    def refresh(self):
        if(round(time.time() - self.time) > 10):
            V.POWERUPS.remove(self)


class ExpandPaddle(PowerUp):
    def __init__(self, x, y):
        PowerUp.__init__(self, x, y)

        self.symbol = "E"

    def func(self, ball, paddle):
        paddle.width += 10


class ShrinkPaddle(PowerUp):
    def __init__(self, x, y):
        PowerUp.__init__(self, x, y)

        self.symbol = "S"

    def func(self, ball, paddle):
        paddle.width -= 5


class FastBall(PowerUp):
    def __init__(self, x, y):
        PowerUp.__init__(self, x, y)

        self.symbol = "F"

    def func(self, ball, paddle):
        ball.vx += 1

class PaddleGrab(PowerUp):
    def __init__(self, x, y):
        PowerUp.__init__(self, x, y)

        self.symbol = "P"

    def func(self, ball, paddle):
        ball.attached = True

def display_powerup(game_arr, ball, paddle):
    for i in V.POWERUPS:
        x = i.x
        y = i.y

        if (y == V.ROWS) and (paddle.x - 1 <= i.x <= paddle.x + paddle.width + 1):
            i.func(ball, paddle)

        if not (y >= V.ROWS):
            game_arr[y][x] = 0
        i.y += 1
        if not (y + 1 >= V.ROWS):
            game_arr[y + 1][x] = i.symbol
        i.refresh()

    return game_arr