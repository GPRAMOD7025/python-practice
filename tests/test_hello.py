import unittest

from hello import greet


class TestGreet(unittest.TestCase):
    def test_greet_returns_name(self):
        self.assertEqual(greet("Pramod"), "Hello my friend, Pramod!")


if __name__ == "__main__":
    unittest.main()
