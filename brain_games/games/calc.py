from random import randint, choice
import operator


DESCRIPTION = 'What is the result of the expression?'


def get_question_and_answer():
    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
    }
    number1 = randint(1, 20)
    number2 = randint(1, 20)
    operation = choice(list(operations.keys()))
    question = f'{str(number1)} {operation} {str(number2)}'
    answer = str(operations[operation](number1, number2))
    return question, answer
