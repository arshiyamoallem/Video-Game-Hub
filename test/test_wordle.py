# test/test_wordle.py
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import unittest
from games.wordle import WordleGame


class TestWordleGame(unittest.TestCase):
    
    def setUp(self):
        self.game = WordleGame()
    
    def test_init(self):
        """Test basic game initialization"""
        self.assertIsNotNone(self.game)
        self.assertEqual(self.game.max_attempts, 6)
        self.assertEqual(self.game.word_length, 5)
        self.assertIsInstance(self.game.word_list, list)
    
    def test_reset_game(self):
        """Test game reset functionality"""
        self.game.reset_game()
        self.assertIsNotNone(self.game.secret_word)
        self.assertEqual(len(self.game.secret_word), 5)
        self.assertEqual(self.game.attempts, 0)
        self.assertFalse(self.game.game_over)
    
    def test_validate_guess(self):
        """Test guess validation"""
        # Valid guess
        valid, msg = self.game.validate_guess("APPLE")
        self.assertTrue(valid)
        
        # Invalid: wrong length
        valid, msg = self.game.validate_guess("APP")
        self.assertFalse(valid)
        
        # Invalid: non-alpha
        valid, msg = self.game.validate_guess("APP1E")
        self.assertFalse(valid)
    
    def test_evaluate_guess(self):
        """Test guess evaluation"""
        self.game.secret_word = "APPLE"
        
        # Perfect match
        result = self.game.evaluate_guess("APPLE")
        self.assertEqual(len(result), 5)
        for _, color in result:
            self.assertEqual(color, "green")
        
        # Partial match
        result = self.game.evaluate_guess("APRON")
        colors = [color for _, color in result]
        self.assertEqual(colors[:2], ["green", "green"])
    
    def test_make_guess(self):
        """Test making guesses"""
        self.game.secret_word = "APPLE"
        
        # Correct guess
        valid, result, msg = self.game.make_guess("APPLE")
        self.assertTrue(valid)
        self.assertTrue(self.game.won)
        self.assertIn("Congratulations", msg)
        
        # Reset for next test
        self.game.reset_game()
        self.game.secret_word = "APPLE"
        
        # Wrong guess
        valid, result, msg = self.game.make_guess("APRON")
        self.assertTrue(valid)
        self.assertEqual(msg, "")
        self.assertEqual(self.game.attempts, 1)


if __name__ == '__main__':
    unittest.main()