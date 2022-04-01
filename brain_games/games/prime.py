from random import randint


DESCRIPTION = '''Answer "yes" if given number is prime. \
Otherwise answer "no".'''


def is_prime(number):
    divisors = set()
    for i in range(2, number):
        if number % i == 0:
            divisors.add(i)
    return False if len(divisors) > 0 else True


def get_question_and_answer():
    question = randint(1, 100)
    answer = 'yes' if is_prime(question) else 'no'
    return str(question), answer
