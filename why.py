from headers import *
import variables as V

start_time = time.time()
game_time = time.time()

t = 1/FPS

os.system('clear')

pd = Paddle(6, 1)
bk = Brick(1, 1)
ball = Ball()

while True:


    ball.move()
    V.GAME_ARR[-2] = pd.display()

    # V.GAME_ARR[]
    print(bk.display())
    V.GAME_ARR[ball.y][ball.x] = ball.display()

    temp_x = ball.x
    temp_y = ball.y

    setup(start_time)
    txt = input_char(timeout = t)
    # txt = getChar()()

    if txt.lower() == "a":
        pd.v = -1
    elif txt.lower() == "d":
        pd.v = 1
    elif txt.lower() == "q":
        break
    else:
        pd.v = 0

    if (pd.x + pd.v*SPEED + pd.width + 2 > COLS) or (pd.x + pd.v*SPEED < 0):
        pd.v = 0

    time.sleep(t)
    
    V.GAME_ARR[temp_y][temp_x] = "."
    pd.move()
