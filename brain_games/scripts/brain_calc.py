import prompt
import random
from operator import add, sub, mul
from brain_games.cli import calc_welcome
from brain_games.games_logic import random_exp, answer


def main():
    calc_welcome()

    name = prompt.string('May i have your name: ')
    print('Hello, ' + name + '!')
    print('')  

    i = 1
   

    while i < 5:
        if i == 4:
            print(winner)
            break    
        
        real_answer = random_exp()
        player_answer = answer()
        incorrect_answer = ('{} is wrong answer. Correct answer was {}.'.format(player_answer, real_answer))
        correct_answer = 'Correct!'
        try_again = ("Let's try again, " + name)
        winner = ('Congratulations, ' + name + '!')

        if str(real_answer) == str(player_answer):
            print(correct_answer)
        else:
            print(incorrect_answer)
            print(try_again)
            break

        i += 1
    

if __name__ == '__main__':
    main()
