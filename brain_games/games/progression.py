from random import randint


DESCRIPTION = 'What number is missing in the progression?'


def get_question_and_answer():
    start = randint(1, 50)
    step = randint(1, 20)
    length = 10
    progression = list(range(start, (start + length * step), step))
    hidden_index = randint(0, 9)
    answer = str(progression[hidden_index])
    progression[hidden_index] = '..'
    question = ' '.join([str(k) for k in progression])
    return question, answer
