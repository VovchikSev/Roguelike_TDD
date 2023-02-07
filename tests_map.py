import unittest
from random import choice, randint
from src.map import Map
from src.options import *


class MapTestCase(unittest.TestCase):
    def test_make_map(self):
        map = Map()
        self.assertIsNotNone(map)
        self.assertIsNotNone(map.map)
        self.assertIsInstance(map.map, list)
        self.assertEqual(map.width, 0)
        self.assertEqual(map.height, 0)
        self.assertEqual(map.empty_char, '')
    
    def test_init_map(self):
        width = 20
        height = 10
        empty_char = EMPTY
        map = Map()
        map.generate(width, height, empty_char)
        self.assertEqual(10, len(map.map))
        self.assertEqual(20, len(choice(map.map)))
        self.assertEqual(EMPTY, map.get(randint(0, width - 1), randint(0, height - 1)))
        self.assertEqual(map.width, width)
        self.assertEqual(map.height, height)
        self.assertEqual(map.empty_char, empty_char)
        
        map.generate(20, 10, TREE)
        self.assertEqual(TREE, map.get(randint(0, 20 - 1), randint(0, 10 - 1)))
    
    def test_put_item_on_map(self):
        x, y = randint(0, 20 - 1), randint(0, 10 - 1)
        map = Map()
        map.generate(20, 10, EMPTY)
        self.assertEqual(EMPTY, map.get(x, y))
        map.put(x, y, TREE)
        self.assertEqual(TREE, map.get(x, y))
    
    def test_check_position_contain_char(self):
        map = Map()
        map.generate(20, 10, TREE)
        map.put(10, 5, EMPTY)
        self.assertTrue(map.check(10, 5, EMPTY))
        self.assertFalse(map.check(10, 6, EMPTY))
        self.assertTrue(map.check(10, 6, TREE))

    def tests_calculate_items_on_map(self):
        map = Map()
        map.generate(20, 10, EMPTY)
        count = 0
        for x, y in [[0, 0], [3, 4], [5, 6]]:
            map.put(x, y, TREE)
            count += 1
        self.assertEqual(map.count(TREE), count)
        self.assertEqual(map.count(EMPTY), 20 * 10 - count)

    def tests_place_items_on_map(self):
        map = Map()
        map.generate(20, 10, EMPTY)
        map.place(20, TREE)

        self.assertEqual(map.count(TREE), 20)


if __name__ == "__main__":
    unittest.main()
