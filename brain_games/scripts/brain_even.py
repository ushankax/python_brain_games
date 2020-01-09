#!/usr/bin/env python3

from random import randint
import prompt
from brain_games.games.even_logic import welcome


def game():
    name = prompt.string('May i have your name: ')
    print('Hello, ' + name + '!')
    print('')
    correct_answer = 'Correct!'
    try_again = ("Let's try again, " + name)
    winner = ('Congratulations, ' + name + '!')
    i = 1
    x = randint

    while i < 4:
        string = x(1, 100)
        print('Question: ' + str(string))
        answer = prompt.string('Your answer: ')

        def reverse():
            result = ''

            if answer == 'yes':
                result = "no"
            else:
                result = "yes"
            return result 

        not_answer = reverse()
        inc_text = 'is wrong answer ;(. Correct answer was'
        incorrect = "'{}' {} '{}'".format(answer, inc_text, not_answer)

        if answer == 'yes' and string % 2 == 0:
            print(correct_answer)
        elif answer == 'no' and string % 2 != 0:
            print(correct_answer)
        else:
            print(incorrect)
            print(try_again)
            break
        i += 1
        if i == 4:
            print(winner)


def main():
    welcome()
    game()


if __name__ == '__main__':
    main()
