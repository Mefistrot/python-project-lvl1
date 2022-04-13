from random import randint


DESCRIPTION = \
    'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number == 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    else:
        return True


def get_question_and_answer():
    question = randint(1, 100)
    answer = 'yes' if is_prime(question) else 'no'
    return str(question), answer
