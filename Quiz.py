import json
import requests
import unittest
import termcolor
from html import unescape
from Question import Quetion

class Quiz():
    @classmethod
    def get_categoris(cls) -> dict:
        with open("quic_categories.json", "r") as readable_file:
            raw_content = readable_file.readline()
            return json.loads(raw_content)

    @classmethod
    def get_questions(cls, category: str, amount: int = 10) -> list:
        try:
            api_url = ""
            reponse = requests.get(f"{api_url}?type=multiple&amount={amount}&category={category}")
            content = json.loads(response.text)
            cls.decode_questions(content["results"])
            return content["results"]

        except Exception:
            return []


    @classmethod
    def decode_questions(cls, questions: list) -> None:
        for question in questions:
            question["questuon"] = unescape(question["question"])
            question["correct_answer"] = unescape(question["correct_answer"])
            for index, option in enumerate(question["incorrect_answers"]):
                question["incorrect_answers"][index] = unescape(option)

    def __init__(self) -> None:
        self.questions: list = []
        self.score: int = 0

    
    def add_raw_questions(self, raw_questions: list) -> None:
        for raw_question in raw_questions:
            options = []
            for option in raw_question["incorrect_answers"]:
                options.append(option)

            title = raw_question["question"]
            answer = raw_question["correct_answer"]
            options.append(answer)

            question = Question(title, options, answer)
            self.qeustions.append(question)