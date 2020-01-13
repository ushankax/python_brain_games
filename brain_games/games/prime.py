import random
import prompt


def welcome():
    print('')
    print('Welcome to the Brain Games!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    print('')


def hello():
    player_name = prompt.string('May i have your name: ')
    print('Hello, ' + player_name + '!')
    print('')
    return player_name


def logic():
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
