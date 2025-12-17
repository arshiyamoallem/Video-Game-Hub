import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from games.guess_game import GuessNumberGame
from games.quiz_game import QuizGame
from games.rock_paper_scissors import RockPaperScissors
from hub.game_hub import GameHub

import unittest
from unittest.mock import patch, MagicMock

class TestGameHub(unittest.TestCase):
    
    def setUp(self):
        self.hub = GameHub()

    def tearDown(self):
        return super().tearDown()
    
    def test_init(self):
        self.assertIn(1, self.hub.games)
        self.assertIs(self.hub.games[1], GuessNumberGame)

        self.assertIn(2, self.hub.games)
        self.assertIs(self.hub.games[2], RockPaperScissors)
        
        self.assertIn(3, self.hub.games)
        self.assertIs(self.hub.games[3], QuizGame)

        self.assertEqual(len(self.hub.games), 3, "Should have exactly 3 games")

        # Check they are classes, not instances (no parentheses)
        self.assertTrue(callable(self.hub.games[1]))  # Classes are callable
        self.assertTrue(callable(self.hub.games[2]))
        self.assertTrue(callable(self.hub.games[3]))

        #print("✅ All tests passed!")

if __name__ == '__main__':
    unittest.main()