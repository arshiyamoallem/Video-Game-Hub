"""
VIDEO GAME HUB
A cool coding project design using time and sys libraries. 
A simple hub where you can play any sort of game
"""
import time, sys
import guess_game as GuessGame
import rock_paper_scissors as RockPaperScissors
import quiz_game as QuizGame

class GameHub:
    def __init__(self):
        # self.games = {
        #     1:GuessGame(),
        #     2:RockPaperScissors(),
        #     3:QuizGame(),
        # }
        self.games = {
            1: GuessGame.play,
            2: RockPaperScissors.play,
            3: QuizGame.play,
        }
    def loading_animation(self, text: str) -> str:
        for _ in range(3):
            for dot_count in range(1, 4):  
                sys.stdout.write(f"\r{text}{'.' * dot_count}")  # Overwrite the line with dots
                sys.stdout.flush()  
                time.sleep(0.5)  
                sys.stdout.write("\r" + text + "   ")  
                sys.stdout.flush()  
        sys.stdout.write("\r" + " " * len(text))  
        sys.stdout.flush() 
        print("\n") 

    def display_menu(self):

        print("\nVideo Game Hub")
        print("_______________________________________")
        print("1- Guess the Number")
        print("2- Rock Paper Scissors Game") 
        print("3- Quiz Game") 
        print("4- Exit")     
        print("_______________________________________")

    def run(self):
        while True:
            self.display_menu()
            try:
                choice = int(input("Your choice: ").strip())
                print("\n")

                if choice in self.games:
                    #self.games[choice].play() # Call the play function of the selected game using OOP
                    # will use this until I edit other files to be implemented with OOP
                    self.games[choice]()
                    self.loading_animation("Returning back to hub") 

                elif choice == 4:
                    self.loading_animation("Exiting Program") 
                    print("Thank you for playing! Goodbye!\n")
                    break  
                
                else:
                    print("\nInvalid entry! \n")

            except ValueError:
                print("Unknown Entry. Try again")

if __name__ == "__main__":
    game_hub = GameHub()
    game_hub.run()