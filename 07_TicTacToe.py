import random

def update_board(n,symbol):
    l[n-1] = symbol
    list_of_remaining_nos.remove(n)  
    print(l)
    return None

def check_win():
    pass

def show_board():
    for i in [0,3,6]:
        print(f'|{l[i]}|{l[i+1]}|{l[i+2]}|')
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

for i in range(5):
    num = int(input("Enter a number: "))
    update_board(num,'X')
    check_win()
    computer_plays()
    check_win()
    print(list_of_remaining_nos)
    show_board()