import random
import prompt


def welcome():
    print('')
    print('Welcome to the Brain Games!')
    print('Answer "yes" if number even otherwise answer "no".')
    print('')


def hello():
    player_name = prompt.string('May i have your name: ')
    print('Hello, ' + player_name + '!')
    print('')
    return player_name


def logic():
    num = random.randint(1, 100)

    if num % 2 == 0:
      result = 'yes'
    else:
      result = 'no'

    print('Question: {}'.format(num))
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



