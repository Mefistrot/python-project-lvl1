from random import randint


DESCRIPTION = 'What number is missing in the progression?'


def get_question_and_answer():
    start = randint(1, 50)
    step = randint(1, 20)
    length = 10
    progression = list(range(start, (start + length * step), step))
    deleted_number = randint(0, 9)
    answer = str(progression[deleted_number])
    progression[deleted_number] = '..'
    question = ' '.join([str(k) for k in progression])
    return question, answer
