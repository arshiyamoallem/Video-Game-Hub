import random, time

"""
Simple rock paper scissors game implemented using a hub along 
with an input from a user to decide if he wishes to play a game or not.
"""
class RockPaperScissors:
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors']
        self.win_map = {
            'rock': 'scissors',  
            'paper': 'rock',     
            'scissors': 'paper'  
        }
    
    def show_instructions(self) -> None:
        """Display game instructions."""
        instructions = [
            "Here are the instructions to the game.\n",
            "1. Rock-Paper-Scissors is a game where you have two players. In this case, the computer vs you.",
            "2. You choose rock, paper or scissors.",
            "3. The computer will randomly choose to throw as well.",
            "4. Rock beats scissors, scissors beats paper, and paper beats rock",
            "5. If you both throw the same hand, it's a tie.",
            "6. Make sure not to lose to the computer. Let's see what you got!",
            "Good luck!\n"
        ]
        
        for line in instructions:
            print(line)
            time.sleep(0.2)

        while True:
            esc = input("Press Enter to continue...").strip()
            if esc == "":
                break
            print("Error! Please press Enter only.")

    def play_round(self) -> None:
        """Plays one round of the game."""
        user_choice = input("Enter rock, paper, or scissors: ").strip().lower()

        if user_choice not in self.choices:
            print("Invalid choice! Try again.\n")
            return

        computer_choice = random.choice(self.choices)
        time.sleep(0.5)
        print(f"Computer throws {computer_choice}.")

        if user_choice == computer_choice:
            print("It's a tie!\n")
        elif self.win_map[user_choice] == computer_choice:
            print("You win!\n")
        else:
            print("You lose!\n")

    def play(self) -> None:
            """Main function to run the Rock-Paper-Scissors game."""
            print("Welcome to Rock, Paper, Scissors!\n")
            time.sleep(1)

            while True:
                view = input("View instructions? [y/n]: ").strip().lower()
                if view in ("y", "yes"):
                    self.show_instructions()
                    break
                elif view in ("n", "no"):
                    break
                else:
                    print("Error! Please enter 'y' or 'n'.\n")

            while True:
                print("\nPress Enter to play, or type 'exit' to return to the hub.")
                decision = input("Your choice: ").strip().lower()
                print()

                if decision == "":
                    self.play_round()
                elif decision == "exit":
                    return
                else:
                    print("Invalid entry! Try again.\n")
