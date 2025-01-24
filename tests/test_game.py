import unittest
from src.game import GameManager

class TestGameManager(unittest.TestCase):

    def test_play_round(self):
        game = GameManager()
        self.assertEqual(game.play_round("k", "s"), 1)
        self.assertEqual(game.play_round("k", "k"), 0)
        self.assertEqual(game.play_round("p", "s"), -1)

if __name__ == "__main__":
    unittest.main()