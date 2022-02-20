#!/usr/bin/env python3


from brain_games.cli import welcome_user, gameplay
from random import randint


def make_gcd():
    gcd = {}
    n = 3
    for i in range(n):
        number1 = randint(1, 30)
        number2 = randint(1, 30)
        divisors1 = set()
        divisors2 = set()
        for j in range(1, number1 + 1):
            if number1 % j == 0:
                divisors1.add(j)
        for j in range(1, number2 + 1):
            if number2 % j == 0:
                divisors2.add(j)
        key = str(number1) + ' ' + str(number2)
        gcd[key] = str(max(divisors1 & divisors2))
    return gcd


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('Hello, ' + name + '!')
    print('Find the greatest common divisor of given numbers.')
    gameplay(make_gcd(), name)


if __name__ == '__main__':
    main()
