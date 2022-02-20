#!/usr/bin/env python3


from brain_games.cli import welcome_user, gameplay
from random import randint


def make_prime():
    prime = {}
    n = 3
    for i in range(n):
        number = randint(1, 100)
        divisors = set()
        for j in range(2, number):
            if number % j == 0:
                divisors.add(j)
        if len(divisors) > 0:
            prime[str(number)] = 'no'
        else:
            prime[str(number)] = 'yes'
    return prime


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('Hello, ' + name + '!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    gameplay(make_prime(), name)


if __name__ == '__main__':
    main()
