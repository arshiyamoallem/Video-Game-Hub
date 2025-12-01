"""
VIDEO GAME HUB
A cool coding project design using time and sys libraries. 
A simple hub where you can play any sort of game
"""
import guess_game as g
import rock_paper_scissors as rps
import quiz_game as qg
import time, sys

#________________________________________________________________________________________________________________________________
def loading_animation(text: str) -> str:
    if True:
        for _ in range(3):
            for dot_count in range(1, 4):  # Count from 1 to 3 dots
                sys.stdout.write(f"\r{text}{'.' * dot_count}")  # Overwrite the line with dots
                sys.stdout.flush()  # Force it to print immediately
                time.sleep(0.8)  
                sys.stdout.write("\r" + text + "   ")  # Ensure to preserve the 'Exiting' text
                sys.stdout.flush()  # Clear the line properly
        sys.stdout.write("\r" + " " * len(text))  # Overwrite with spaces
        sys.stdout.flush()  # Clear the text from the screen
        time.sleep(0.15)  # Short delay before showing the final message

    print("\nThank you for playing! Goodbye!\n\n")
#________________________________________________________________________________________________________________________________

while True:

    print("Video Game Hub")
    print("_______________________________________")
    print("1- Guess the Number\n2- Rock Paper Scissors Game\n3- Quiz Game\n4- Exit")
    print("_______________________________________")

    try:
        choice = int(input("Your choice: ").strip())
        print("\n\n")

        if choice == 1:
            g.guessing_game() # 1st game
            loading_animation("Returning back to hub") 
            continue
        
        elif choice == 2:
            rps.rock_paper_scissors() # 2nd game
            loading_animation("Returning back to hub") 
            continue

        elif choice == 3:
            qg.quiz() # 3rd game
            loading_animation("Returning back to hub") 
            continue

        elif choice == 4:
            #exit program
            loading_animation("Exiting Program") 
            break  
        
        else:
            #For invalid entries in the program
            print("\nInvalid entry! \n")
            continue

    except ValueError:
        #For invalid values in the program
        time.sleep(0.3)
        print("Unknown Entry. Try again")

