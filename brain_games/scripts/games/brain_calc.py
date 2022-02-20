#!/usr/bin/env python3


from brain_games.cli import welcome_user, gameplay
from random import randint


def make_expressions():
    expressions = {}
    signs = {'+', '-', '*'}
    for i in range(len(signs)):
        number1 = str(randint(1, 20))
        number2 = str(randint(1, 20))
        sign = signs.pop()
        key = number1 + ' ' + sign + ' ' + number2
        expressions[key] = str(eval(number1 + sign + number2))
    return expressions


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('Hello, ' + name + '!')
    print('What is the result of the expression?')
    gameplay(make_expressions(), name)


if __name__ == '__main__':
    main()
