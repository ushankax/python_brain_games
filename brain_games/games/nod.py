import prompt
import random

def welcome():
    print('')
    print('Welcome to the Brain Games!')
    print('Find the greatest common divisor of given numbers.')
    print('')


def hello():
    player_name = prompt.string('May i have your name: ')
    print('Hello, ' + player_name + '!')
    print('')
    return player_name


def logic():
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
