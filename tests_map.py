import unittest
from random import choice, randint
from src.map import Map
from src.options import *


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
        self.assertEqual(EMPTY, map.get(randint(0, 20 - 1), randint(0, 10 - 1)))
        
        map.generate(20, 10, TREE)
        self.assertEqual(TREE, map.get(randint(0, 20 - 1), randint(0, 10 - 1)))
    
    def test_put_item_on_map(self):
        x, y = randint(0, 20 - 1), randint(0, 10 - 1)
        map = Map()
        map.generate(20, 10, EMPTY)
        self.assertEqual(EMPTY, map.get(x, y))
        map.put(x, y, TREE)
        self.assertEqual(TREE, map.get(x, y))
        
    def tests_place_items_on_map(self):
        map = Map()
        map.generate(20, 10, EMPTY)
        map.place(20, TREE)
        count = 0
        for y in range(10):
            count += map.map.count(TREE)
        self.assertEqual(count, 20)

        

        


if __name__ == "__main__":
    unittest.main()
