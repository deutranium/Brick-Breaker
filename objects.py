
import variables as V
from random import randrange

import time

from brick import *

from headers import *

# from colorama import init, Fore, Back, Style

ball = (Back.WHITE + Fore.CYAN + "▣" + Style.RESET_ALL)

unbreakable_brick = "|_x_|"

brick1 = Back.GREEN + "1111" + Style.RESET_ALL
brick2 = Back.YELLOW + "2222" + Style.RESET_ALL
brick3 = Back.RED + "3333" + Style.RESET_ALL
brick_unbreakable = Back.BLUE + "0000" + Style.RESET_ALL


init()

class Paddle:
    def __init__ (self, width, height = 1):
        super().__init__()
        self.width = width
        self.height = height

        self.x = 0
        self.v = 0


    def move(self):
        self.x += self.v * V.SPEED

    def display(self):
        x = self.x

        w = self.width

        
        arr = [Back.WHITE + " "]*x + [Back.BLACK + Style.BRIGHT + "|"] + ["|"]*w + ["|"] + [ Back.WHITE + " " + Style.RESET_ALL]*(V.COLS - x - w - 2)

        return arr




class Ball:
    def __init__ (self, pd, vx = 1):
        super().__init__()
        self.width = 0
        self.height = 0

        self.paddle_location = randrange(pd.width)

        self.init_x = pd.x
        self.init_y = V.ROWS - 2
        self.vx = 1
        self.vy = 1

        self.angle = self.vx/self.vy

        self.x = self.init_x
        self.y = self.init_y
        self.next_x = self.init_x + self.vx
        self.next_y = self.init_y + self.vy

        self.im_x = self.x + (self.vx)/abs(self.vx)
        self.im_y = self.y + (self.vy)/abs(self.vy)

        self.attached = True

    def check_death(self, paddle):
        if (self.y + self.vy >= V.ROWS - 1) and not (paddle.x - 1 <= self.init_x <= paddle.x + paddle.width + 1):
            return 1


    def move(self, paddle, GAME_ARR, BRICKS):

        if(self.attached and (self.next_y == (V.ROWS - 1))and (paddle.x - 1 <= self.init_x <= paddle.x + paddle.width + 1)):
            self.init_x = paddle.x + self.paddle_location
            self.x = self.init_x
            self.im_x = self.x + (self.vx)/abs(self.vx)

        else:

        # predicted location
            self.im_x = self.x + (self.vx)/abs(self.vx)
            self.im_y = self.y + (self.vy)/abs(self.vy)

            check_brick_x = GAME_ARR[round(self.y)][round(self.x + 1*(self.vx)/abs(self.vx))]
            # print(check_brick_x)
            check_brick_y = GAME_ARR[round(self.y + 1*(self.vy)/abs(self.vy))][round(self.x)]
            # print(check_brick_y)

            if(self.next_y == self.y):
                if((self.x + 1*(self.vx)/abs(self.vx) == V.COLS - 1) or
                    (self.x + 1*(self.vx)/abs(self.vx) == 0) or
                    check_brick_x == 1 ):

                    if(check_brick_x == 1):
                        GAME_ARR = collide_brick(round(self.y),round(self.x + 1*(self.vx)/abs(self.vx)), BRICKS, GAME_ARR, ball = self, paddle = paddle)


                    self.vx *= -1
                    self.init_x = round(self.x)
                    self.init_y = round(self.y)

                    self.next_x = self.init_x + self.vx
                    self.next_y = self.init_y + self.vy

                self.x += 1*(self.vx)/abs(self.vx)



            elif((self.next_y == self.im_y) or (self.next_x - self.im_x)/(self.next_y - self.y) > self.angle):
                if((self.y + 1*(self.vy)/abs(self.vy) == 0) 
                or ((self.y + 1*(self.vy)/abs(self.vy) == V.ROWS - 1)) 
                and (paddle.x - 1 <= self.init_x <= paddle.x + paddle.width + 1)
                or check_brick_y == 1):

                    if (paddle.x - 1 <= self.init_x <= paddle.x + paddle.width + 1) and ((self.y + 1*(self.vy)/abs(self.vy) == V.ROWS - 1)):
                        self.vx = abs((self.x - paddle.x) - (paddle.width/2 - paddle.x)) + 1

                        if self.vx > 4:
                            self.vx = 4
                        if self.vx < -4:
                            self.vx = -4

                    if(check_brick_y == 1):
                        GAME_ARR = collide_brick(round(self.y + 1*(self.vy)/abs(self.vy)), round(self.x), BRICKS, GAME_ARR, ball = self, paddle = paddle)

                    self.vy *= -1
                    self.init_x = round(self.x)
                    self.init_y = round(self.y)

                    self.next_x = self.init_x + self.vx
                    self.next_y = self.init_y + self.vy

                self.y += 1*(self.vy)/abs(self.vy)



            else:
                if((self.x + 1*(self.vx)/abs(self.vx) == V.COLS - 1) or (self.x + 1*(self.vx)/abs(self.vx) == 0)
                or check_brick_x == 1):
                    if(check_brick_x == 1):
                        GAME_ARR = collide_brick(round(self.y),round(self.x + 1*(self.vx)/abs(self.vx)), BRICKS, GAME_ARR, ball = self, paddle = paddle)



                    self.vx *= -1
                    self.init_x = self.x
                    self.init_y = self.y

                    self.next_x = self.init_x + self.vx
                    self.next_y = self.init_y + self.vy
                self.x += 1*(self.vx)/abs(self.vx)

            if(self.next_x == self.x) and (self.next_y == self.y):

                self.angle = self.vx/self.vy
                self.init_x = round(self.x)
                self.init_y = round(self.y)

                self.next_x = self.init_x + self.vx
                self.next_y = self.init_y + self.vy
        
        return GAME_ARR

    def display(self, game_arr):
        y = self.init_y
        x = self.init_x

        game_arr[y][x] = ball

        return game_arr


