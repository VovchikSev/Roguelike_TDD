import unittest
from random import randint
from unittest.mock import patch

from src.brain import Brain
from src.options import *
from src.user import User


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
    
    def test_user_has_barain(self):
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
    def test_user_see(self, MockMap):
        user = User("TestUser_Name")
        attrs = {"get_in_direction.return_value": TREE}
        MockMap.configure_mock(**attrs)
        self.assertEqual(user.see(MockMap), TREE)
    
    @patch("src.map.Map")
    def test_place_on_map(self, MockMap):
        x, y = randint(0, 10), randint(0, 20)
        user = User("TestUser_Name")
        attrs = {"get_empty_random_position.return_value": (x, y)}
        MockMap.configure_mock(**attrs)
        user.place_on(MockMap)
        self.assertEqual(user.position, [x, y])
        MockMap.put.assert_called_with(x, y, USER)
    
    # @unittest.skip('Реализуем мозги')
    def test_user_can_do_action(self):
        user = User("TestUser_Name")
        self.assertEqual(user.can_do_action(EMPTY), {'message': MESSAGE_EMPTY, 'action': [DIRECTION_UP,
                                                                                          DIRECTION_DOWN,
                                                                                          DIRECTION_LEFT,
                                                                                          DIRECTION_RIGHT]})
        self.assertEqual(user.can_do_action(TREE), {'message': MESSAGE_TREE, 'action': [DIRECTION_UP,
                                                                                        DIRECTION_DOWN,
                                                                                        DIRECTION_LEFT,
                                                                                        DIRECTION_RIGHT,
                                                                                        HACK]})
        self.assertEqual(user.can_do_action(STONE), {'message': MESSAGE_STONE, 'action': [DIRECTION_UP,
                                                                                          DIRECTION_DOWN,
                                                                                          DIRECTION_LEFT,
                                                                                          DIRECTION_RIGHT]})
        self.assertEqual(user.can_do_action(LETTER), {'message': MESSAGE_LETTER, 'action': [DIRECTION_UP,
                                                                                            DIRECTION_DOWN,
                                                                                            DIRECTION_LEFT,
                                                                                            DIRECTION_RIGHT, READ]})
        self.assertEqual(user.can_do_action(TREASURE), {'message': MESSAGE_TREASURE, 'action': [DIRECTION_UP,
                                                                                                DIRECTION_DOWN,
                                                                                                DIRECTION_LEFT,
                                                                                                DIRECTION_RIGHT,
                                                                                                PICK_UP]})
    
    def test_user_action(self):
        user = User("TestUser_Name")
        self.assertTrue(False)


if __name__ == "__main__":
    unittest.main()
