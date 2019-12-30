#!/usr/bin/env python

import prompt
from random import randomint

def is_even():
    i = 1
    name = prompt.string('May i have your name? ')
    print('Hello, ' + name + '!')

    name_exclanation = (name + '!')

    while i < 5 or result != 'Correct!':
        number = random.randint(1, 100)
        correct_answer = 'Correct!'
        incorrect_answer = "'yes' is wrong answer ;(. Correct answer was 'no'. Let's try again, "
        winner = ('Congratulations, ' + name_exclanation)
        
        print('Question: ' + number)
        answer = prompt.string('Your answer: ')

        if i == 4:
            print(winner)
            break
        elif number % 2 == 0 and answer == 'yes':
            print(correct_answer)            
        elif number % 2 != 0 and answer == 'no':
            print(correct_answer)
        else:
            print(incorrect_answer + name_exclanation)       
        i += 1

if __name__ == '__main__':
    is_even()
