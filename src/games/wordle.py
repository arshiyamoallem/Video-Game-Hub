from time import sleep
import random

"""
Wordle:
This module implements a simple text-based wordle game. 
It presents a 5-letter unknown word that the user must guess in 6 tries,
and keeps track of the user's answers.
"""

class WordleGame:
    def __init__(self):
        self.max_attempts = 6
        self.word_length = 5
        self.word_list = self.get_words()
        self.reset_game()
        
        # ANSI color codes for terminal
        self.COLORS = {
            'green': '\033[92m',   # Bright green
            'yellow': '\033[93m',  # Bright yellow  
            'white': '\033[97m',   # Bright white (for wrong letters)
            'gray': '\033[90m',    # Gray (alternative for wrong)
            'reset': '\033[0m',    # Reset to default
            'bold': '\033[1m',
        }

    def reset_game(self):
        """Resets the game state for a new round."""
        self.secret_word = random.choice(self.word_list).upper()
        self.attempts = 0
        self.guesses = []
        self.game_over = False
        self.won = False

    def get_words(self):
        """Return the word list - NO API needed"""
        return [
            "APPLE", "BERRY", "CHERRY", "MANGO", "PEACH",
            "GRAPE", "LEMON", "LIMEY", "PLUMS", "PEARS",
            "LARGE", "SMALL", "QUICK", "SLOWY", "BRAVE",
            "MINOR", "MAJOR", "HAPPY", "SADLY", "ANGRY",
            "LIGHT", "DARKS", "SHINY", "DULLY", "CLEAN",
            "DIRTY", "FRESH", "STALE", "YOUNG", "OLDLY",
            "CLEAN", "ROCKS", "PAPER", "WATER", "CHAIR",
            "BRAIN", "DREAM", "EARTH", "FLAME", "GRAPE", 
            "HONEY", "IGLOO", "JUICE", "KNIFE", "LEMON",
            "MONEY", "NIGHT", "PEACE", "RANCH", "SUGAR",
            "OCEAN", "PIANO", "QUEEN", "RIVER", "SNAKE", 
            "TABLE", "UNITY", "FAITH", "GHOST", "HOUSE",
            "VOICE", "WATER", "YOUTH", "ZEBRA", "CLOUD", 
            "HEART", "IMAGE", "JELLY", "KARMA", "LIGHT", 
            "MAGIC", "NOISE", "UNION", "VALUE", "STEEL",
            "PARTY", "QUIET", "ROBOT", "SHAPE", "TOWER", 
            "WOMAN", "XENON", "YACHT", "ZESTY", "TRAIN",
        ]
        
    def validate_guess(self, guess):
        """Validate user's guess"""
        guess = guess.upper().strip()
        
        # Basic validation
        if len(guess) != self.word_length:
            return False, f"Guess must be exactly {self.word_length} letters"
        
        if not guess.isalpha():
            return False, "Guess must contain only letters"
        
        return True, ""
    
    def evaluate_guess(self, guess):
        """Evaluate guess against secret word and return color codes"""
        guess = guess.upper()
        secret_chars = list(self.secret_word)
        guess_chars = list(guess)
        result = [None] * self.word_length  # Initialize result list
        
        # First pass: Find correct letters in correct positions (GREEN)
        for i in range(self.word_length):
            if guess_chars[i] == secret_chars[i]:
                result[i] = (guess_chars[i], "green")
                secret_chars[i] = None
                guess_chars[i] = None
        
        # Second pass: Find correct letters in wrong positions (YELLOW)
        for i in range(self.word_length):
            if guess_chars[i] is not None:
                if guess_chars[i] in secret_chars:
                    result[i] = (guess_chars[i], "yellow")
                    secret_chars[secret_chars.index(guess_chars[i])] = None
                else:
                    result[i] = (guess_chars[i], "white")
        
        return result
    
    def colored_letter(self, letter, color):
        """Return a colored letter for display"""
        color_code = self.COLORS.get(color, self.COLORS['reset'])
        return f"{color_code}{letter}{self.COLORS['reset']}"
    
    def display_board(self):
        """Display the current game board with COLOR hints"""
        print(f"\n{'='*50}")
        print(f"{self.COLORS['bold']}WORDLE - Attempt {self.attempts}/{self.max_attempts}{self.COLORS['reset']}")
        print('='*50)
        
        for guess in self.guesses:
            result = self.evaluate_guess(guess)
            display_row = ""
            for letter, color in result:
                if color == "green":
                    display_row += f" {self.colored_letter(letter, 'green')}  "
                elif color == "yellow":
                    display_row += f" {self.colored_letter(letter, 'yellow')}  "
                else:  # white
                    display_row += f" {self.colored_letter(letter, 'white')}  "
            print(display_row)
        
        # Show empty slots for remaining attempts
        for _ in range(self.max_attempts - len(self.guesses)):
            print("  _     _     _     _     _  ")
        
        print('='*50)
        
        # Color legend
        print("\nColor Legend:")
        print(f"  {self.colored_letter('G', 'green')} - Correct letter, correct position")
        print(f"  {self.colored_letter('Y', 'yellow')} - Correct letter, wrong position")
        print(f"  {self.colored_letter('W', 'white')} - Letter not in word")
    
    def show_instructions(self):
        """Display game instructions with colors"""
        print("\n" + "="*60)
        print(f"{self.COLORS['bold']}🎮 WORDLE - Guess the 5-letter word!{self.COLORS['reset']}")
        print("="*60)
        print("HOW TO PLAY:")
        print(f"- You have {self.max_attempts} attempts to guess the word")
        print("- Each guess must be a valid 5-letter word")
        print("- After each guess, you'll get color hints:")
        
        print(f"\n  {self.colored_letter('G', 'green')} - Letter is correct and in right position")
        print(f"  {self.colored_letter('Y', 'yellow')} - Letter is in word but wrong position")
        print(f"  {self.colored_letter('W', 'white')} - Letter is not in the word")
        
        print("\nExample:")
        print("  Secret word: APPLE")
        print("  Your guess:  APRON")
        print("  Result:      ", end="")
        example_colors = ['green', 'green', 'white', 'white', 'white']
        example_letters = ['A', 'P', 'R', 'O', 'N']
        for i in range(5):
            print(f"{self.colored_letter(example_letters[i], example_colors[i])}  ", end="")
        print("\n               A,P correct; R,O,N not in word")
        print("="*60)
        
        input("\nPress Enter to continue...")
    
    def make_guess(self, guess):
        """Process a user guess"""
        valid, message = self.validate_guess(guess)
        if not valid:
            return False, [], message
        
        guess = guess.upper()
        self.attempts += 1
        self.guesses.append(guess)
        
        result = self.evaluate_guess(guess)
        
        if guess == self.secret_word:
            self.game_over = True
            self.won = True
            return True, result, f"{self.COLORS['green']}🎉 Congratulations! You guessed the word!{self.COLORS['reset']}"
        
        if self.attempts >= self.max_attempts:
            self.game_over = True
            return True, result, f"💀 Game over! The word was: {self.COLORS['bold']}{self.secret_word}{self.COLORS['reset']}"
        
        return True, result, ""
    
    def play(self):
        """Main game loop with colors"""
        # Show welcome and instructions only once
        print("\n" + "="*60)
        print(f"{self.COLORS['bold']}{self.COLORS['green']}🎮 WELCOME TO WORDLE!{self.COLORS['reset']}")
        print("="*60)
        
        # Ask if user wants instructions (only once)
        view_instructions = input("View instructions? (y/n): ").strip().lower()
        if view_instructions in ['y', 'yes']:
            self.show_instructions()
        
        # Game loop for multiple rounds
        while True:
            self.reset_game()
            
            print(f"\nI'm thinking of a {self.word_length}-letter word...")
            sleep(1)
            
            # Play one round
            while not self.game_over:
                self.display_board()
                
                guess = input(f"\nEnter your guess ({self.word_length} letters): ").strip()
                
                valid, result, message = self.make_guess(guess)
                
                if not valid:
                    print(f"❌ {message}")
                    continue
                
                if message:  # Game over message (win or lose)
                    self.display_board()
                    print(f"\n{message}")
                    break
                
                # Show feedback for this guess with colors
                print(f"\n{self.COLORS['bold']}Feedback:{self.COLORS['reset']}")
                feedback_row = ""
                for letter, color in result:
                    if color == "green":
                        feedback_row += f" {self.colored_letter(letter, 'green')}  "
                    elif color == "yellow":
                        feedback_row += f" {self.colored_letter(letter, 'yellow')}  "
                    else:
                        feedback_row += f" {self.colored_letter(letter, 'white')}  "
                print(feedback_row)
            
            # Ask to play again
            while True:
                play_again = input("\nPlay again? (y/n): ").strip().lower()
                if play_again in ['y', 'yes']:
                    print("\n" + "="*50)
                    print(f"{self.COLORS['bold']}STARTING NEW GAME{self.COLORS['reset']}")
                    print("="*50)
                    break  # Break out of the play-again question loop to start new game
                elif play_again in ['n', 'no']:
                    print("\nThanks for playing Wordle!")
                    sleep(1)
                    return  # Exit the entire play() method
                else:
                    print("Please enter 'y' or 'n'")