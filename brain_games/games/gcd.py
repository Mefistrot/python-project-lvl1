from random import randint

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_greatest_common_divisor(num1, num2):
    divisors1 = set()
    divisors2 = set()
    for i in range(1, num1 + 1):
        if num1 % i == 0:
            divisors1.add(i)
    for i in range(1, num2 + 1):
        if num2 % i == 0:
            divisors2.add(i)
    return str(max(divisors1 & divisors2))


def get_question_and_answer():
    number1 = randint(1, 30)
    number2 = randint(1, 30)
    question = str(number1) + ' ' + str(number2)
    answer = get_greatest_common_divisor(number1, number2)
    return question, answer
