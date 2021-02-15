import colorama, sys, os, math, time, copy
from colorama import Fore, Back, Style

rows = 20
cols = 20
fps = 10
t = 1/fps

class Paddle:
	"""docstring for Paddle"""
	def __init__(self, width, height=1):
		super().__init__()
		self.width = width
		self.height = height
		self.x = 1
		self.y = 6
		self.v = 1
		#self.a = 1

	def move(self):
		self.x += self.v

	def display(self, color, symbol, arr):
		y = self.y
		h = self.height
		w = self.width
		x = self.x
		for i in range(y, y+h):
			arr[i] = arr[i][:x] + color + "<" + "x"*w + ">" + Fore.RESET + Back.RESET + arr[i][x+w:]
		return arr


blank_arr = []

for i in range(rows):
	blank_arr.append(' '*cols + '\n')

newPaddle = Paddle(6, 1)

while True:
	display_arr = copy.deepcopy(blank_arr)
	print("\033[H\033[J", end="")

	display_arr = newPaddle.display(Back.RED, ' ', display_arr)
	display_arr = ''.join(display_arr)
	print(display_arr)
	time.sleep(t)
	newPaddle.move()



