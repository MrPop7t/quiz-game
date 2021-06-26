import unittest
import termcolor
from Quiz import Quiz
from Question import Question

class TestQuizClass(unittest.TestCase):
    def test_get_categories(self):
        """Test Quiz.get_categories()"""
        categories = Quiz.get_categories()
        self.assertEqual(type(categories), dict)
        self.assertTrue(len(categories.keys()) > 0)
    
    def test_get_questions(self):
        """Test Quiz.get_questions()"""
        questions = Quiz.get_questions(9)
        self.assertEqual(len(questions), 10)

        questions = Quiz.get_questions(-1)
        self.assertEqual(len(questions), 0)

        questions = Quiz.get_questions(category=9, amount=3)
        self.assertEqual(len(questions), 3)
        self.assertTrue(type(questions[0]["incorrect_answers"]) == list)
        self.assertTrue(type(questions[0]["question"]) == str)
        self.assertTrue(type(questions[0]["correct_answer"]) == str)

    def test_decode_questions(self):
        """Test Quiz.decode_questions()"""
        questions = [{
            "question": "Hey &quot;there&quot;",
            "incorrect_answers": ["Hey &quot;there&quot;"],
            "correct_answer": "Hey &quot;there&quot;"
        }]
        Quiz.decode_questions(questions)
        self.assertEqual(questions[0]["question"], 'Hey "there"')
        self.assertEqual(questions[0]["incorrect_answers"][0], 'Hey "there"')
        self.assertEqual(questions[0]["correct_answer"], 'Hey "there"')
    
    def test_quiz(self):
        """Test Quiz()"""
        try:
            quiz = Quiz()
            quiz.questions
            quiz.score
        except Exception as error:
            self.assertTrue(False, error)

    def test_add_raw_questions(self):
        """Test quiz.add_raw_questions()"""
        quiz = Quiz()
        questions = Quiz.get_questions(9)
        quiz.add_raw_questions(questions)
        self.assertEqual(len(quiz.questions), 10)
        self.assertIsInstance(quiz.questions[0], Question)
        self.assertEqual(quiz.questions[0].title, questions[0]["question"])
        self.assertTrue(quiz.questions[0].answer, questions[0]["correct_answer"])