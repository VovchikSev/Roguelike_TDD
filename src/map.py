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
    
    def generate(self, width, height, empty_char):
        self.map = [[empty_char for _ in range(width)] for _ in range(height)]
    
    def get(self, x, y):
        return self.map[y][x]
    
    def put(self, x, y, char):
        self.map[y][x] = char

    def place(self, quantity, char):
        pass
