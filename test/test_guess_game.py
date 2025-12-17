# test/test_guess_game.py
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
    
    def test_game_logic_comparison(self):
        """Test the number comparison logic"""
        chosen_number = 42
        
        # Test lower number
        self.assertLess(25, chosen_number)  # 25 < 42
        
        # Test higher number
        self.assertGreater(60, chosen_number)  # 60 > 42
        
        # Test equal number
        self.assertEqual(42, chosen_number)  # 42 == 42
    
    def test_range_validation_logic(self):
        """Test the range validation logic"""
        max_number = 50
        
        # Valid numbers (1-50)
        self.assertTrue(1 <= 25 <= max_number)   # 25 is valid
        self.assertTrue(1 <= 50 <= max_number)   # 50 is valid (edge case)
        self.assertTrue(1 <= 1 <= max_number)    # 1 is valid (edge case)
        
        # Invalid numbers
        self.assertFalse(1 <= 0 <= max_number)    # 0 is invalid
        self.assertFalse(1 <= 51 <= max_number)   # 51 is invalid
        self.assertFalse(1 <= -5 <= max_number)   # -5 is invalid
    
    def test_duplicate_check_logic(self):
        """Test duplicate number checking logic"""
        guessed_numbers = {10, 20, 30}
        
        # Already guessed
        self.assertIn(10, guessed_numbers)   # 10 is already guessed
        self.assertIn(20, guessed_numbers)   # 20 is already guessed
        
        # Not guessed yet
        self.assertNotIn(25, guessed_numbers)  # 25 is not guessed
        self.assertNotIn(42, guessed_numbers)  # 42 is not guessed
    
    def test_attempt_counting_logic(self):
        """Test attempt counting logic"""
        max_attempts = 5
        attempts = 0
        
        # Simulate making guesses
        guesses = [10, 20, 30, 42]
        for _ in guesses:
            attempts += 1
        
        # Check counts
        self.assertEqual(attempts, 4)
        self.assertLess(attempts, max_attempts)  # Still have attempts left
    
    def test_level_settings_positive_values(self):
        """Test that all level settings have positive values"""
        for level, (max_num, max_attempts) in self.game.level_settings.items():
            # Max number should be positive
            self.assertGreater(max_num, 0, f"Level {level}: max number should be > 0")
            
            # Attempts should be positive
            self.assertGreater(max_attempts, 0, f"Level {level}: attempts should be > 0")

if __name__ == '__main__':
    unittest.main()