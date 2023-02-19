import unittest
from random import randint
from unittest.mock import patch
from src.brain import *
from src.options import *
from src.user import User


class BrainTetCase(unittest.TestCase):
    
    def setUp(self) -> None:
        self.position = [randint(0, MAP_WIDTH - 1), randint(0, MAP_HEIGHT - 1)]
    
    def test_make_brain_object(self):
        brain = Brain()
        self.assertIsNotNone(brain)
    
    def test_generate_object_by_char(self):
        brain = Brain()
        self.assertIsInstance(brain.recognize(EMPTY, self.position), Empty)
        self.assertIsInstance(brain.recognize(TREE, self.position), Tree)
        self.assertIsInstance(brain.recognize(STONE, self.position), Stone)
        self.assertIsInstance(brain.recognize(LETTER, self.position), Letter)
        self.assertIsInstance(brain.recognize(TREASURE, self.position), Treasure)


    @patch("src.map.Map")
    def test_brain_see(self, MockMap):
        x, y = randint(0, MAP_WIDTH), randint(0, MAP_HEIGHT)
        brain = Brain()
        attrs = {"get.return_value": TREE, "calculate_position.return_value": [x, y - 1]}
        MockMap.configure_mock(**attrs)
        self.assertEqual(brain.see(MockMap, [x, y], DIRECTION_UP), (TREE, [x, y - 1]))


if __name__ == "__main__":
    unittest.main()
