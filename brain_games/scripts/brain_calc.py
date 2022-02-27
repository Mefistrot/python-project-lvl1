#!/usr/bin/env python3


from brain_games.engine import run_game
from brain_games.games.calc import game_description, game_data


def main():
    run_game(game_description, game_data)


if __name__ == '__main__':
    main()
