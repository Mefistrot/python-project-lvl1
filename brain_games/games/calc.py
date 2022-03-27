from random import randint, choice


DESCRIPTION = 'What is the result of the expression?'


def get_question_and_answer():
    signs = ['+', '-', '*']
    number1 = randint(1, 20)
    number2 = randint(1, 20)
    sign = choice(signs)
    question = str(number1) + ' ' + sign + ' ' + str(number2)
    answer = str(eval(question))
    return question, answer
