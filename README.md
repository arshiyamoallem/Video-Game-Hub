# Video Game Hub

A simple, interactive **text-based game hub** built in Python. This project offers a central interface to play three classic games:

- **Guess the Number** - Try to guess a random number within limited attempts
- **Rock Paper Scissors** - Classic hand game against the computer
- **Multiple Choice Quiz** - Test your knowledge with trivia questions
- **Wordle** - Popular word guessing game with color-coded feedback

Each game runs in the terminal and includes instructions, input validation, and playful animations for a smooth experience.

---

## Features

- **Central Game Hub** - Easy navigation between games
- **Interactive Gameplay** - Engaging terminal-based interfaces
- **Detailed Instructions** - Help available for each game
- **Input Validation** - Robust error handling for user inputs
- **Loading Animations** - Visual feedback during transitions
- **Replay Options** - Play again or return to hub
- **Modular Design** - Clean, organized, and maintainable code

---

## Project Structure
```
📂 Video-Game-Hub/
│
├── 📂 src/
│ ├── main.py # Main entry point
│ │
│ ├── 📂 hub/ # Game hub module
│ │ ├── init.py # Package exports
│ │ └── game_hub.py # Main hub logic and menu
│ │
│ └── 📂 games/ # Individual games module
│ ├── init.py # Game class exports
│ ├── guess_game.py # Number guessing game
│ ├── rock_paper_scissors.py # Rock Paper Scissors
│ ├── quiz_game.py # Multiple-choice quiz
│ └── wordle_game.py # Wordle word guessing game
│
├── 📂 test/ # Test files
│ ├── init.py 
│ ├── test_guess_game.py
│ ├── test_rock_paper_scissors.py
│ ├── test_quiz_game.py
│ └── test_wordle.py
│
└── README.md # Project documentation
└── run_test.py
└── LICENSE
└── .gitignore
```

## Installation & Setup

1. **Prerequisites**: Make sure Python 3.6+ is installed
2. **Download**: Clone or download the project folder
3. **Navigate**: Open terminal in the project directory

## How to Run

Run the game hub from the main directory:

```bash
# Navigate to the src directory
cd src

# Run the main program
python main.py
```

## Sample:
```
Video Game Hub
_______________________________________
1- Guess the Number
2- Rock Paper Scissors
3- Quiz Game
4- Wordle
5- Exit
_______________________________________
Your choice:
```
## Game Instructions

#### **Guess the Number**
- Choose from 3 difficulty levels

- Guess the computer's random number

- Get hints if your guess is too high or low

- Limited attempts per level

#### **Rock Paper Scissors**
- Classic hand game against AI

- Choose rock, paper, or scissors

- See immediate results

- Play unlimited rounds

#### **Quiz Game**
- Answer multiple-choice questions

- Test your general knowledge

- See your score at the end

- Try to improve your grade

#### **Wordle**
- Guess a 5-letter word in 6 attempts

- Color-coded feedback for each guess:

  - 🟩 Green: Correct letter, correct position

  - 🟨 Yellow: Correct letter, wrong position

  - ⬜ White: Letter not in the word

- Visual board display with colored letters

- Play multiple rounds with the same word list

## Technologies Used
- Python 3 - Core programming language

- Standard Library - time, sys, random, os modules

- Object-Oriented Design - Classes for each game

- Modular Architecture - Separated game logic

- ANSI Color Codes - Terminal color formatting for Wordle

- Unit Testing - Test cases for each game

## Future Enhancements
Potential improvements for the project:

Add more games (Hangman, Tic-Tac-Toe, etc.)

Implement player score tracking

Add difficulty customization

Create a graphical interface

Add sound effects

Implement multiplayer options

## License
This project is open-source and available for educational purposes.

## Author
Created as a Python learning project to demonstrate modular programming, game development, and user interface design in the terminal.
