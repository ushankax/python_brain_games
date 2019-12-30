from random import randint
import prompt


def main():
    print('Welcome to the Brain Games!')
    print('Answer "yes" if number even otherwise answer "no".')
    print('')
    name = prompt.string('May i have your name: ')
    print('Hello, ' + name + '!')
    print('')
    correct_answer = 'Correct!'
    incorrect_answer = "'yes' is wrong answer ;(. Correct answer was 'no'."
    try_again = ("Let's try again, " + name)
    winner = ('Congratulations, ' + name + '!')
    i = 1
    x = randint
    result = ''

    while i < 4:
        string = x(1, 100)
        print('Question: ' + str(string))
        answer = prompt.string('Your answer: ')

        if answer == 'yes' and string % 2 == 0:
            print(correct_answer)
        elif answer == 'no' and string % 2 != 0:
            print(correct_answer)
        else: 
            print(incorrect_answer)
            print(try_again)
            break
        i += 1
        if i == 4:
            print(winner)


if __name__ == '__main__':
    main()
