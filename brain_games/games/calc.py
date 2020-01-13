import random
import prompt
from operator import add, sub, mul


def welcome():
    print('')
    print('Welcome to the Brain Games!')
    print('What is the result of the expression?')
    print('')


def hello():
    player_name = prompt.string('May i have your name: ')
    print('Hello, ' + player_name + '!')
    print('')
    return player_name


def logic():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    symbol, operation = random.choice((
      ('+', add),
      ('-', sub),
      ('*', mul),
      ))
    result = operation(num1, num2)

    print('Question: {} {} {}'.format(num1, symbol, num2))
    return result


def answer():
    right = logic()
    guess = prompt.string('Your answer: ')
    correct_ans = 'Correct!\n'
    incorrect_text = 'is wrong answer. Correct answer was'
    incorrect_ans = ('{} {} {}.'.format(guess, incorrect_text, right))

    if str(guess) == str(right):
        print(correct_ans)
        return True
    else:
        print(incorrect_ans)
        return False


def main():
    answer()


if __name__ == '__main__':
    main()
