from random import randint


DESCRIPTION = 'Answer "yes" if number is even, otherwise answer "no".'


def get_question_and_answer():
    question = randint(1, 99)
    answer = 'no' if question % 2 else 'yes'
    return str(question), answer
