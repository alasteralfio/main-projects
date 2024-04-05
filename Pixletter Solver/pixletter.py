from english_words import get_english_words_set
from grids import letter_grids, pixletter_text

web2lowerset = list(get_english_words_set(['web2'], lower=True))
alphabet_list = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

def scan_letters(row, pixels):
    pixel_list1 = [1 if x == 2 else x for x in pixels]
    pixel_list2 = [0 if x == 2 else x for x in pixels]
    output_list = []
    for alphabet in alphabet_list:
        scan = letter_grids[alphabet][row]
        if scan == pixel_list1:
            output_list.append(alphabet)
        if scan == pixel_list2:
            output_list.append(alphabet)
    return output_list

def scan_word(char_list):
    output_list = []
    word_list = [word for word in web2lowerset if len(word) == len(char_list)]
    for word in word_list:
        for position, chars in enumerate(char_list):
        # Check if the character at the current position in the word matches any of the characters in the char_list
            if word[position].upper() not in chars:
                break
        else:
            # If all characters match, print the word
            output_list.append(word)
    return output_list

def main_scan():
    try:
        character_list = []
        row_number = 0
        while row_number < 7: # Repeat til no more rows
            pixel_input = input(f"Enter pixels for row {row_number + 1}: ").split(',')
            if pixel_input == ['']:
                print('Uh oh, maybe an error occured. Returning to menu!')
                menu()
                return
            for length in range(len(pixel_input)):
                pixels = [int(pixel) for pixel in pixel_input[length].strip()] # E.g. 10001, 01010, 10101
                pixel_scan = scan_letters(row_number, pixels)
                if row_number == 0: # Checks for existing elements
                    character_list.append(pixel_scan)
                else:
                    compare_list = character_list[length]
                    character_list[length] = list(set(compare_list).intersection(pixel_scan))
            row_number += 1
            possible = scan_word(character_list)
            print('Possible words: ')
            for word in range(len(possible)):
                if word == len(possible) - 1:
                    print(possible[word])
                else:
                    print(possible[word], end=', ')
    except:
        print('Uh oh, maybe an error occured. Returning to menu!')
        menu()

def menu():
    choice = 0
    while choice != 3:
        print("===============")
        print("1. Get Started")
        print("2. Help")
        print("3. Quit")
        choice = input("...")

        if choice == "1":
            print("===============")
            main_scan()

        elif choice == "2":
            print("===============")
            print("""To use this program, enter the row of pixels, where Green is 1, Red is 0 and Blanks are 2. 
For example, our first guess is DOG. After Pixletters has scanned the row, we enter it's output, 
10002, 21112, 21112. You may enter nothing if you wish to exit the program at any time.""")

        elif choice == "3":
            print("===============")
            quit()

print(pixletter_text)
menu()