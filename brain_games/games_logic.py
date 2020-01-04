import random
import prompt
from operator import add, sub, mul


def random_exp():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    symbol, operation = random.choice((
      ('+', add),
      ('-', sub),
      ('*', mul),
      ))
    result = operation(num1, num2)
    i = 1

    print('Question: {} {} {}'.format(num1, symbol, num2))
    return result

def answer():
    answer = prompt.string('Your answer: ')

    return answer
