import unittest
from unittest.mock import patch
from src.brain import *
from src.options import *


class BrainTetCase(unittest.TestCase):
    
    def test_make_brain_object(self):
        brain = Brain()
        self.assertIsNotNone(brain)
    
    def test_generate_object_by_char(self):
        brain = Brain()
        self.assertIsInstance(brain.recognize(EMPTY), Empty)
        self.assertIsInstance(brain.recognize(TREE), Tree)
        self.assertIsInstance(brain.recognize(STONE), Stone)
        self.assertIsInstance(brain.recognize(LETTER), Letter)
        self.assertIsInstance(brain.recognize(TREASURE), Treasure)
    
    def test_empty_object(self):
        empty = Empty()
        self.assertEqual(empty.mesage(), MESSAGE_EMPTY)
        self.assertEqual(empty.actions(), [DIRECTION_UP, DIRECTION_DOWN, DIRECTION_LEFT, DIRECTION_RIGHT])
    
    def test_tree_object(self):
        tree = Tree()
        self.assertEqual(tree.mesage(), MESSAGE_TREE)
        self.assertEqual(tree.actions(), [DIRECTION_UP, DIRECTION_DOWN, DIRECTION_LEFT, DIRECTION_RIGHT, HACK])
    
    def test_stone_object(self):
        stone = Stone()
        self.assertEqual(stone.mesage(), MESSAGE_STONE)
        self.assertEqual(stone.actions(), [DIRECTION_UP, DIRECTION_DOWN, DIRECTION_LEFT, DIRECTION_RIGHT])
    
    def test_letter_object(self):
        letter = Letter()
        self.assertEqual(letter.mesage(), MESSAGE_LETTER)
        self.assertEqual(letter.actions(), [DIRECTION_UP, DIRECTION_DOWN, DIRECTION_LEFT, DIRECTION_RIGHT, READ])
    
    def test_treasure_object(self):
        treasure = Treasure()
        self.assertEqual(treasure.mesage(), MESSAGE_TREASURE)
        self.assertEqual(treasure.actions(), [DIRECTION_UP, DIRECTION_DOWN, DIRECTION_LEFT, DIRECTION_RIGHT, PICK_UP])


if __name__ == "__main__":
    unittest.main()
