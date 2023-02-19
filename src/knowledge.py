from abc import ABC,   abstractclassmethod

from src.options import *


class KnowledgeAbout(ABC):
    def __init__(self, position):
        self.position = position
    
    @abstractclassmethod
    def message(self):
        pass
    
    @abstractclassmethod
    def can_do(self):
        return [DIRECTION_UP, DIRECTION_DOWN, DIRECTION_LEFT, DIRECTION_RIGHT]
    
    @abstractclassmethod
    def do(self, user, action, map):
        pass
    
    # @abstractclassmethod
    def it_barier(self):
        return True


class Empty(KnowledgeAbout):
    def do(self, user, action, map):
        pass
    
    def message(self):
        return MESSAGE_EMPTY
    
    def can_do(self):
        return []
    
    def it_barier(self):
        return False


class Tree(KnowledgeAbout):
    def do(self, user, action, map):
        pass
    
    def message(self):
        return MESSAGE_TREE
    
    def can_do(self):
        return [HACK]


class Stone(KnowledgeAbout):
    def do(self, user, action, map):
        pass
    
    def message(self):
        return MESSAGE_STONE
    
    def can_do(self):
        return []


class Letter(KnowledgeAbout):
    def do(self, user, action, map):
        pass
    
    def message(self):
        return MESSAGE_LETTER
    
    def can_do(self):
        return [READ]


class Treasure(KnowledgeAbout):
    def do(self, user, action, map):
        pass
    
    def message(self):
        return MESSAGE_TREASURE
    
    def can_do(self):
        return [PICK_UP]
