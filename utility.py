from variables import *
from getch import _getChUnix as getChar
import time
from alarmexception import *
import signal

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
    for i in GAME_ARR:
        for j in i:
            print(j, end="")
        print()




def alarm_handler(signum, frame):
    raise AlarmException

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
