import prompt
import random


def show_progression():
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


def is_number():
  real = show_progression()
  answer = prompt.string('Your answer: ')
  return str(answer) == str(real)


def welcome_progression():
    print('Welcome to the Brain Games!')
    print('What number is missing in the progression?')
