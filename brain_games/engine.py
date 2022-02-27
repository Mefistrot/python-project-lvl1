from brain_games.cli import welcome_user


def run_game(game_description, game_data):
    name = welcome_user()
    print(game_description)
    answer_count = 0
    for key in game_data:
        print('Question: ' + key)
        answer = input()
        print('Your answer: ' + answer)
        if answer == game_data[key]:
            print('Correct!')
            answer_count += 1
        else:
            print('\'' + answer + '\' is wrong answer ;(. '
                  'Correct answer was \'' + game_data[key] + '\'.')
            print('Let\'s try again, ' + name + '!')
            break
    if answer_count == len(game_data):
        print('Congratulations, ' + name + '!')
