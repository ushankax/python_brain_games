import random


# Welcome to the game text:
def welcome():
    print('Find the greatest common divisor of given numbers.\n')


# Function returns tuple with question and right answer:
def question_and_answer():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    greatest_div = min(num1, num2)
    question = ('Question: {} {}'.format(num1, num2))

    while greatest_div > 0:
        if num1 % greatest_div == 0 and num2 % greatest_div == 0:
            return question, str(greatest_div)
        else:
            greatest_div -= 1
