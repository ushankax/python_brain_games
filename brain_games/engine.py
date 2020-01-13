from brain_games.games import calc, nod, even, progression, prime

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

        if compare == True:
            i += 1
        else:
            print(try_again)
            break

def main():
  game(module)

if __name__ == '__main__':
  main()
