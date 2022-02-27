from random import randint


game_description = 'What number is missing in the progression?'
game_data = {}
n = 3
for i in range(n):
    number1 = randint(1, 20)
    number2 = randint(1, 10)
    numbers = [number1]
    for j in range(9):
        numbers.append(numbers[j] + number2)
    deleted_number = randint(0, 9)
    answer = numbers[deleted_number]
    numbers[deleted_number] = '..'
    key = ' '.join([str(k) for k in numbers])
    game_data[key] = str(answer)
