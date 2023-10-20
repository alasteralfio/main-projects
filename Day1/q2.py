# Scrabble Word Point Calculator

letter_points = {
    'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3,
    'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10,
    ' ': 0
}

def pointsCalc(scrabble_input, double_letter, score_multiplier):
    points = 0
    scrabble_input = scrabble_input.upper()
    double_letter = double_letter.upper()
    score_multiplier = score_multiplier.upper()

    if len(scrabble_input) > 1 and len(scrabble_input) < 8 and scrabble_input.isalpha() == False:
        return "Invalid"
    
    for i in scrabble_input:
        points += letter_points[i]

    if double_letter in scrabble_input and double_letter.isalpha():
        points += letter_points[double_letter]

    if score_multiplier == 'D':
        points *= 2
    elif score_multiplier == 'T':
        points *= 3

    return points

scrabble = input('Enter your word: ')
double_letter = input("Letter with double letter score? (Press 'Enter' if none) :")
score_multiplier = input("Double or triple word score? (Press 'd', 't', or 'Enter') : ")

final_points = pointsCalc(scrabble, double_letter, score_multiplier)
print(f"Word score is: {final_points}")