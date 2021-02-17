paddle = "<========>"

ball = "⬤"

unbreakable_brick = "|_x_|"

brick = "|___|"

import variables as V
from random import randrange

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

        
        arr = [" "]*x + ["<"] + ["="]*w + [">"]

        return arr

class Brick:
    def __init__ (self, width=1, height=1):
        super().__init__()

        self.width = 1
        self.height = 1

        self.x = 1
        self.y = 1

    def display(self):
        y = self.y
        x = self.x

        return ('\n'*y + ' '*x + brick)

class Ball:
    def __init__ (self):
        super().__init__()
        self.width = 0
        self.height = 0

        self.init_x = 5
        self.init_y = 5
        self.vx = 1
        self.vy = 1

        self.angle = self.vx/self.vy

        self.x = self.init_x
        self.y = self.init_y
        self.next_x = self.init_x + self.vx
        self.next_y = self.init_y + self.vy

        self.im_x = self.x + (self.vx)/abs(self.vx)
        self.im_y = self.y + (self.vy)/abs(self.vy)


    def move(self):

        # current location

        # predicted location
        self.im_x = self.x + (self.vx)/abs(self.vx)
        self.im_y = self.y + (self.vy)/abs(self.vy)

        if(self.next_y == self.y):
            self.x += 1*(self.vx)/abs(self.vx)
        elif((self.next_y == self.im_y) or (self.next_x - self.im_x)/(self.next_y - self.y)>(self.next_x - self.x)/(self.next_y - self.im_y)):
            self.y += 1*(self.vy)/abs(self.vy)
        else:
            self.x += 1*(self.vx)/abs(self.vx)

        if(self.next_x == self.x) and (self.next_y == self.y):
            self.angle = self.vx/self.vy
            self.init_x = round(self.x)
            self.init_y = round(self.y)

            self.next_x = self.init_x + self.vx
            self.next_y = self.init_y + self.vy
            

        


        # V.GAME_ARR[self.y][self.x] = "."
        # if(self.x + self.vx >= V.COLS - 1) or (self.x + self.vx <= 0):
        #     self.vx *= -1
        # if(self.y + self.vy <= 0):
        #     self.vy *= -1
        # else:
        # self.x = (self.vx + self.x)%V.COLS
        # self.y = (self.vy + self.y)%V.ROWS




    def display(self):
        y = self.init_y
        x = self.init_x

        return ball


