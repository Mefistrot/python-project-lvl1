from random import randint

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_question_and_answer():
    number1 = randint(1, 30)
    number2 = randint(1, 30)
    divisors1 = set()
    divisors2 = set()
    for i in range(1, number1 + 1):
        if number1 % i == 0:
            divisors1.add(i)
    for i in range(1, number2 + 1):
        if number2 % i == 0:
            divisors2.add(i)
    question = str(number1) + ' ' + str(number2)
    answer = str(max(divisors1 & divisors2))
    return question, answer
