import unittest
from src.game import Game
from src.map import Map
from src.options import *
from random import choice, randint


class GameTetCase(unittest.TestCase):
    def test_make_game_object(self):
        game = Game()
        self.assertIsNotNone(game)
    
    def test_init_map(self):
        game = Game()
        game.generate_map(20, 10, EMPTY)
        self.assertIsNotNone(game.map)
        self.assertIsInstance(game.map, Map)
        # self.assertEqual()


if __name__ == "__main__":
    unittest.main()
