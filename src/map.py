from random import randint

from src.options import *


class Map:
    # delta_xy = {
    #     DIRECTION_UP: (0, -1),
    #     DIRECTION_DOWN: (0, 1),
    #     DIRECTION_LEFT: (-1, 0),
    #     DIRECTION_RIGHT: (1, 0),
    # }
    
    def __init__(self):
        self.map = []
        self.width = 0
        self.height = 0
        self.empty_char = ''
    
    def generate(self, width, height, empty_char):
        self.map = [[empty_char for _ in range(width)] for _ in range(height)]
        self.width = width
        self.height = height
        self.empty_char = empty_char
    
    def get(self, x, y):
        return self.map[y][x]
    
    def put(self, x, y, char):
        self.map[y][x] = char
    
    def place(self, quantity, char):
        for i in range(quantity):
            while True:
                x, y = randint(0, self.width - 1), randint(0, self.height - 1)
                if self.check(x, y, self.empty_char):
                    self.put(x, y, char)
                    break
    
    def place_normal_ver(self, quantity, char):
        # требует проверки количества пустых ячеек, оно должно быть меньше или равно quantity
        count = 0
        while count < quantity:
            column = randint(0, len(self.map[0]) - 1)
            rows = randint(0, len(self.map) - 1)
            if self.get(column, rows) == EMPTY:
                self.put(column, rows, char)
                count += 1

    def check(self, x, y, char):
        return self.map[y][x] == char

    def count(self, char):
        count = 0
        for y in range(self.height):
            for x in range(self.width):
                if self.map[y][x] == char:
                    count += 1
        return count
