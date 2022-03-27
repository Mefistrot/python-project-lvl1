from random import randint


DESCRIPTION = 'What number is missing in the progression?'


def get_question_and_answer():
    number1 = randint(1, 20)
    number2 = randint(1, 10)
    numbers = [number1]
    for i in range(9):
        numbers.append(numbers[i] + number2)
    deleted_number = randint(0, 9)
    answer = str(numbers[deleted_number])
    numbers[deleted_number] = '..'
    question = ' '.join([str(k) for k in numbers])
    return question, answer
