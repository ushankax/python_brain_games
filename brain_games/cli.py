import prompt


def run():
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')


#---Brain-Calculator---#
def calc_welcome():
    print('Welcome to the Brain Games!')
    print('What is the result of the expression?')
    print('')


if __name__ == '__main__':
    run()
