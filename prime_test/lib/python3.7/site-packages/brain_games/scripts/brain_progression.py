import prompt
from brain_games.games.progression_game_logic import welcome_progression, show_progression, is_number


def game():
  name = prompt.string('May i have your name: ')
  print('Hello, ' + name)
  print('')
  incorrect = ('Wrong answer. Try again, ' + name)
  correct_answer = ('Correct!')
  winner = ('Congratulations, ' + name + '!')
  a = 1

  while a <= 4:
    if a == 4:
      print(winner)
      break

    correct = is_number()

    if correct:
      print(correct_answer)
      print('')
    else:
      print(incorrect)
      print('')
      break

    a += 1


def main():
    welcome_progression()
    game()


if __name__ == '__main__':
    main()
