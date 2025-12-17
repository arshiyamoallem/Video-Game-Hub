import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
import unittest
from games.rock_paper_scissors import RockPaperScissors



class TestRockPaperScissors(unittest.TestCase):
    
    def setUp(self):
        self.game = RockPaperScissors()
    
    def test_init(self):
        """Test basic initialization"""
        self.assertIsNotNone(self.game)
        
        # Should have choices list
        self.assertIsInstance(self.game.choices, list)
        self.assertEqual(len(self.game.choices), 3)
        
        # Should have win_map dictionary
        self.assertIsInstance(self.game.win_map, dict)
        self.assertEqual(len(self.game.win_map), 3)
    
    def test_choices_list(self):
        """Test that choices are correct"""
        expected_choices = ['rock', 'paper', 'scissors']
        self.assertEqual(self.game.choices, expected_choices)
        
        # Check all are strings
        for choice in self.game.choices:
            self.assertIsInstance(choice, str)
    
    def test_win_map_structure(self):
        """Test win_map has correct structure"""
        # Check all choices are in win_map as keys
        for choice in self.game.choices:
            self.assertIn(choice, self.game.win_map)
            
        # Check values are also valid choices
        for winner, loser in self.game.win_map.items():
            self.assertIn(loser, self.game.choices)
    
    def test_win_map_logic(self):
        """Test that win_map has correct winning logic"""
        # Rock beats scissors
        self.assertEqual(self.game.win_map['rock'], 'scissors')
        
        # Paper beats rock  
        self.assertEqual(self.game.win_map['paper'], 'rock')
        
        # Scissors beats paper
        self.assertEqual(self.game.win_map['scissors'], 'paper')
    
    def test_game_rules(self):
        """Test the game rules directly"""
        # Test all combinations
        test_cases = [
            # (user, computer, expected_result)
            ('rock', 'rock', 'tie'),
            ('rock', 'paper', 'lose'),
            ('rock', 'scissors', 'win'),
            ('paper', 'rock', 'win'),
            ('paper', 'paper', 'tie'),
            ('paper', 'scissors', 'lose'),
            ('scissors', 'rock', 'lose'),
            ('scissors', 'paper', 'win'),
            ('scissors', 'scissors', 'tie'),
        ]
        
        for user_choice, computer_choice, expected_result in test_cases:
            # Simulate the game logic
            if user_choice == computer_choice:
                result = 'tie'
            elif self.game.win_map[user_choice] == computer_choice:
                result = 'win'
            else:
                result = 'lose'
            
            self.assertEqual(result, expected_result,
                           f"{user_choice} vs {computer_choice} should be {expected_result}")
    
    def test_choice_validation(self):
        """Test that only valid choices are accepted"""
        valid_choices = ['rock', 'paper', 'scissors']
        invalid_choices = ['', 'RaCk', 'Papper', 'scissor', 'lizard', 'spock', '123', None]
        
        # Test valid choices
        for choice in valid_choices:
            self.assertIn(choice, self.game.choices)
        
        # Test invalid choices (should not be in choices list)
        for choice in invalid_choices:
            if isinstance(choice, str):
                self.assertNotIn(choice.lower(), self.game.choices)
    
    def test_case_insensitive_support(self):
        """Test that game could support case-insensitive input (if implemented)"""
        # Note: This tests the POSSIBILITY, not the actual implementation
        test_cases = ['rock', 'ROCK', 'Rock', 'rOcK']
        
        for test_input in test_cases:
            normalized = test_input.lower()
            self.assertEqual(normalized, 'rock')

if __name__ == '__main__':
    unittest.main()