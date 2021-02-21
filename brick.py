from colorama import init, Fore, Back, Style

class Brick:
    def __init__ (self, id, width=1, height=1):
        super().__init__()

        self.width = 1
        self.height = 1

        self.x = 1
        self.y = 1

        self.strength = 3

    def display(self):
        y = self.y
        x = self.x
        symbol = self.strength

        return (symbol)
