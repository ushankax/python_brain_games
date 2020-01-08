import prompt
import random


def welcome():
    print('Welcome to the Brain Games!')
    print('Find the greatest common divisor of given numbers.')
    print('')


def greatest_div():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    i = min(num1, num2)
    question = ('Question: {} {}'.format(num1, num2))
    print(question)

    while i > 0:
        if num1 % i == 0 and num2 % i == 0:
            return i
            break
        else:
            i -= 1


def answering():
    result = greatest_div()
    guess = prompt.string('Your answer: ')
    return str(result) == str(guess)
