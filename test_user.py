import unittest

from src.user import User


class UserTestCase(unittest.TestCase):
    
    def tests_make_user_object(self):
        name = "UserName"
        user = User(name)
        self.assertIsNotNone(user)
        self.assertEqual(user.name, name)
    
if __name__ == "__main__":
    unittest.main()
