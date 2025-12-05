from time import sleep
"""
Quiz game:
This module implements a simple text-based multiple-choice quiz. 
It presents a series of questions, displays the possible answer options for each, 
accepts user input, and keeps track of the user's answers.
"""
class QuizGame:
    def __init__(self):
        self.questions = (
            "How many wheels does a car have: ",
            "How many meters are in a kilometer: ",
            "How many centimeters are in a meter: ",
            "How many zeros are in a million: ",
            "Which planet is the most similar to that of earth in this galaxy: "
        )

        self.options = (
            ("A. 2 ", "B. 8", "C. 4", "D. 6"),
            ("A. 100", "B. 10", "C. 10000", "D. 1000"),
            ("A. 100", "B. 10", "C. 10000", "D. 1000"),
            ("A. 7", "B. 8", "C. 6", "D. 5"),
            ("A. None", "B. Mars", "C. Saturn", "D. Mercury")
        )

        self.answers = ("C", "D", "A", "C", "B")

    def show_instructions(self) -> None:   
        """Displays game instructions."""
        print("Welcome to the Quiz Game!")
        sleep(.5)
        print("You will be presented with multiple-choice questions.")
        sleep(.5)
        print("Type the letter corresponding to your answer (A, B, C, or D) and press Enter.")
        sleep(.5)
        print("At the end of the quiz, your score will be displayed.")
        sleep(.5)
        print("Good luck!\n")
        
        while True:
            esc = input("Press Enter to continue...")
            if esc.strip() == "":
                break
            print("Error! Please press Enter only.")

    def ask_question(self, index: int) -> str:
        print("_____________________________________")
        sleep(.5)
        print(self.questions[index])

        for option in self.options[index]:
            sleep(0.2)
            print(option)

        # Validate user input
        while True:
            guess = input("Enter (A, B, C, D): ").strip().upper()
            if guess not in ('A', 'B', 'C', 'D'):
                print("\nPlease enter a valid option (A, B, C, D).\n")
            else:
                break  # Valid input, exit the loop
        
        correct = guess == self.answers[index]

        if correct:
            print("\nCORRECT!")
        else: 
            print("\nINCORRECT!\n")
            sleep(0.5)
            print(f"{self.answers[index]} is the correct answer!")
        
        return guess

    def play(self) -> None:
        """Main method to play the quiz game."""
        print("\nWelcome to the Quiz Game!\n")
        sleep(1)

        while True:
            view = input("View instructions? [y/n]: ").strip().lower()
            print("\n")
            if view in ('y', 'yes'):
                self.show_instructions()
                break
            elif view in ('n', 'no'):
                break
            else:
                print("Error! Please enter 'y' for yes or 'n' for no.\n")

        play_quiz = True

        while play_quiz:
            score = 0
            guesses = []
        
            for i in range(len(self.questions)):
                guess = self.ask_question(i)
                guesses.append(guess)
                
                if guess == self.answers[i]:
                    score += 1

            sleep(0.5)
            print("_______________________")
            print("\tRESULTS\t\n")

            print("Correct Answers: ", " | ".join(self.answers))
            print("Your Result: ", " | ".join(guesses))
            print()

            percent = int((score / (len(self.questions))) * 100)
            print(f"Your score is {percent}%.")
            print("_______________________\n")

            # Restart prompt
            while True:
                again = input("Would you like to try again? [y/n]: ").strip().lower()
                if again in ("y", "yes"):
                    break
                elif again in ("n", "no"):
                    play_quiz = False
                    print("\nReturning to main menu...\n")
                    break
                else:
                    print("Error! Please enter 'y' or 'n'.") 
