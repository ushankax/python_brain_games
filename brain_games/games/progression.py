import random


def welcome():
    print('\nWelcome to the Brain Games!')
    print('What number is missing in the progression?\n')


def question_and_answer():
    num = random.randint(1, 100)
    prog_length = 10
    step = random.randint(1, 10)
    counter = 1
    empty_place = random.randint(1, 10)
    empty_place_number = num + empty_place * step
    full_progression = ''

    while counter <= prog_length:
        progression = num + counter * step

        if full_progression:
            full_progression += ' '

        if empty_place == counter:
            full_progression += '..'
        else:
            full_progression += str(progression)

        counter += 1

    question = 'Question: {}'.format(full_progression)
    result = (question, str(empty_place_number))
    return result
