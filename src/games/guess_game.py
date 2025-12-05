import time, random

def show_instructions():
    """Displays game instructions."""
    print("Here are the instructions to the game.")
    time.sleep(0.2)
    print("We are only working with integer numbers, no fractions.")
    print("The computer will select a random number based on your chosen level.")
    print("You must guess the number, and hints will be provided if your guess is too high or too low.")
    print("The game tracks your number of attempts and ensures you don't repeat guesses.")
    print("Once you guess correctly, the game is over.")
    while True:
        escape_instruction = input("Press Enter to continue...")
        if escape_instruction != "".strip():
            print("Error! Please press enter to continue")
        else:
            break


def get_user_choice():
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

def play_level(level, max_number, max_attempts):
    """Handles gameplay for a given level."""
    print(f"\nLet's Begin! I have selected a number between 1 and {max_number}.")
    print(f"You have {max_attempts} attempts to guess it.")
    
    chosen_number = random.randint(1, max_number)
    attempts = 0
    guessed_numbers = set()
    
    while attempts < max_attempts:
        try:
            user_guess = int(input("Guess a number: "))
            if user_guess in guessed_numbers:
                print("You already guessed that number! Try a different one.")
                continue
            
            if 1 <= user_guess <= max_number:
                guessed_numbers.add(user_guess)
                attempts += 1
            else:
                print(f"Number must be between 1 and {max_number}. Try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if user_guess < chosen_number:
            print(f"Too low! Attempts left: {max_attempts - attempts}")
        elif user_guess > chosen_number:
            print(f"Too high! Attempts left: {max_attempts - attempts}")
        else:
            print(f"Congrats! You guessed the number {chosen_number} in {attempts} attempts!")
            return True
    
    print(f"Game Over! The correct number was {chosen_number}.")
    return False

def play():
    """Main function to run the Guessing Game."""
    print("Welcome to the Guessing Game!")
    time.sleep(1)
    while True:
        view_instruct = input("Do you want to view the instructions? [y/n]: ").strip().lower()
        if view_instruct in ['y', 'yes']:
            show_instructions()
            break
        elif view_instruct in ['n', 'no']:
            break
        else:
            print("Error! Please enter 'y' for yes or 'n' for no.")

    while True:
        choice = get_user_choice()
        if choice == 4:
            print("Thanks for playing! Goodbye.")
            break
        
        level_settings = {
            1: (50, 5),
            2: (100, 10),
            3: (200, 10)
        }
        max_number, max_attempts = level_settings[choice]
        
        while True:
            won = play_level(choice, max_number, max_attempts)
            while True:
                play_again = input("Do you want to play another round? [y/n]: ").strip().lower()
                if play_again in ['y', 'yes']:
                    break
                elif play_again in ['n', 'no']:
                    print("Returning to main menu...")
                    break
                else:
                    print("Error! Please enter 'y' for yes or 'n' for no.")
            if play_again in ['n', 'no']:
                break
