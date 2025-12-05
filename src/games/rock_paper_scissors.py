import random
import time

"""
Simple rock paper scissors game implemented using a hub along 
with an input from a user to decide if he wishes to play a game or not.
"""

def play():
    play_game = True  # Controls the main game loop
    
    # Welcome message
    print("Welcome to Rock, Paper, Scissors!")
    time.sleep(1)  
    redo = True
    instructions_shown = False  # To track if instructions have already been shown

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
                print("Here are the instructions to the game.\n")
                time.sleep(0.2)
                print("1. Rock-Paper-Scissors is a game where you have two players. In this case, the computer vs you.")
                time.sleep(0.2)
                print("2. You will throw of your choice either rock, paper or scissors.")
                time.sleep(0.2)
                print("3. The computer will randomly choose to throw rock, paper or scissors.")
                time.sleep(0.2)
                print("4. Remeber this, rock beats scissors, paper beats rock and scissors beats paper")
                time.sleep(0.2)
                print("5. If you throw the same hand as the computer, it's a tie.")
                time.sleep(0.2)
                print("6. Make sure not to lose to the computer. Let's see what you got!")
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
            

    while play_game:
        print("\nRock Paper Scissors Game Hub")
        print("_______________________________________")
        print("\n- Press enter if you want to play.\n- Type exit if you want to leave.")
        print("_______________________________________")

        try:
            decision = input("Which option do you want to choose: ").strip().lower()
            print("\n")
            round = True
            time.sleep(0.2)

        except decision != '' or decision != 'exit':
            time.sleep(0.5)
            print("\nInvalid entry")
            print("Enter a valid number\n")
            continue    

        if decision == '':  # Start the game when the user presses enter
            round = True  # Game round starts
            while round:
                choices = ['rock', 'paper', 'scissors']
                computer_choice = random.choice(choices)
                user_choice = input("Enter rock, paper, or scissors: ").strip().lower()
                time.sleep(0.5)

                win_condition = {
                    'rock': 'scissors',  # rock beats scissors
                    'paper': 'rock',     # paper beats rock
                    'scissors': 'paper'  # scissors beats paper
                }

                if user_choice not in choices:
                    print("Invalid choice! Please choose rock, paper, or scissors.\nTry again!\n")
                    continue  # Skip the rest of the loop and ask for input again

                time.sleep(1)
                print(f"Computer throws {computer_choice}.")

                if user_choice == computer_choice:
                    print("It's a tie!\n")

                elif win_condition[user_choice] == computer_choice:
                    print("You win!\n")

                else:
                    print("You lose!\n")

                while True:
                    restart_input = input("Do you want to return to the hub? [y/n]: ").strip().lower()
                    if restart_input in ['y', 'n']:
                        time.sleep(0.5)

                        if restart_input == 'y':
                            round = False  # End the round if 'n' is chosen
                            time.sleep(0.5)

                        break

                    else:
                        print("Invalid entry! Please enter 'y' or 'n'.\n")
                        time.sleep(0.2)

        elif decision == 'exit':  # Exit the game if the user types 'exit'
            return 
        
        else:
            print("Invalid entry! Try again.\n")

                       
