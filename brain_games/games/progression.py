import random
import prompt

def welcome():
    print('')
    print('Welcome to the Brain Games!')
    print('What number is missing in the progression?')
    print('')


def hello():
    player_name = prompt.string('May i have your name: ')
    print('Hello, ' + player_name + '!')
    print('')
    return player_name


def logic():
    number = random.randint(1, 100)
    n = 10
    step = random.randint(1, 10)
    i = 1
    empty_place = random.randint(1, 10)
    empty_place_number = number + empty_place * step
    result = ''

    while i <= n:
        progression = number + i * step

        if result:
            result += ' '

        if empty_place == i:
            result += '..'
        else:
            result += str(progression)

        i += 1

    question = 'Question: {}'.format(result)
    print(question)
    return empty_place_number


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
