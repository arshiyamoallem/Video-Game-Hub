    def test_choice_validation(self):
        """Test that only valid choices are accepted"""
        valid_choices = ['rock', 'paper', 'scissors']
        invalid_choices = ['', 'ROCK', 'Paper', 'scissor', 'lizard', 'spock', '123', None]
        
        # Test valid choices
        for choice in valid_choices:
            self.assertIn(choice, self.game.choices)
        
        # Test invalid choices (should not be in choices list)
        for choice in invalid_choices:
            if isinstance(choice, str):
                self.assertNotIn(choice.lower(), self.game.choices)