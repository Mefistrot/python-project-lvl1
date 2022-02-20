import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    return name


def gameplay(data, name):
    answer_count = 0
    for key in data:
        print('Question: ' + key)
        answer = input()
        print('Your answer: ' + answer)
        if answer == data[key]:
            print('Correct!')
            answer_count += 1
        else:
            print('\'' + answer + '\' is wrong answer ;(.'
                  'Correct answer was \'' + data[key] + '\'.')
            print('Let\'s try again, ' + name + '!')
            break
    if answer_count == len(data):
        print('Congratulations, ' + name + '!')
