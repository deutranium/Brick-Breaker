from objects import *
from getch import _getChUnix as getChar
import time
from alarmexception import *
import signal


SCORE = 0
LIVES = 3
TIME_ELAPSED = 0
FPS = 40
t = 1/FPS


ROWS = 20
COLS = 100

SPEED = 2

GAME_ARR = [["." for x in range(COLS)] for y in range(ROWS+1)]


pd = Paddle(6, 1)
ball = Ball()

# RENDER GAME_ARR
def setup():
    for i in GAME_ARR:
        for j in i:
            print(j, end="")
        print()


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



while True:
    print("\033[H\033[J", end="")

    txt = input_char(timeout = t)
    if txt.lower() == "a":
        pd.v = -1
    elif txt.lower() == "d":
        pd.v = 1
    elif txt.lower() == "q":
        break
    else:
        pd.v = 0

    ball.move()
    GAME_ARR[ball.y][ball.x] = ball.display()

    if (pd.x + pd.v*SPEED + pd.width + 2 > COLS) or (pd.x + pd.v*SPEED < 0):
        pd.v = 0

    pd.move()
    GAME_ARR[-1] = pd.display()
    
    setup()
    time.sleep(t)
    GAME_ARR[ball.y][ball.x] = "."
