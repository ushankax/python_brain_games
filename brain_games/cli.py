import prompt


def run():
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name)


if __name__ == '__main__':
    run()
