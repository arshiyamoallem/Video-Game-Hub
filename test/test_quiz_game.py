import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import unittest
from games.quiz_game import QuizGame

class TestQuizGame(unittest.TestCase):
    
    def setUp(self):
        self.game = QuizGame()

    def tearDown(self):
        return super().tearDown()
    
    def test_init(self):
        self.assertEqual(len(self.game.questions), 5)
        self.assertEqual(len(self.game.answers), 5)
        self.assertEqual(len(self.game.options), 5)
    
    def test_question_1(self):
        self.assertEqual(self.game.questions[0], "How many wheels does a car have: ")
        self.assertEqual(self.game.answers[0], "C")
        self.assertEqual(self.game.options[0], ("A. 2 ", "B. 8", "C. 4", "D. 6"))

    def test_question_2(self):
        self.assertEqual(self.game.questions[1], "How many meters are in a kilometer: ")
        self.assertEqual(self.game.answers[1], "D")
        self.assertEqual(self.game.options[1], ("A. 100", "B. 10", "C. 10000", "D. 1000"))

    def test_question_3(self):
        self.assertEqual(self.game.questions[2], "How many centimeters are in a meter: ")
        self.assertEqual(self.game.answers[2], "A")
        self.assertEqual(self.game.options[2], ("A. 100", "B. 10", "C. 10000", "D. 1000"))

    def test_question_4(self):
        self.assertEqual(self.game.questions[3], "How many zeros are in a million: ")
        self.assertEqual(self.game.answers[3], "C")
        self.assertEqual(self.game.options[3], ("A. 7", "B. 8", "C. 6", "D. 5"))

    def test_question_5(self):
        self.assertEqual(self.game.questions[4], "Which planet is the most similar to that of earth in this galaxy: ")
        self.assertEqual(self.game.answers[4], "B")
        self.assertEqual(self.game.options[4], ("A. None", "B. Mars", "C. Saturn", "D. Mercury"))

if __name__ == '__main__':
    unittest.main()