import unittest
from random import randint
from unittest.mock import patch
from src.knowledge import *


class KnowledgeTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.position = [randint(0, MAP_WIDTH - 1), randint(0, MAP_HEIGHT - 1)]
    
    def test_empty_object(self):
        object_empty = Empty(self.position)
        self.assertIsInstance(object_empty, KnowledgeAbout)
        self.assertEqual(object_empty.position, self.position)
        self.assertEqual(object_empty.message(), MESSAGE_EMPTY)
        self.assertEqual(object_empty.can_do(), [])
        self.assertFalse(object_empty.it_barier())
    
    def test_tree_object(self):
        object_tree = Tree(self.position)
        self.assertIsInstance(object_tree, KnowledgeAbout)
        self.assertEqual(object_tree.position, self.position)
        self.assertEqual(object_tree.message(), MESSAGE_TREE)
        self.assertEqual(object_tree.can_do(), [HACK])
        self.assertTrue(object_tree.it_barier())
    
    def test_stone_object(self):
        object_stne = Stone(self.position)
        self.assertIsInstance(object_stne, KnowledgeAbout)
        self.assertEqual(object_stne.position, self.position)
        self.assertIsInstance(object_stne, KnowledgeAbout)
        self.assertEqual(object_stne.message(), MESSAGE_STONE)
        self.assertEqual(object_stne.can_do(), [])
        self.assertTrue(object_stne.it_barier())
    
    def test_letter_object(self):
        object_letter = Letter(self.position)
        self.assertIsInstance(object_letter, KnowledgeAbout)
        self.assertEqual(object_letter.position, self.position)
        self.assertEqual(object_letter.message(), MESSAGE_LETTER)
        self.assertEqual(object_letter.can_do(), [READ])
        self.assertTrue(object_letter.it_barier())
    
    def test_treasure_object(self):
        object_treasure = Treasure(self.position)
        self.assertIsInstance(object_treasure, KnowledgeAbout)
        self.assertEqual(object_treasure.position, self.position)
        self.assertEqual(object_treasure.message(), MESSAGE_TREASURE)
        self.assertEqual(object_treasure.can_do(), [PICK_UP])
        self.assertTrue(object_treasure.it_barier())


if __name__ == "__main__":
    unittest.main()
