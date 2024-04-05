import random
import json
import time
from menu import *

# Read JSON file
def get_settings():
    global length, duplicates, attempts
    with open("settings.json", "r") as f:
        # Load the JSON data from the file and store it in a variable
        settings = json.load(f)

    length = settings["length"]
    duplicates = settings["duplicates"]
    attempts = settings["attempts"]

# Board generation
def generate_board():
    if duplicates == 'true':
        return [random.randint(1, 8) for i in range(length)]
    else: 
        return random.sample(range(1, 9), length)

# Guess input
def get_guess():
    while True:
        guess = input(f"Enter your guess ({length} numbers): ")
        if len(guess) != length:
            print(f"Invalid guess. Please enter {length} numbers.")
        else:
            return [int(num) for num in guess]

# Check for black and white pegs
def check_guess(board, guess):
    black = sum(1 for i in range(length) if guess[i] == board[i])
    white = sum(1 for i in range(length) if guess[i] in board) - black
    return black, white

def main():
    global length, duplicates, attempts
    get_settings()
    while True:
        mastermind()
        menu()
        choice = input('Enter your choice: ')
        print()

        if choice == "1":
            # Play the game
            board = generate_board()
            #print(board)
            print(f'Welcome to MasterMind:')
            print(f'Guess the board within {attempts} tries.')

            for attempt in range(1, attempts + 1):
                print(f'\nAttempt {attempt}')
                guess = get_guess()
                black, white = check_guess(board, guess)

                if black == length:
                    print(f'You guessed the board!')
                    break
                else:
                    print(f'Black: {black}, White: {white}')
            print('\nThe hidden board was:', board)
            print()
            break

        elif choice == "2":
            # Display the rules
            rules()

        elif choice == "3":
            # Display the settings
            while True:
                with open("settings.json", "r") as f:
                    data = json.load(f)

                settings_menu(duplicates, length, attempts)
                choice = input('Enter your choice: ')
                print()
                if choice == "1":
                    # Get the user's input
                    duplicates_input = input('Allow duplicates (T/F)? ')
                    if duplicates_input.upper() == "T":
                        duplicates = 'true'
                    elif duplicates_input.upper() == "F":
                        duplicates = 'false'
                    else:
                        print("Invalid choice. Please try again.")
                        print()
                        time.sleep(1)
                        continue 

                    data["duplicates"] = duplicates
                    print('Successfully updated settings.')
                    print()
                    time.sleep(1)

                elif choice == "2":
                    # Get the user's input
                    length_input = int(input('Enter the length of code: '))
                    if length_input > 0 and length_input <= 8:
                        length = length_input
                        data["length"] = length
                        print('Successfully updated settings.')
                        print()
                        time.sleep(1)
                        with open("settings.json", "w") as f:
                            json.dump(data, f)  
                    else:
                        print('Go easy on yourself! Keep the length between 1 and 8.')
                        print()
                        time.sleep(1)

                elif choice == "3":
                    # Get the user's input
                    attempts_input = int(input('Enter the number of attempts: '))
                    if attempts_input > 0 and attempts_input <= 99:
                        attempts = attempts_input
                        data["attempts"] = attempts
                        print('Successfully updated settings.')
                        print()
                        time.sleep(1)
                        with open("settings.json", "w") as f:
                            json.dump(data, f)
                    else:
                        print("Sorry, that's too many attempts! Keep it under 99.")
                        print()
                        time.sleep(1)

                elif choice == "4":
                    break  # Exit the settings 

        elif choice == "4":
            # Exit the game
            break
        else:
            # Invalid choice
            print("Invalid choice. Please try again.")

main()
