import time, random

class GuessNumberGame:

    def __init__(self):
        # Level difficulty settings
        self.level_settings = {
            1: (50, 5),
            2: (100, 10),
            3: (200, 10),
        }

    def show_instructions(self) -> None:
        """Displays game instructions."""
        print("Here are the instructions to the game.")
        time.sleep(0.2)
        print("We are only working with integer numbers, no fractions.")
        print("The computer will select a random number based on your chosen level.")
        print("You must guess the number, and hints will be provided if your guess is too high or too low.")
        print("The game tracks your number of attempts and ensures you don't repeat guesses.")
        print("Once you guess correctly, the game is over.")
    
        while True:
            esc = input("Press Enter to continue...")
            if esc.strip() != "":
                print("Error! Please press enter to continue")
            else:
                break


    def get_user_choice(self) -> int:
        """Displays the level selection menu and returns the chosen level."""
        print("\nWe have 3 levels:")
        print("1 - Level 1 (1 to 50, 5 attempts)")
        print("2 - Level 2 (1 to 100, 10 attempts)")
        print("3 - Level 3 (1 to 200, 10 attempts)")
        print("4 - Exit")
        
        while True:
            try:
                choice = int(input("Choose a level: "))
                if 1 <= choice <= 4:
                    return choice
                else:
                    print("Invalid choice. Please enter a number between 1 and 4.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def play_level(self, max_number: int, max_attempts: int) -> bool:
        """Handles gameplay for a given level."""
        print(f"\nI picked a number between 1 and {max_number}.")
        print(f"You have {max_attempts} attempts.\n")
        
        chosen_number = random.randint(1, max_number)
        attempts = 0
        guessed = set()
        
        while attempts < max_attempts:
            try:
                guess = int(input("Guess a number: ").strip())
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue

            if guess in guessed:
                print("You already guessed that!")
                continue
            
            if not (1 <= guess <= max_number):
                print(f"Enter a number between 1 and {max_number}.")
                continue

            guessed.add(guess)
            attempts += 1

            if guess < chosen_number:
                print(f"Too low! Attempts left: {max_attempts - attempts}")
            elif guess > chosen_number:
                print(f"Too high! Attempts left: {max_attempts - attempts}")
            else:
                print(f"Congrats! You found {chosen_number} in {attempts} tries!")
                return True
        
        print(f"Out of attempts! Number was {chosen_number}.")
        return False

    def play(self) -> None:
        """Main function to run the Guessing Game."""
        print("Welcome to the Guessing Game!")
        time.sleep(1)
        while True:
            view = input("View instructions? [y/n]: ").strip().lower()
            if view in ("y", "yes"):
                self.show_instructions()
                break
            elif view in ("n", "no"):
                break
            else:
                print("Error! Please enter 'y' for yes or 'n' for no.")

        while True:
            choice = self.get_user_choice()
            if choice == 4:
                print("Thanks for playing! Goodbye.")
                break
            
            max_number, max_attempts = self.level_settings[choice]
            
            while True:
                self.play_level(max_number, max_attempts)
                
                again = input("Play another round? [y/n]: ").strip().lower()
                if again in ("n", "no"):
                    print("Returning to main menu...\n")
                    break
                elif again not in ("y", "yes"):
                    print("Please enter 'y' or 'n'.")