#!/usr/bin/env python3


from brain_games.cli import welcome_user


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('Hello, ' + name + '!')
    print('Answer "yes" if number is even, otherwise answer "no".')
    question_answer = {15 : 'no', 6 : 'yes', 7 : 'no'}
    answer_count = 0
    for key in question_answer:
        print('Question: ' + str(key))
        answer = input()
        if answer == question_answer[key]:
            print('Correct!')
            answer_count += 1
        else:
            print('\'' + answer + '\' is wrong answer ;(. Correct answer was \'' + question_answer[key] + '\'.')
            print('Let\'s try again, ' + name + '!')
            break
    if answer_count == len(question_answer):
        print('Congratulations, ' + name + '!')

if __name__ == '__main__':
    main()
