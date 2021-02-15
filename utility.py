from variables import *
from getch import _getChUnix as getChar
import time

def print_stats(time, lives, score):
    print(
        """Time: %d,\nLives: %d,\nScore: %d
        """ % (time, lives, score)
    )


def setup(start_time):
    cur_time = round(time.time() - start_time)
    print("\033[H\033[J", end="")
    print_stats(cur_time, LIVES, SCORE)
    print("_"*COLS)

def input_char():
    try:
        txt = getChar()()
        return txt
    except:
        return ""
