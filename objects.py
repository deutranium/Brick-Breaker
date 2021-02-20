paddle = "<========>"

ball = "⬤"

unbreakable_brick = "|_x_|"

brick = "|___|"

import variables as V
from random import randrange

import time

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
        self.vx = 4
        self.vy = 1

        self.angle = self.vx/self.vy

        self.x = self.init_x
        self.y = self.init_y
        self.next_x = self.init_x + self.vx
        self.next_y = self.init_y + self.vy

        self.im_x = self.x + (self.vx)/abs(self.vx)
        self.im_y = self.y + (self.vy)/abs(self.vy)

        self.attached = False


    def move(self, paddle):

        # current location

        # predicted location
        self.im_x = self.x + (self.vx)/abs(self.vx)
        self.im_y = self.y + (self.vy)/abs(self.vy)

        if(self.next_y == self.y):
            if((self.x + 1*(self.vx)/abs(self.vx) == V.COLS - 1) or (self.x + 1*(self.vx)/abs(self.vx) == 0)):
                self.vx *= -1
                self.init_x = round(self.x)
                self.init_y = round(self.y)

                self.next_x = self.init_x + self.vx
                self.next_y = self.init_y + self.vy

            self.x += 1*(self.vx)/abs(self.vx)



        elif((self.next_y == self.im_y) or (self.next_x - self.im_x)/(self.next_y - self.y) > self.angle):
            if((self.y + 1*(self.vy)/abs(self.vy) == 0) or ((self.y + 1*(self.vy)/abs(self.vy) == V.ROWS - 1) and (paddle.x - 1 <= self.init_x <= paddle.x + paddle.width + 1))):
                self.vy *= -1
                self.init_x = round(self.x)
                self.init_y = round(self.y)

                self.next_x = self.init_x + self.vx
                self.next_y = self.init_y + self.vy

            self.y += 1*(self.vy)/abs(self.vy)



        else:
            if((self.x + 1*(self.vx)/abs(self.vx) == V.COLS - 1) or (self.x + 1*(self.vx)/abs(self.vx) == 0)):
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

        # if(self.x >= V.COLS - 1) or (self.x <= 0):
        #     self.vx *= -1
        #     self.init_x = round(self.x) + self.vx
        #     self.init_y = round(self.y) + self.vy
        #     self.next_x = self.init_x + self.vx
        #     self.next_y = self.init_y + self.vy
        # if(self.y <= 0):
        #     self.vy *= -1
        #     self.init_x = round(self.x) + self.vx
        #     self.init_y = round(self.y) + self.vy
        #     self.next_y = self.init_y + self.vy
        #     self.next_x = self.init_x + self.vx
            

        


        # V.GAME_ARR[self.y][self.x] = self.display()




    def display(self):
        y = self.init_y
        x = self.init_x

        return ball


