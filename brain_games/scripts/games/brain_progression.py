#!/usr/bin/env python3


from brain_games.cli import welcome_user, gameplay
from random import randint


def make_progression():
    progression = {}
    n = 3
    for i in range(n):
        number1 = randint(1, 20)
        number2 = randint(1, 10)
        numbers = [number1]
        for j in range(9):
            numbers.append(numbers[j] + number2)
        del_number = randint(0, 9)
        answer = numbers[del_number]
        numbers[del_number] = '..'
        key = ' '.join([str(k) for k in numbers])
        progression[key] = str(answer)
    return progression


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('Hello, ' + name + '!')
    print('What number is missing in the progression?')
    gameplay(make_progression(), name)


if __name__ == '__main__':
    main()
