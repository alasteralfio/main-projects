# Football Teams

teamDict = {}

values = ['Total Games', 'Games Won', 'Games Lost', 'Games Drawn', 'Points']

def addTeam(teamName):
    teamDict[teamName] = [0, 0, 0, 0, 0]
    print(f'{teamName} has been added.')
    print()

def addResult(TeamName, Result):
    if TeamName in teamDict:
        for i in range(len(values)):
            teamDict[TeamName][i] += Result[i]
        print(f'Results for {TeamName} have been added.')
        print()
    else:
        print('Team not found.')

def printResult():
    print(f'{"Team":<15} {"Played":<7} {"Won":<7} {"Lost":<7} {"Drawn":<7} {"Points":<7}')
    print('---------------------------------------------------------------------------')
    for team in teamDict:
        print(f'{team:<15} {teamDict[team][0]:<7} {teamDict[team][1]:<7} {teamDict[team][2]:<7} {teamDict[team][3]:<7} {teamDict[team][4]:<7}')
    print('---------------------------------------------------------------------------')

def printTeam(team):
    print(f'{"Team":<15} {"Played":<7} {"Won":<7} {"Lost":<7} {"Drawn":<7} {"Points":<7}')
    print('---------------------------------------------------------------------------')
    print(f'{team:<15} {teamDict[team][0]:<7} {teamDict[team][1]:<7} {teamDict[team][2]:<7} {teamDict[team][3]:<7} {teamDict[team][4]:<7}')
    print('---------------------------------------------------------------------------')

def menu():
    print("1. Add Team")
    print("2. Add Result")
    print("3. Print All Results")
    print("4. Search Team")
    print("5. Exit")
    print()

def main():
    while True:
        menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            team_add = input('Enter team name: ')
            addTeam(team_add)

        if choice == "2":
            team = input('Enter team name: ')
            result = []
            for i in values:
                number = int(input(f'Enter {i}: '))
                result.append(number)
            addResult(team, result)

        if choice == '3':
            printResult()

        if choice == '4':
            team = input('Enter team name: ')
            printTeam(team)

        if choice == '5':
            printResult()
            break

main()
