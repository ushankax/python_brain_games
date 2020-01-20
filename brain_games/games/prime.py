import random

# Welcome to the game text:
def welcome():
    print('\nWelcome to the Brain Games!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".\n')

# Function returns tuple with question and right answer:
def question_and_answer():
    num = random.randint(1, 101)
    step = 2
    result = ''
    question = 'Question: {}'.format(num)

    while step <= num:
        if step == num:
            answer = 'yes'
            break
        elif num == 1 or num == 2:
            answer = 'yes'
            break
        elif num % step != 0:
            step += 1
        else:
            answer = 'no'
            break

    result = (question, answer)
    return result
