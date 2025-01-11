"""
VIDEO GAME HUB
A cool coding project design using time and sys libraries. 
A simple hub where you can play any sort of game
"""
#import guess_game
import game_center 
import time
import sys

#________________________________________________________________________________________________________________________________
def loading_animation(text: str) -> str:
    if True:
        for _ in range(3):
            for dot_count in range(1, 4):  # Count from 1 to 3 dots
                sys.stdout.write(f"\r{text}{'.' * dot_count}")  # Overwrite the line with dots
                sys.stdout.flush()  # Force it to print immediately
                time.sleep(1)  
                sys.stdout.write("\r" + text + "   ")  # Ensure to preserve the 'Exiting' text
                sys.stdout.flush()  # Clear the line properly
        sys.stdout.write("\r" + " " * len(text))  # Overwrite with spaces
        sys.stdout.flush()  # Clear the text from the screen
        time.sleep(0.5)  # Short delay before showing the final message

    print("\nThank you for playing! Goodbye!\n\n")
#________________________________________________________________________________________________________________________________
while True:

    print("Video game hub")
    print("_______________________________________")
    print("1- Guess the number\n2- Black Jack\n3- Exit")
    print("_______________________________________")
    choice = int(input("Your choice: "))

    if choice == 1:
        game_center.guessing_game()
        loading_animation("Returning back to hub")
        continue
    
    elif choice == 2:
        game_center.blackjack_game()
        loading_animation("Returning back to hub") 
        continue

    elif choice == 3:
        loading_animation("Exiting Program")
        break

    else:
        print("\nInvalid entry! \n")
        continue
