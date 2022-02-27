from random import randint


game_description = 'Answer "yes" if number is even, otherwise answer "no".'
game_data = {}
n = 3
for i in range(n):
    number = str(randint(1, 99))
    while number in game_data:
        number = str(randint(1, 99))
    if int(number) % 2 == 0:
        game_data[number] = 'yes'
    else:
        game_data[number] = 'no'
