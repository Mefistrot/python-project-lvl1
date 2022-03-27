from random import randint


DESCRIPTION = '''Answer "yes" if given number is prime. \
Otherwise answer "no".'''


def get_question_and_answer():
    question = randint(1, 100)
    divisors = set()
    for i in range(2, question):
        if question % i == 0:
            divisors.add(i)
    if len(divisors) > 0:
        answer = 'no'
    else:
        answer = 'yes'
    return str(question), answer
