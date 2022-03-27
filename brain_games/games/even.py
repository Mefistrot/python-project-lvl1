from random import randint


DESCRIPTION = 'Answer "yes" if number is even, otherwise answer "no".'


def get_question_and_answer():
    question = randint(1, 99)
    if question % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    return str(question), answer
