import unittest
from random import randint, choice
from unittest.mock import patch

from src.brain import *
from src.options import *
from src.user import *
from src.map import *


class UserTestCase(unittest.TestCase):

    def tests_make_user_object(self):
        name = "UserName"
        user = User(name)
        self.assertIsNotNone(user)
        self.assertEqual(user.name, name)
        self.assertEqual(user.action, '')

    def test_user_has_inventory(self):
        user = User("UserName")
        self.assertIsInstance(user.inventory, list)
        self.assertEqual(len(user.inventory), 0)

    def test_user_has_health(self):
        user = User("UserName")
        self.assertEqual(user.health, MAX_USER_HEALTH)

    def test_user_has_brain(self):
        user = User("TestUser_Name")
        self.assertIsInstance(user.brain, Brain)

    def test_get_user_default_position(self):
        user = User("TestUser_Name")
        position = user.get_position()
        self.assertIsInstance(position, list)
        self.assertEqual(len(position), 2)
        self.assertEqual(position, [-1, -1])
        self.assertEqual(user.direction, DIRECTION_UP)

    def test_user_put_item_to_inventory(self):
        user = User("TestUser_Name")
        self.assertEqual(user.inventory.count(TREASURE), 0)
        user.to_inventory(TREASURE)
        self.assertEqual(user.inventory.count(TREASURE), 1)

    def test_user_has_items(self):
        user = User("TestUser_Name")
        self.assertTrue(user.has(0, TREASURE))
        self.assertEqual(user.inventory.count(TREASURE), 0)

        self.assertFalse(user.has(1, TREASURE))
        user.to_inventory(TREASURE)
        self.assertTrue(user.has(1, TREASURE))

    def test_user_is_dead(self):
        user = User("TestUser_Name")
        self.assertFalse(user.is_dead())

        user.health = 0
        self.assertTrue(user.is_dead())

    @patch("src.map.Map")
    def test_place_on_map(self, MockMap):
        x, y = randint(0, 10), randint(0, 20)
        user = User("TestUser_Name")
        attrs = {"get_empty_random_position.return_value": (x, y)}
        MockMap.configure_mock(**attrs)
        user.place_on(MockMap)
        self.assertEqual(user.position, [x, y])
        MockMap.put.assert_called_with(x, y, USER)

    def test_can_walk_to(self):
        user = User("TestUser_Name")
        knowledge_about = Empty([0, 0])
        self.assertEqual(user.can_walk_to(DIRECTION_UP, knowledge_about),
                         [DIRECTION_UP, DIRECTION_DOWN, DIRECTION_LEFT, DIRECTION_RIGHT])

        knowledge_about = Stone([0, 0])
        self.assertEqual(user.can_walk_to(DIRECTION_UP, knowledge_about),
                         [DIRECTION_DOWN, DIRECTION_LEFT, DIRECTION_RIGHT])

        knowledge_about = Treasure([0, 0])
        self.assertEqual(user.can_walk_to(DIRECTION_LEFT, knowledge_about),
                         [DIRECTION_UP, DIRECTION_DOWN, DIRECTION_RIGHT])

    @patch("src.brain.Treasure")
    def test_user_do(self, MockTreasure):
        user = User("TestUser_Name")
        map = Map()
        user.action = PICK_UP
        MockTreasure.can_do.return_value = [PICK_UP]
        user.do(map, MockTreasure)
        MockTreasure.do.assert_called_with(user, user.action, map)

    @patch("src.map.Map")
    @patch("src.brain.Brain")
    def test_change_direction_if_user_move(self, MockBrain, MockMap):
        user = User("TestUser_Name")
        user.brain = MockBrain
        user.move(DIRECTION_DOWN, MockMap)
        self.assertEqual(user.direction, DIRECTION_DOWN)

        direction = choice(user.directions)
        user.move(direction, MockMap)
        self.assertEqual(user.direction, direction)
#  остановился на 15 минуте седьмой части видео https://www.youtube.com/watch?v=rlu16b0PdFw
# разнесение по разным тестам.


if __name__ == "__main__":
    unittest.main()
