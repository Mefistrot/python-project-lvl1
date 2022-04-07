from random import randint

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_greatest_common_divisor(num1, num2):
    if not num2:
        return num1
    return get_greatest_common_divisor(num2, num1 % num2)


def get_question_and_answer():
    number1 = randint(1, 30)
    number2 = randint(1, 30)
    question = f'{str(number1)} {str(number2)}'
    answer = str(get_greatest_common_divisor(number1, number2))
    return question, answer
