import random
import prompt


def is_prime():
    n = random.randint(1, 101)
    step = 2
    result = ''
    question = 'Question: {}'.format(n)
    print(question)

    while step <= n:
        if step == n:
            result = 'yes'
            break
        elif n == 1 or n == 2:
            result = 'yes'
            break
        elif n % step != 0:
            step += 1
        else:
            result = 'no'
            break

    return result


def answer():
    real = is_prime()
    guess = prompt.string('Your answer: ')

    return str(real) == str(guess)


def welcome():
    print('')
    print('Welcome to the Brain Games!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    print('')
