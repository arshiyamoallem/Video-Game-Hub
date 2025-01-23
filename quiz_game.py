from time import * 
"""
Quiz game:
The function "quiz()" implements a simple text-based multiple-choice quiz. 
It presents a series of questions, displays the possible answer options for each, 
accepts user input, and keeps track of the user's answers.
"""
def quiz():
    play_quiz = True
    while play_quiz:
        questions = ("How many wheels does a car have: ",
                    "How many meters are in a kilometer: ",
                    "How many centimeters are in a meter: ",
                    "How many zeros are in a million: ",
                    "Which planet is the most similar to that of earth in this galaxy: "
                    )

        options = (("A. 2 ", "B. 8", "C. 4", "D. 6"),
                ("A. 100", "B. 10", "C. 10000", "D. 1000"),
                ("A. 100", "B. 10", "C. 10000", "D. 1000"),
                ("A. 7", "B. 8", "C. 6", "D. 5"),
                ("A. None", "B. Mars", "C. Saturn", "D. Mercury"))

        answers = ("C","D","A","C","B")
        guesses = []
        score = 0
        question_num = 0

        for question in questions:
            print("_____________________________________")
            sleep(.5)
            print(question)
            for option in options[question_num]:
                sleep(.2)
                print(option)
            
            while True:
                guess = input("Enter (A, B, C, D): ").strip().upper()
                if guess not in ('A', 'B', 'C', 'D'):
                    print("\nPlease enter a valid option (A, B, C, D).\n")
                else:
                    break  # Valid input, exit the loop

            sleep(.5)

            if guess == answers[question_num]:
                    score += 1
                    print("\nCORRECT!")

            else:
                print("\nINCORRECT!\n")
                sleep(.5)
                print(f"{answers[question_num]} is the correct answer!")

            sleep(0.5)
            question_num += 1

        print("_______________________")
        print("\tRESULTS\t\n")
        
        sleep(.5)

        print("answers: ", end = "")
        for answer in answers:
            print(answer, end = " ")
        print("\n")
        
        print("guesses: ", end = "")
        for guess in guesses:
            print(guess, end = " ")
        print("\n")
        
        sleep(.5)

        score = int((score / (len(questions))) * 100)
        print(f"Your score is {score}%.")
        print("_______________________\n")
    
        while True: 
            sleep(0.5)
            restart_quiz = input("Would you like to try again? [y/n]: ").strip().lower()
            print("\n")

            if restart_quiz == 'n':
                sleep(0.5)
                play_quiz = False
                break

            elif restart_quiz == 'y':
                sleep(0.5)
                break

            else:
                sleep(0.5)
                print("Error! Please enter either 'y' or 'n'.\n")  
     
