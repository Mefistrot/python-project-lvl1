#!/usr/bin/env python3


from brain_games.cli import welcome_user
from random import randint


def make_question_answer():
    question_answer = {}
    n = 3
    for i in range(n):
        number = randint(1, 99)
        while number in question_answer:
            number = randint(1, 99)
        if number % 2 == 0:
            question_answer[number] = 'yes'
        else:
            question_answer[number] = 'no'
    return question_answer


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('Hello, ' + name + '!')
    print('Answer "yes" if number is even, otherwise answer "no".')
    question_answer = make_question_answer()
    answer_count = 0
    for key in question_answer:
        print('Question: ' + str(key))
        answer = input()
        if answer == question_answer[key]:
            print('Correct!')
            answer_count += 1
        else:
            print('\'' + answer + '\' is wrong answer ;(.'
                  'Correct answer was \'' + question_answer[key] + '\'.')
            print('Let\'s try again, ' + name + '!')
            break
    if answer_count == len(question_answer):
        print('Congratulations, ' + name + '!')


if __name__ == '__main__':
    main()
