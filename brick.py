from colorama import init, Fore, Back, Style
import random, time

class Brick:
    def __init__ (self, x, y, width=1, height=1):
        super().__init__()

        self.width = 1
        self.height = 1

        self.x = x
        self.y = y

        self.strength = 3

    def display(self, game_arr):
        y = self.y
        x = self.x
        symbol = self.strength

        game_arr[y][x] = symbol

        return game_arr


def create_bricks(cols, rows, num, game_arr):
    bricks = []
    for i in range(num):
        x = random.randrange(cols)
        y = random.randrange(rows - 5)
        elem = Brick(x, y)
        bricks.append(elem)
        # print(x)
        # time.sleep(1)
    return display_bricks(bricks, game_arr)

def display_bricks(bricks, game_arr):
    for i in bricks:
        x = i.x
        y = i.y
        game_arr[y][x] = 9

    return game_arr
