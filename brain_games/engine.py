import prompt


def run_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.DESCRIPTION)
    rounds_count = 3
    for i in range(rounds_count):
        question, correct_answer = game.get_question_and_answer()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer != correct_answer:
            print(f'\'{answer}\' is wrong answer ;(. '
                  f'Correct answer was \'{correct_answer}\'.')
            print('Let\'s try again, {}!'.format(name))
            return
        print('Correct!')
    print(f'Congratulations, {name}!')
