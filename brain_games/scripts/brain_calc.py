import prompt
from brain_games.cli import calc_welcome
from brain_games.games.games_logic import random_exp, answer


def main():
    calc_welcome()
    name = prompt.string('May i have your name: ')
    print('Hello, ' + name + '!')
    print('')
    i = 1
    winner = ('Congratulations, ' + name + '!')

    while i < 5:
        if i == 4:
            print(winner)
            break

        right = random_exp()
        guess = answer()
        incorrect_text = 'is wrong answer. Correct answer was'
        incorrect = ('{} {} {}.'.format(guess, incorrect_text, right))
        correct = 'Correct!'
        try_again = ("Let's try again, " + name)

        if str(right) == str(guess):
            print(correct)
        else:
            print(incorrect)
            print(try_again)
            break

        i += 1


if __name__ == '__main__':
    main()
