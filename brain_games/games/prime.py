from random import randint


game_description = '''Answer "yes" if given number is prime. \
Otherwise answer "no".'''
game_data = {}
n = 3
for i in range(n):
    number = randint(1, 100)
    divisors = set()
    for j in range(2, number):
        if number % j == 0:
            divisors.add(j)
    if len(divisors) > 0:
        game_data[str(number)] = 'no'
    else:
        game_data[str(number)] = 'yes'
