import random


PROG_LENGTH = 10


def welcome():
    print('What number is missing in the progression?\n')


def question_and_answer():
    num = random.randint(1, 10)
    step = random.randint(1, 10)
    empty_place = random.randint(1, 10)
    empty_place_number = num + empty_place * step
    counter = 1
    full_progression = ''

    while counter <= PROG_LENGTH:
        progression = num + counter * step

        if full_progression:
            full_progression += ' '

        if empty_place == counter:
            full_progression += '..'
        else:
            full_progression += str(progression)

        counter += 1

    question = 'Question: {}'.format(full_progression)

    return question, str(empty_place_number)
