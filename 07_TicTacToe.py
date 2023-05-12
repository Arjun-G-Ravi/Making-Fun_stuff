import random

def update_board(n,symbol):
    l[n-1] = symbol
    list_of_remaining_nos.remove(n)  
    # print(l)
    return None

def check_win():
    pass

def show_board():
    for i in [0,3,6]:
        print(f'    |{l[i]}|{l[i+1]}|{l[i+2]}|')
    return None

def computer_plays():
    rand_num = random.choice(list_of_remaining_nos) 
    update_board(rand_num,"O")
    return None

l =[" " for i in range(9)]
list_of_remaining_nos = [i+1 for i in range(9)]       # Contains numbers left
print('''This shows the number's location:-
    | 1 | 2 | 3 |
    | 4 | 5 | 6 |
    | 7 | 8 | 9 |\n''')

while True:
    num = int(input("\nEnter a number: "))
    try:
        update_board(num,'X')
    except Exception:
        print("Invalid move. Try again\n")
        continue
    check_win()
    try:
        computer_plays()
    except Exception:
        show_board()
        print("--------GAME OVER--------")
        print("It is a draw.")
        break
    check_win()
    
    # print(list_of_remaining_nos)
    show_board()