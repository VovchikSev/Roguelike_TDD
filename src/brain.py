from src.options import *


class Brain:
    def recognize(self, char):
        
        if char == TREE:
            return Tree()
        if char == STONE:
            return Stone()
        if char == LETTER:
            return Letter()
        if char == TREASURE:
            return Treasure()
        return Empty()


class Empty:
    def mesage(self):
        return MESSAGE_EMPTY
    
    def actions(self):
        return [DIRECTION_UP, DIRECTION_DOWN, DIRECTION_LEFT, DIRECTION_RIGHT]


class Tree:
    def mesage(self):
        return MESSAGE_TREE
    
    def actions(self):
        return [DIRECTION_UP, DIRECTION_DOWN, DIRECTION_LEFT, DIRECTION_RIGHT, HACK]


class Stone:
    def mesage(self):
        return MESSAGE_STONE
    
    def actions(self):
        return [DIRECTION_UP, DIRECTION_DOWN, DIRECTION_LEFT, DIRECTION_RIGHT]


class Letter:
    def mesage(self):
        return MESSAGE_LETTER
    
    def actions(self):
        return [DIRECTION_UP, DIRECTION_DOWN, DIRECTION_LEFT, DIRECTION_RIGHT, READ]


class Treasure:
    def mesage(self):
        return MESSAGE_TREASURE
    
    def actions(self):
        return [DIRECTION_UP, DIRECTION_DOWN, DIRECTION_LEFT, DIRECTION_RIGHT, PICK_UP]
