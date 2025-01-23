#GUESS_GAME
import time
import random
"""
Guessing the Number Game

This function implements a simple game where the computer generates a random 
number, and the user attempts to guess that number. The game has a hub 
where the player has 4 options to choose from. The game provides feedback on whether 
the user's guess is too high, too low, or correct. The game also keeps track if the player
provides the correct type of number as it will only accept integer numbers.
It tracks the number of attempts and the game ends when the user guesses the correct number or
if the user has taken up all of their attempts. The game will then ask if you would like to restart 
the level you were at or if you would like to return the hub. 
"""
def guessing_game(): 
    # Set the game flag to True to start the game
    guess_game = True

    while guess_game:
        # Welcome message
        print("Welcome to the Guessing Game")
        time.sleep(1)
        
        # Flag to control whether to show instructions
        play_guess_game = True
        redo = True
        instructions_shown = False  # To track if instructions have already been shown

        while redo:
            if not instructions_shown:  # Only prompt for instructions if not already shown
                instruction = input("Do you want to go over the instructions of the game? [y/n]: ").strip().lower()

                # Skip instructions if the user chooses 'n'
                if instruction == 'n':
                    print("\nSkipping instructions and moving to the next part of the game.\n")
                    time.sleep(1)
                    redo = False  # Exit the loop
                    break

                # Show instructions if the user chooses 'y'
                elif instruction == 'y':
                    instructions_shown = True  # Mark instructions as shown
                    print("\nHere are the instructions to the game:\n")
                    time.sleep(0.2)
                    print("1. We are only working with integer numbers, no fractions.")
                    time.sleep(0.2)
                    print("2. The computer will select a random number between 1 and 100. You must guess the number.")
                    time.sleep(0.2)
                    print("3. The computer will give hints if your guess is too high or too low.")
                    time.sleep(0.2)
                    print("4. The game keeps track of your guesses and ensures you don't repeat numbers.")
                    time.sleep(0.2)
                    print("5. Once you guess the correct number, the game is over.")
                    time.sleep(0.2)

                    while True:  # Prompt until valid input
                        escape_instruction = input("To go to the next section, enter 'yes': ").strip().lower()
                        if escape_instruction == 'yes':
                            print("\nProceeding to the next part of the game\n")
                            redo = False  # Exit the loop
                            break
                        else:
                            print("\nInvalid entry! Please type 'yes' to proceed.\n")

                else:
                    # Handle invalid input for instructions
                    print("\nInvalid entry! Please type 'y' for yes or 'n' for no.\n")
            else:
                # If instructions are already shown, proceed
                print("\nProceeding to the next part of the game...\n")
                redo = False


        while play_guess_game:
            # Show game level options
            print("_______________________________________")
            print(
                "We have 3 levels\n"
                "1- Level 1 is a number between 1 and 50\n"
                "2- Level 2 is a number between 1 and 100\n"
                "3- Level 3 is a number between 1 and 200\n"
                "4- Exit"
            )
            print("_______________________________________")
            time.sleep(0.2)
            # User selects difficulty level
            try:
                choice = int(input("Which option do you want to choose: ").strip())
                print("\n")
                round = True
                time.sleep(0.2)

            except ValueError:
                time.sleep(0.5)
                print("\nInvalid entry")
                print("Enter a valid number\n")
                continue

            while round:
                # Level 1 game (1 to 50)
                if choice == 1:
                    print("Let's Begin\n")
                    time.sleep(0.2)
                    print("I have selected a number between 1 and 50.")
                    time.sleep(0.2)
                    print("You have 5 attempts to guess the number. Can you guess what it is?")
                    time.sleep(0.2)

                    # Randomly choose number between 1 and 50
                    chosen_number = random.randint(1,50)
                    attempts = 0

                    while attempts < 5:
                        try:
                            # User guesses a number
                            user_guess = int(input("Guess a number: ").strip())
                            time.sleep(0.2)
                        
                        except ValueError:
                            # Handle invalid input
                            print("Invalid entry")
                            print("Enter a valid number\n")
                            continue
                        
                        attempts += 1
                        time.sleep(0.2)

                        # Compare guess with the chosen number
                        if 0 < user_guess < chosen_number:
                            print(f"\nToo low! Try again.\tAttempts: {attempts}\n")

                        elif 51 > user_guess > chosen_number:
                            print(f"\nToo High! Try again.\tAttempts: {attempts}\n")

                        elif user_guess == chosen_number:
                            print(f"Congrats! You guess the number {chosen_number} in {attempts} attempts.\n")
                            break

                        else:
                            # Handle out-of-range guess
                            print("\nError! Number must be in a range of 1-200.\nThis attempt will not count. Try again.\n")
                            attempts -= 1

                    # End game if attempts run out
                    if attempts >= 5 and user_guess != chosen_number:
                        time.sleep(0.2)
                        print(f"Game Over! The correct number was {chosen_number}.\n")
                                        
                    # Ask user if they want to restart
                    while True:
                        restart_input = input("Do you want to restart? [y/n]: ").strip().lower()

                        if restart_input in ['y','n']:
                            time.sleep(.5)
                            break
                        else:
                            print("Invalid entry! Please enter 'y' or 'n'.\n")
                            time.sleep(.2)

                    if restart_input == 'n':
                        round = False
                        time.sleep(.5)

                # Level 2 game (1 to 100)
                elif choice == 2:
                    time.sleep(0.2)
                    print("Let's Begin\n")
                    time.sleep(0.2)
                    print("I have selected a number between 1 and 100.")
                    time.sleep(0.2)
                    print("You have 10 attempts to guess the number. Can you guess what it is?")
                    time.sleep(0.2)

                    # Randomly choose number between 1 and 100
                    chosen_number = random.randint(1,100)
                    attempts = 0

                    while attempts < 10:
                        try:
                            user_guess = int(input("Guess a number: ").strip())
                        
                        except ValueError:
                            print("Invalid entry")
                            print("Enter a valid number\n")
                            continue

                        time.sleep(0.2)
                        attempts += 1

                        if 0 < user_guess < chosen_number:
                            print(f"\nToo low! Try again.\tAttempts: {attempts}\n")

                        elif 101 > user_guess > chosen_number:
                            print(f"\nToo High! Try again.\tAttempts: {attempts}\n")

                        elif user_guess == chosen_number:
                            print(f"Congrats! You guess the number {chosen_number} in {attempts} attempts.\n")
                            break

                        else:
                            print("\nError! Number must be in a range of 1-200.\nThis attempt will not count. Try again.\n")
                            attempts -= 1

                    # End game if attempts run out
                    if attempts >= 10 and user_guess != chosen_number:
                        print(f"Game Over! The correct number was {chosen_number}.\n")
                        time.sleep(0.2)
                        break

                    # Ask for restart input
                    while True:
                        restart_input = input("Do you want to restart? [y/n]: ").strip().lower()
                        
                        if restart_input in ['y','n']:
                            time.sleep(.5)
                            break
                        else:
                            print("Invalid entry! Please enter 'y' or 'n'.\n")
                            time.sleep(.2)

                    if restart_input == 'n':
                        round = False
                        time.sleep(.5)

                # Level 3 game (1 to 200)
                elif choice == 3:
                    time.sleep(0.2)
                    print("Let's Begin\n")
                    time.sleep(0.2)
                    print("I have selected a number between 1 and 200.")
                    time.sleep(0.2)
                    print("You have 10 attempts to guess the number. Can you guess what it is?")
                    time.sleep(0.2)

                    # Randomly choose number between 1 and 200
                    chosen_number = random.randint(1,200)
                    attempts = 0

                    while attempts < 10:
                        time.sleep(0.2)
                        try:
                            user_guess = int(input("Guess a number: ").strip())
                        
                        except ValueError:
                            print("Invalid entry")
                            print("Enter a valid number\n")
                            continue
                        
                        attempts += 1

                        if 0 < user_guess < chosen_number:
                            print(f"\nToo low! Try again.\tAttempts: {attempts}\n")

                        elif 201 > user_guess > chosen_number:
                            print(f"\nToo High! Try again.\tAttempts: {attempts}\n")

                        elif user_guess == chosen_number:
                            print(f"Congrats! You guess the number {chosen_number} in {attempts} attempts.\n")
                            break

                        else:
                            print("\nError! Number must be in a range of 1-200.\nThis attempt will not count. Try again.\n")
                            attempts -= 1

                    # End game if attempts run out
                    if attempts >= 10 and user_guess != chosen_number:
                        print(f"Game Over! The correct number was {chosen_number}.\n")
                        time.sleep(0.2)
                        break

                    # Restart option for level 3
                    while True:
                        restart_input = input("Do you want to restart? [y/n]: ").strip().lower()
                        
                        if restart_input in ['y','n']:
                            time.sleep(.5)
                            break
                        else:
                            print("Invalid entry! Please enter 'y' or 'n'.\n")
                            time.sleep(.2)

                    if restart_input == 'n':
                        round = False
                        time.sleep(.5)

                # Exit option
                elif choice == 4:
                    time.sleep(0.2)
                    return
                
                else:
                    time.sleep(0.2)
                    print("\nInvalid entry! Try again\n")
                    time.sleep(0.2)
                    break
