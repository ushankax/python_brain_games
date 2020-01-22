import random


# Welcome to the game text:
def welcome():
    print('Answer "yes" if number even otherwise answer "no".\n')


# Function returns tuple with question and right answer:
def question_and_answer():
    num = random.randint(1, 100)

    if num % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'

    question = ('Question: {}'.format(num))

    return question, answer
