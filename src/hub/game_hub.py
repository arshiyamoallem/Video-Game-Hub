import time, sys
from games import GuessNumberGame, RockPaperScissors, QuizGame

class GameHub:
    def __init__(self):
        self.games = {
            1: GuessNumberGame,
            2: RockPaperScissors,
            3: QuizGame,
        }
    def loading_animation(self, text: str) -> None:
        for _ in range(3):
            for dot_count in range(1, 4):  
                sys.stdout.write(f"\r{text}{'.' * dot_count}")  # Overwrite the line with dots
                sys.stdout.flush()  
                time.sleep(0.5)  
                sys.stdout.write("\r" + text + "   ")  
                sys.stdout.flush()  
        sys.stdout.write("\r" + " " * len(text))  
        sys.stdout.flush() 
        print() 
    
    
    def display_menu(self) -> None:
        """Print the main hub menu."""
        print("\nVideo Game Hub")
        print("_______________________________________")
        print("1- Guess the Number")
        print("2- Rock Paper Scissors Game") 
        print("3- Quiz Game") 
        print("4- Exit")     
        print("_______________________________________")

    def run(self) -> None: 
        while True:
            self.display_menu()
            try:
                choice = int(input("Your choice: ").strip())
                print("\n")

                if choice in self.games:
                    game = self.games[choice]()
                    game.play()
                    self.loading_animation("Returning back to hub") 

                elif choice == 4:
                    self.loading_animation("Exiting Program") 
                    print("Thank you for playing! Goodbye!\n")
                    break  
                
                else:
                    print("Invalid menu option! Choose 1-4.\n")

            except ValueError:
                print("Unknown Entry. Try again")