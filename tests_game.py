import unittest
from unittest.mock import patch

import src.map
from src.game import Game
from src.map import Map
from src.options import *


class GameTetCase(unittest.TestCase):
    def test_make_game_object(self):
        game = Game()
        self.assertIsNotNone(game)
    
    def test_init_map(self):
        game = Game()
        self.assertIsNotNone(game.map)
        self.assertIsInstance(game.map, Map)

    @patch("src.map.Map")
    def test_map_generation(self, MockMap):
        game = Game()
        game.map = MockMap
        game.generate_map(20, 10, EMPTY)
        game.map.generate.assert_called_with(20, 10,  EMPTY)

    @patch("src.map.Map")
    def tests_place_items_on_map(self, MockMap):
        game = Game()
        game.map = MockMap
        game.generate_map(20, 10, EMPTY)
        game.place_on_map(20, TREE)
        game.map.place.assert_called_with(20, TREE)

    
if __name__ == "__main__":
    unittest.main()
