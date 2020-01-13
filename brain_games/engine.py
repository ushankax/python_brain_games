def run(module):
    module.welcome()
    name = module.hello()
    winner = ('Congratulations, ' + name + '!')
    try_again = ("Let's try again, " + name)
    i = 1

    while i < 5:
        if i == 4:
            print(winner)
            break

        compare = module.answer()

        if compare is True:
            i += 1
        else:
            print(try_again)
            break


def main():
    run()


if __name__ == '__main__':
    main()
