
import termcolor
from termcolor import cprint
import inquirer # type: ignore
from Quiz import Quiz

quiz = Quiz()
categories = Quiz.get_categories()
main_color = "blue"

cprint("Welcome to Quiz! The worlds best terminal quiz game", main_color)
cprint("Please select your quiz category")

questions = [
    inquirer.List(
        'category',
        message="Which category would you like?",
        choices=categories.keys(),
    )
]

category_name = inquirer.prompt(questions)["category"]

cprint(f"Awesome you have selected {category_name} as your category!", main_color)
cprint("Please wait while we build your quiz...", main_color)

raw_questions = Quiz.get_questions(categories[category_name])

if len(raw_questions) == 0:
    cprint("Sorry but we couldnt finy any questions to build your quiz", main_color)
    exit()

quiz.add_raw_questions(raw_questions)

for quiz_question in quiz.questions:
    question = [
        inquirer.List(
            "answer",
                message=quiz_question.title,
                choices=quiz_question.options,
        )
    ]

    answer = inquirer.prompt(question)["answer"]

    if quiz_question.is_correct(answer):
        cprint("Correct", "green")
        quiz.score += 1
    else:
        cprint("Sorry that wasn't right", main_color)

cprint("That's the end of the quiz", main_color)
cprint(f"You scored a {quiz.score} out of {len(quiz.questions)}")