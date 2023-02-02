import unittest
from unittest.mock import patch
from random import choice, randint
# import sys
# sys.path.append("../Roguelike_TDD")
# sys.path.append("..")
from Roguelike_TDD.src.map import Map
from Roguelike_TDD.src.options import *

# проблема с импортом https://tproger.ru/translations/guide-into-python-imports/
class MapTestCase(unittest.TestCase):
    def test_make_map(self):
        map = Map()
        self.assertIsNotNone(map)
    
    def test_init_map(self):
        map = Map()
        map.generate(20, 10, EMPTY)
        self.assertIsNotNone(map.map)
        self.assertIsInstance(map.map, list)
        self.assertEqual(10, len(map.map))
        self.assertEqual(20, len(choice(map.map)))
        self.assertEqual(EMPTY, map.get(randint(0, 20), randint(0, 10)))
        
        map.generate(20, 10, TREE)
        self.assertEqual(TREE, map.get(randint(0, 20), randint(0, 10)))
    
    def test_put_item_on_map(self):
        x, y = randint(0, 20 - 1), randint(0, 10 - 1)
        map = Map()
        map.generate(20, 10, EMPTY)
        map.put(x, y, TREE)
        self.assertEqual(TREE, map.get(x, y))


if __name__ == "__main__":
    unittest.main()
