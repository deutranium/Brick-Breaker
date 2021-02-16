from headers import *

start_time = time.time()
game_time = time.time()

t = 1/FPS

os.system('clear')

pd = Paddle(6, 1)

bk = Brick(1, 1)

ball = Ball()

blank_arr = []

for i in range(ROWS):
    blank_arr.append(' '*COLS + '\n')

while True:

    setup(start_time)

    display_arr = copy.deepcopy(blank_arr)

    display_arr = pd.display(" ", display_arr)
    display_arr = ''.join(display_arr)
    print(bk.display())
    print(ball.display())
    print(display_arr)

    txt = input_char(timeout = t)
    # txt = getChar()()

    if txt.lower() == "a":
        pd.v = -1
    elif txt.lower() == "d":
        pd.v = 1
    elif txt.lower() == "q":
        break

    if (pd.x + pd.v*SPEED + pd.width + 2 > COLS) or (pd.x + pd.v*SPEED < 0):
        pd.v = 0

    time.sleep(t)
    # ball.move()
    pd.move()


# print(ball)
# for i in range(5):
#     print(unbreakable_brick, end='')
#     print(brick)
