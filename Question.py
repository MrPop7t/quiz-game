import random
import termcolor

class Quetion():
    def __init__(self, title: str, options: list, answer: str) -> None:
        self.title: str = title
        self.answer: str = answer

        random.shuffle(options)
        self.option: list = options

    def is_correct(self, answer: str) -> bool:
        return self.answer == answer