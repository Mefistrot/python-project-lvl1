#!/usr/bin/env python3


from brain_games.cli import welcome_user, gameplay
from random import randint


def make_question_answer():
    question_answer = {}
    n = 3
    for i in range(n):
        number = str(randint(1, 99))
        while number in question_answer:
            number = str(randint(1, 99))
        if int(number) % 2 == 0:
            question_answer[number] = 'yes'
        else:
            question_answer[number] = 'no'
    return question_answer


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('Hello, ' + name + '!')
    print('Answer "yes" if number is even, otherwise answer "no".')
    gameplay(make_question_answer(), name)


if __name__ == '__main__':
    main()
