import prompt
from brain_games.games.calc_logic import random_exp, answer, welcome


def game():
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


def main():
    welcome()
    game()


if __name__ == '__main__':
    main()
