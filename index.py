from objects import *
from getch import _getChUnix as getChar
import time
from alarmexception import *
import signal
import variables as V


SCORE = 0
LIVES = 3
TIME_ELAPSED = 0
FPS = 30
t = 1/FPS


ROWS = V.ROWS
COLS = V.COLS

SPEED = 2

GAME_ARR = [["." for x in range(COLS)] for y in range(ROWS+1)]

start_time = time.time()

pd = Paddle(20, 1)
ball = Ball()

# print stats like life etc.
def print_stats(time, lives, score):
    print(
        """Time: %d,\nLives: %d,\nScore: %d
        """ % (time, lives, score)
    )

# RENDER GAME_ARR
def setup():
    global TIME_ELAPSED
    TIME_ELAPSED = round(time.time() - start_time)
    print("\033[H\033[J", end="")
    print_stats(TIME_ELAPSED, LIVES, SCORE)
    print("_"*COLS)
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


def paddle_bounce():
    ball.vy *= -1
    # ball_x = ball.init_x
    
    ball.vx = round(abs(pd.x - pd.width/2)/15) * round((ball.vx)/abs(ball.vx))
    ball.init_x = ball.init_x + ball.vx
    ball.init_y = ball.init_y + ball.vy
    ball.next_x = ball.init_x + ball.vx
    ball.next_y = ball.init_y + ball.vy
    ball.move()

    print(ball.vy)
    print(ball.vx)
    time.sleep(1)

while True:
    txt = input_char(timeout = t)
    if(txt != None):
        time.sleep(t)
    if txt.lower() == "a":
        pd.v = -1
    elif txt.lower() == "d":
        pd.v = 1
    elif txt.lower() == "q":
        break
    else:
        pd.v = 0

    if(ball.init_y + ball.vy >= V.ROWS):
        if (pd.x - 1 <= ball.init_x <= pd.x + pd.width + 1):
            paddle_bounce()
            
        else:
            end_game()
            break
    else:
        ball.move()
        
    GAME_ARR[ball.init_y][ball.init_x] = ball.display()

    if (pd.x + pd.v*SPEED + pd.width + 1 > COLS) or (pd.x + pd.v*SPEED < 0):
        pd.v = 0

    pd.move()
    GAME_ARR[-1] = pd.display()
    
    setup()
    
    time.sleep(t)
    GAME_ARR[ball.init_y][ball.init_x] = "."

