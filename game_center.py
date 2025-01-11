import time
import random
""" Guessing the number game

Instructions
1. Import Required Libraries
Use the random library to generate a random number.
2. Generate the Random Number
The computer will randomly select a number within a range (e.g., 1 to 100).
3. User Input
Prompt the user to guess the number.
4. Provide Hints
Compare the user's guess with the random number:
If it's too low, print "Too low! Try again."
If it's too high, print "Too high! Try again."
5. Keep Track of Guesses
Use a counter to track the number of attempts.
6. End the Game
When the user guesses correctly, print a success message with the number of attempts and exit the loop.
"""

def guessing_game(): 
    guess_game = True

    while guess_game:
        print("Welcome to the Guessing Game")
        time.sleep(1)
        
        play_guess_game = True
        redo = True

        while redo:
            instruction = input("Do you want to go over the instructions of the game? [y/n]: ")

            if instruction == 'n':
                print("\nSkipping instructions and moving to the next part of the game.")
                time.sleep(1)
                redo = False

            elif instruction == 'y':
                print("Here are the instructions to the game.")
                time.sleep(0.2)
                print("We are only working with integer numbers, no fractions.")
                time.sleep(0.2)
                print("The computer will select a random number between 1 and 100. You must guess the number chosen by the computer.")
                time.sleep(0.2)
                print("When you guess, the computer will give hints if your guess is too high or too low.")
                time.sleep(0.2)
                print("The game keeps track of how many guesses you've made and ensures you don't lose guesses by repeating the same number.")
                time.sleep(0.2)
                print("Once you guess the correct number, the game is over.")
                time.sleep(0.2)
                escape_instruction = input("To go to the next section, enter 'yes': ").lower()
                time.sleep(0.2)

                if escape_instruction == 'yes':
                    instruction = 'n'  # Ends the loop
                    redo = False

                    if instruction == 'n':
                        break  
                    
            else:
                print("\nInvalid entry! Try again.\n")
                
                
                

        while play_guess_game:
            print("_______________________________________")
            print("\nWe have 3 levels\n1- Level 1 is a number between 1 and 50\n2- Level 2 is a number between 1 and 100\n3- Level 3 is a number between 1 and 200\n4- Exit \n")
            print("_______________________________________")
            time.sleep(0.2)
            choice = int(input("Which option do you want to choose: "))
            round = True
            time.sleep(0.2)

            while round:

                if choice == 1:

                    print("Let's Begin\n")
                    time.sleep(0.2)
                    print("I have selected a number between 1 and 50.")
                    time.sleep(0.2)
                    print("You have 5 attempts to guess the number. Can you guess what it is?")
                    time.sleep(0.2)

                    chosen_number = random.randint(1,50)
                    attempts = 0

                    while attempts < 5:

                        try:
                            user_guess = int(input("Guess a number: "))

                            time.sleep(0.2)
                        
                        except ValueError:
                            print("Invalid entry")
                            print("Enter a valid number\n")
                            continue
                        
                        attempts += 1
                        time.sleep(0.2)

                        if 0 < user_guess < chosen_number:
                            print(f"\nToo low! Try again.\tAttempts: {attempts}\n")

                        elif 51 > user_guess > chosen_number:
                            print(f"\nToo High! Try again.\tAttempts: {attempts}\n")

                        elif user_guess == chosen_number:
                            print(f"Congrats! You guess the number {chosen_number} in {attempts} attempts.\n")
                            break

                        else:
                            print("\nError! Number must be in a range of 1-200.\nThis attempt will not count. Try again.\n")
                            attempts -= 1

                    if attempts >= 5 and user_guess != chosen_number:
                        time.sleep(0.2)
                        print(f"Game Over! The correct number was {chosen_number}.\n")
                                        
                    while True:
                        restart_input = input("Do you want to restart? [y/n]: ").lower()

                        if restart_input in ['y','n']:
                            time.sleep(.5)
                            break
                        else:
                            print("Invalid entry! Please enter 'y' or 'n'.\n")
                            time.sleep(.2)

                    if restart_input == 'n':
                        round = False
                        time.sleep(.5)

                elif choice == 2:
                    time.sleep(0.2)
                    print("Let's Begin\n")
                    time.sleep(0.2)
                    print("I have selected a number between 1 and 100.")
                    time.sleep(0.2)
                    print("You have 10 attempts to guess the number. Can you guess what it is?")
                    time.sleep(0.2)

                    chosen_number = random.randint(1,100)
                    attempts = 0

                    while attempts < 10:

                        try:
                            user_guess = int(input("Guess a number: "))
                        
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

                    if attempts >= 10 and user_guess != chosen_number:
                        print(f"Game Over! The correct number was {chosen_number}.\n")
                        time.sleep(0.2)
                        break

                    while True:
                        restart_input = input("Do you want to restart? [y/n]: ").lower()
                        
                        if restart_input in ['y','n']:
                            time.sleep(.5)
                            break
                        else:
                            print("Invalid entry! Please enter 'y' or 'n'.\n")
                            time.sleep(.2)

                    if restart_input == 'n':
                        round = False
                        time.sleep(.5)

                elif choice == 3:
                    time.sleep(0.2)
                    print("Let's Begin\n")
                    time.sleep(0.2)
                    print("I have selected a number between 1 and 200.")
                    time.sleep(0.2)
                    print("You have 10 attempts to guess the number. Can you guess what it is?")
                    time.sleep(0.2)

                    chosen_number = random.randint(1,200)
                    attempts = 0

                    while attempts < 10:
                        time.sleep(0.2)
                        try:
                            user_guess = int(input("Guess a number: "))
                        
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

                    if attempts >= 10 and user_guess != chosen_number:
                        print(f"Game Over! The correct number was {chosen_number}.\n")
                        time.sleep(0.2)
                        break

                    while True:
                        restart_input = input("Do you want to restart? [y/n]: ").lower()
                        
                        if restart_input in ['y','n']:
                            time.sleep(.5)
                            break
                        else:
                            print("Invalid entry! Please enter 'y' or 'n'.\n")
                            time.sleep(.2)

                    if restart_input == 'n':
                        round = False
                        time.sleep(.5)

                elif choice == 4:
                    time.sleep(0.2)
                    return
                
                else:
                    time.sleep(0.2)
                    print("\nInvalid entry! Try again\n")
                    time.sleep(0.2)
                    break
