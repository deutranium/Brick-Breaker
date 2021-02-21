# from colorama import init, Fore, Back, Style
import random, time

import variables as V
from powerup import *

class Brick:
    def __init__ (self, x, y, width=1, height=1):
        super().__init__()

        self.width = 1
        self.height = 1

        self.x = x
        self.y = y

        self.strength = 3



def create_bricks(cols, rows, num, game_arr):
    bricks = []
    for i in range(num):
        x = random.randrange(cols - 1)
        y = random.randrange(rows - 5)
        elem = Brick(x, y)

        if( not (i%10)):
            elem.strength = 1000

        bricks.append(elem)
        
        # print(x)
        # time.sleep(1)
    return bricks

def display_bricks(bricks, game_arr):
    for i in bricks:
        x = i.x
        y = i.y
        game_arr[y][x] = 1

    return game_arr

def collide_brick(y, x, BRICKS, GAME_ARR, ball, paddle):
    for i in BRICKS:
        if i.y == y and i.x == x:

            if i.strength != 1000:
                i.strength -=1
                V.SCORE += 10
                if i.strength == 0:
                    BRICKS.remove(i)
                    GAME_ARR[y][x] = 0

    random_int = random.randint(0, 20)

    rand_array = [ExpandPaddle, ShrinkPaddle, FastBall, PaddleGrab]

    if random_int > 10:
        rand2 = random.randint(0, 3)
        this_powerup = rand_array[rand2](x = x, y = y);
        V.POWERUPS.append(this_powerup)

    

    V.BRICKS = BRICKS
    return GAME_ARR
    
