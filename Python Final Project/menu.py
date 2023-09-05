
def mastermind():
    print(r'''
 _      ____  ____  _____  _____ ____  _      _  _      ____ 
/ \__/|/  _ \/ ___\/__ __\/  __//  __\/ \__/|/ \/ \  /|/  _ \
| |\/||| / \||    \  / \  |  \  |  \/|| |\/||| || |\ ||| | \|
| |  ||| |-||\___ |  | |  |  /_ |    /| |  ||| || | \||| |_/|
\_/  \|\_/ \|\____/  \_/  \____\\_/\_\\_/  \|\_/\_/  \|\____/
''')
def menu():
    print(f'-----Welcome to MasterMind!-----')
    print(f'1. Play')
    print(f'2. Rules')
    print(f'3. Settings')
    print(f'4. Exit')
    print(f'--------------------------------')

def rules():
    print()
    print("-------Rules of Mastermind-------")
    print("The computer generates a secret code consisting of a sequence of numbers between 1 and 8.")
    print()
    print("The player makes a guess by entering a sequence of numbers.")
    print()
    print("The computer gives feedback on the player’s guess, indicating how many numbers are\ncorrect and in the correct position, and how many are correct but in the wrong position.")
    print()
    print("The player uses this feedback to make their next guess, and the process repeats\nuntil either the player correctly guesses the code or runs out of turns.")
    print()
    input('Press enter to go back.')
    print('--------------------------------')

def settings_menu(duplicates, length, attempts):
    print("------------Settings------------")
    print(f'1. Allow duplicate numbers: {duplicates}')
    print(f'2. Length of code: {length}')
    print(f'3. Number of attempts: {attempts}')
    print(f'4. Back')
    print('--------------------------------')
