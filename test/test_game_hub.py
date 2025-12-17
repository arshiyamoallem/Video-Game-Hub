# test/test_guess_game.py (SUPER SIMPLE)
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import unittest
from games.guess_game import GuessNumberGame


class TestGuessNumberGame(unittest.TestCase):
    
    def setUp(self):
        self.game = GuessNumberGame()
    
    def test_init(self):
        """Test basic initialization"""
        # Game should exist
        self.assertIsNotNone(self.game)
        
        # Should have level_settings dictionary
        self.assertIsInstance(self.game.level_settings, dict)
        
        # Should have 3 levels
        self.assertEqual(len(self.game.level_settings), 3)
    
    def test_level_1_settings(self):
        """Test level 1 settings"""
        max_number, max_attempts = self.game.level_settings[1]
        self.assertEqual(max_number, 50)
        self.assertEqual(max_attempts, 5)
    
    def test_level_2_settings(self):
        """Test level 2 settings"""
        max_number, max_attempts = self.game.level_settings[2]
        self.assertEqual(max_number, 100)
        self.assertEqual(max_attempts, 10)
    
    def test_level_3_settings(self):
        """Test level 3 settings"""
        max_number, max_attempts = self.game.level_settings[3]
        self.assertEqual(max_number, 200)
        self.assertEqual(max_attempts, 10)
    
    def test_levels_in_order(self):
        """Test that levels are in correct order (1, 2, 3)"""
        levels = list(self.game.level_settings.keys())
        self.assertEqual(levels, [1, 2, 3])

if __name__ == '__main__':
    unittest.main()