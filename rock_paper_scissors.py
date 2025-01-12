import random
import time

def rock_paper_scissors():
    play_game = True  # Controls the main game loop
    
    # Welcome message
    print("Welcome to Rock, Paper, Scissors!")
    time.sleep(1)
    print("Let's play a game.")    

    while play_game:
        print("Rock Paper Scissors Game Hub")
        print("_______________________________________")
        print("Press enter if you want to play.\nType exit if you want to leave.")
        print("_______________________________________")
        decision = input("Enter your choice: ").lower()     

        if decision == '':  # Start the game when the user presses enter
            round = True  # Game round starts
            while round:
                choices = ['rock', 'paper', 'scissors']
                computer_choice = random.choice(choices)
                user_choice = input("Enter rock, paper, or scissors: ").lower()
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
                print(f"Computer Choice: {computer_choice}.")

                if user_choice == computer_choice:
                    print("It's a tie!\n")
                elif win_condition[user_choice] == computer_choice:
                    print("You win!\n")
                else:
                    print("You lose!\n")

                while True:
                    restart_input = input("Do you want to return to the hub? [y/n]: ").lower()
                    if restart_input in ['y', 'n']:
                        time.sleep(0.5)
                        if restart_input == 'n':
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
