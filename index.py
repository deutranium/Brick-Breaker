from objects import *
from getch import _getChUnix as getChar
import time
from alarmexception import *
import signal
import variables as V

from colorama import init, Fore, Back, Style

import brick


SCORE = 0
LIVES = 3
TIME_ELAPSED = 0
FPS = 30
t = 1/FPS
ROWS = V.ROWS
COLS = V.COLS
SPEED = 2
BLOCK = 0
GAME_ARR = [[BLOCK for x in range(COLS)] for y in range(ROWS)]

# for i in range(4):
#     GAME_ARR[4][i + 15] = 1
start_time = time.time()

pd = Paddle(20, 1)

# print stats like life etc.
def print_stats(time, lives, score):
    print(
        """Time: %d,\nLives: %d,\nScore: %d
        """ % (time, lives, score)
    )

GAME_ARR = brick.create_bricks(COLS, ROWS, 20, GAME_ARR)

# RENDER GAME_ARR
def setup():
    global TIME_ELAPSED
    TIME_ELAPSED = round(time.time() - start_time)
    print("\033[H\033[J", end="")
    print_stats(TIME_ELAPSED, LIVES, SCORE)
    print("_"*COLS)
    for i in GAME_ARR:
        for j in i:
            if j == 0:
                print(Back.WHITE + str(j) + Style.RESET_ALL, end="")
            else:
                print(j, end="")
        print()
    print(Style.RESET_ALL)


# set alam stuff for input char
def alarm_handler(signum, frame):
    raise AlarmException

# get input char
def input_char(timeout):
    signal.signal(signal.SIGALRM, alarm_handler)
    signal.setitimer(signal.ITIMER_REAL, timeout)
    try:
        txt = getChar()()
        signal.alarm(0)
        return txt
    except AlarmException:
        pass
    signal.signal(signal.SIGALRM, signal.SIG_IGN)
    return ''

# end game
def end_game():
    msg = """⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⡤⢶⣶⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣠⣤⣤⣤⣿⣧⣀⣀⣀⣀⣀⣀⣀⣀⣤⡄⠀
⢠⣾⡟⠋⠁⠀⠀⣸⠇⠈⣿⣿⡟⠉⠉⠉⠙⠻⣿⡀
⢺⣿⡀⠀⠀⢀⡴⠋⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠙⠇
⠈⠛⠿⠶⠚⠋⣀⣤⣤⣤⣿⣿⣇⣀⣀⣴⡆⠀⠀⠀
⠀⠀⠀⠀⠠⡞⠋⠀⠀⠀⣿⣿⡏⠉⠛⠻⣿⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡇⠀⠀⠀⠈⠁⠀⠀
⠀⠀⣠⣶⣶⣶⣶⡄⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
⠀⢰⣿⠟⠉⠙⢿⡟⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
⠀⢸⡟⠀⠀⠀⠘⠀⠀⠀⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀time played: %d
⠀⠈⢿⡄⠀⠀⠀⠀⠀⣼⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀lives: %d
⠀⠀⠀⠙⠷⠶⠶⠶⠿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀score: %d
    """
    print("\033[H\033[J", end="")
    print(msg % (TIME_ELAPSED, LIVES, SCORE))

for i in range(3):
    ball = Ball(pd)
    LIVES = 3 - i

    while True:
        txt = input_char(timeout = t/2)
        if(txt != None):
            time.sleep(t/2)
        if txt.lower() == "a":
            pd.v = -1
        elif txt.lower() == "d":
            pd.v = 1
        elif txt.lower() == "q":
            break
        elif ball.attached and txt.lower() == "p":
            ball.attached = False
        else:
            pd.v = 0

        if(ball.init_y + 1 >= V.ROWS):
            end_game()
            break
        else:
            if ball.check_death(pd):
                break
            else:
                ball.move(pd, GAME_ARR)
 
        print(type(GAME_ARR[-1]))
            
        GAME_ARR = ball.display(GAME_ARR)
        print(type(GAME_ARR[-1]))

        if (pd.x + pd.v*SPEED + pd.width + 1 > COLS) or (pd.x + pd.v*SPEED < 0):
            pd.v = 0

        pd.move()
        GAME_ARR[-1] = pd.display()
        
        setup()
        # print(ball.vx)
        # print(ball.vy)
        
        
        time.sleep(t)
        GAME_ARR[ball.init_y][ball.init_x] = 0

end_game()
