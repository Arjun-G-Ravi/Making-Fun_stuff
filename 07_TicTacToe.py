'''
BUG
Typing wrong char, updates over existing ones.

'''

import random

def update_board(n,symbol):
    l[n-1] = symbol
    list_of_remaining_nos.remove(n)  
    # print(l)
    return None

def check_win():
    global game

    win1 = [[3*i+1,3*i+1+1,3*i+2+1] for i in range(0,3)]
    win2 = [[i+1,i+3+1,i+6+1] for i in range(0,3)]
    win3 = [[1,5,9],[3,5,7]]
    win_list = win1+win2+win3
    for win_trio in win_list:
        flagX,flagO=0,0
        for num in win_trio:
            if num in X:
                flagX += 1
        if flagX == 3:
            print("\n\n--------GAME OVER--------")
            print("You won the game")
            game = 'Over'
            break

        for num in win_trio:
            if num in O:
                flagO += 1
        if flagO == 3:
            print("\n\n--------GAME OVER--------")
            print("The computer won the game")
            game = 'Over'
            break


def show_board():
    for i in [0,3,6]:
        print(f'    |{l[i]}|{l[i+1]}|{l[i+2]}|')
    return None

def computer_plays():
    rand_num = random.choice(list_of_remaining_nos) 
    update_board(rand_num,"O")
    O.append(rand_num)
    return None

X = []
O = []
l =[" " for i in range(9)]
list_of_remaining_nos = [i+1 for i in range(9)]       # Contains numbers left
print('''This shows the number's location:-
    | 1 | 2 | 3 |
    | 4 | 5 | 6 |
    | 7 | 8 | 9 |\n''')
global game
game = 'Start'
while True:
    num = int(input("\nEnter a number: "))
    try:
        update_board(num,'X')
        X.append(num)
    except Exception:
        print("Invalid move. Try again\n")
        continue
    check_win()
    if game == 'Over':
        break
    try:
        computer_plays()
    except Exception:
        show_board()
        print("\n\n--------GAME OVER--------")
        print("It is a draw.")
        game = 'Over'
        
    check_win()
    if game == 'Over':
        break

    # print(list_of_remaining_nos)
    show_board()
    # print("Game=",game)
    # print(X,O)
print()
show_board()
