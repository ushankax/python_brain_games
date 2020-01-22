import prompt


LVL_NUMBERS = 3


def run(module):
    # Welcome to the game text:
    print('\nWelcome to the Brain Games!')
    module.welcome()

    # Asking name and printing the greet:
    name = prompt.string('May i have your name: ')
    print('Hello, {}!\n'.format(name))

    # Template for incorrect text:
    incorrect_text = 'is wrong answer. Correct answer was'

    # Generating 3 answers to win. Game stops if answer is incorrect:
    for lvl_counter in range(LVL_NUMBERS):
        # Unpacking tuple with question and right answer from logic file
        que_and_right = module.question_and_answer()
        (question, right) = que_and_right

        # Asking the question and taking player's answer:
        print(question)
        guess = prompt.string('Your answer: ')

        # Condition compares player's answer and right result and print result:
        if guess == right:
            print('Correct!\n')
        else:
            print('\n{} {} {}.'.format(guess, incorrect_text, right))
            print("Let's try again, {}.".format(name))
            break
    else:
        print('Congratulations, {}!\n'.format(name))
