                                       
import random
while True:
    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")
    choice = int(input("Enter your choice :"))
    while choice > 3 or choice < 1:
        choice = int(input('Enter a valid choice please '))
    if choice == 1:
        choicename = 'Rock'
    elif choice == 2:
        choicename = 'Paper'
    else:
        choicename = 'Scissors'
    print('User choice is \n', choicename)
    compchoice = random.randint(1, 3)
    while compchoice == choice:
        compchoice = random.randint(1, 3)
    if compchoice == 1:
        compchoicename = 'RocK'
    elif compchoice == 2:
        compchoicename = 'Paper'
    else:
        compchoicename = 'Scissors'
    print("Computer choice is \n", compchoicename)
    print(choicename, 'Vs', compchoicename)
    
    if choice == compchoice:
        print('Its a Draw', end="")
        result = "Draw"
    if (choice == 1 and compchoice == 2):
        print('paper wins', end="")
        result = 'Paper'
    elif (choice == 2 and compchoice == 1):
        print('paper wins', end="")
        result = 'Paper'       
    if (choice == 1 and compchoice == 3):
        print('Rock wins ', end="")
        result = 'Rock'
    elif (choice == 3 and compchoice == 1):
        print('Rock wins ', end="")
        result = 'RocK'
    if (choice == 2 and compchoice == 3):
        print('Scissors wins ', end="")
        result = 'Scissors'
    elif (choice == 3 and compchoice == 2):
        print('Scissors wins ', end="")
        result = 'Scissors'
    if result == 'DRAW':
        print(" Its a tie ")
    if result == choicename:
        print(" User wins ")
    else:
        print("Computer wins ")
    break


