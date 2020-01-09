from brain_games.games.nod_game_logic import welcome, answer
import prompt


def game():
    name = prompt.string('May i have your name: ')
    print('Hello, ' + name)
    incorrect = ('Wrong answer. Try again, ' + name)
    correct_answer = ('Correct!')
    winner = ('Congratulations, ' + name + '!')
    a = 1

    while a <= 4:
        if a == 4:
            print(winner)
            break

        correct = answer()

        if correct:
            print(correct_answer)
        else:
            print(incorrect)
            break
        a += 1


def main():
    welcome()
    game()


if __name__ == '__main__':
    main()
