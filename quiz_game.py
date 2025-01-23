"""
I want to create my own game
"""
def quiz():
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
        print("_______________________")
        print(question)
        for option in options[question_num]:
            print(option)
        
        guess = input("Enter (A, B, C, D): ").upper()
        guesses.append(guess)
        
        if guess == answers[question_num]:
            score += 1
            print("CORRECT!")
        
        else:
            print("INCORRECT!")
            print(f"{answers[question_num]} is the correct answer!")
        
        question_num += 1

    print("_______________________")
    print("\tRESULTS\t")
    print("_______________________")

    print("answers: ", end = "")
    for answer in answers:
        print(answer, end = " ")
    print()

    print("guesses: ", end = "")
    for guess in guesses:
        print(guess, end = " ")
    print()

    score = int((score / (len(questions))) * 100)
    print(f"Your score is {score}%.")
