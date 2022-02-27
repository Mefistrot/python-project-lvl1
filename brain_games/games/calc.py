from random import randint


game_description = 'What is the result of the expression?'
game_data = {}
signs = {'+', '-', '*'}
for i in range(len(signs)):
    number1 = str(randint(1, 20))
    number2 = str(randint(1, 20))
    sign = signs.pop()
    key = number1 + ' ' + sign + ' ' + number2
    game_data[key] = str(eval(number1 + sign + number2))
