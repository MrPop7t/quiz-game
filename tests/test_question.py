from unittest
import unittest
import termcolor
from Question import Question

class TestQuestionClass(unittest.TestCase):
    def test_init(self):
        """"Test Question()"""
        try:
            question = Question("a", [1,2,3], 3)
            question.title
            question.options
            question.answer

        except Exception as error:
            self.assertTrue(False, error)

    
    def test_is_correct(self):
        """"Test quiz.is_correct()"""
        question = Question("a", [1,2,3], 3)
        self.assertTrue(question.is_correct(3))
        self.assertFalse(question.is_correct(2))
        self.assertFalse(question.is_correct(1))