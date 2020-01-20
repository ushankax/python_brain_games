import prompt


def run(module):
    # Welcome to the game text:
    module.welcome()

    # Asking name and printing the greet:
    name = prompt.string('May i have your name: ')
    print('Hello, {}!\n'.format(name))

    LVL_NUMBERS = 3

    # Generating 3 answers to win. Game stops if answer is incorrect:
    for lvl_counter in range(LVL_NUMBERS):
        # Unpacking tuple with question and right answer from logic file
        que_and_right = module.question_and_answer()
        (question, right) = que_and_right

        # Asking the question and taking player's answer:
        print(question)
        guess = prompt.string('Your answer: ')

        # Text templates of correct and incorrect answers:
        try_again = 'Let’s try again, {}.'.format(name)
        incorrect_text = 'is wrong answer. Correct answer was'
        incorrect = '\n{} {} {}.'.format(guess, incorrect_text, right)
        correct = 'Correct!\n'

        # Condition compares player's answer and right result and print result:
        if guess == right:
            print(correct)
        else:
            print(incorrect)
            print(try_again)
            break
    else:
        print('Congratulations, {}!\n'.format(name))


def main():
    run()


if __name__ == '__main__':
    main()
