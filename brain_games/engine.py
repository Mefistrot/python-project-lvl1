from brain_games.cli import welcome_user
import prompt


def run_game(game):
    name = welcome_user()
    print(game.DESCRIPTION)
    questions = set()
    round_count = 3
    for i in range(round_count):
        question, correct_answer = game.get_question_and_answer()
        while question in questions:
            question, correct_answer = game.get_question_and_answer()
        print('Question: {}'.format(question))
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
            questions.add(question)
        else:
            print('\'{}\' is wrong answer ;(. '
                  'Correct answer was \'{}\'.'.format(answer, correct_answer))
            print('Let\'s try again, {}!'.format(name))
            return
    print('Congratulations, {}!'.format(name))
