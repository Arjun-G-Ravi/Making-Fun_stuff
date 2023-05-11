from WordsForHangman import words
import random
import string


num_turns = 5

alphabets = list(string.ascii_uppercase)
alphabets_user = []
correct_alph = []
word = random.choice(words).upper()
w = '-' * len(word)


def get_char(a):
    if not a.isalpha():
        print("Not an alphabet")
        return None
    a = a[0].upper()
    if a in alphabets_user:
        print('Alphabet already chosen')
        return None
    else:
        alphabets_user.append(a)    
        alphabets.remove(a)
        return a 
         
i = 0
print("\nLETS PLAY HANGMAN ...")
print("TRY TO GUESS MY WORD")
print(f"It is {len(word)} lettered word.\n\n")
while True:
    if i == num_turns:
        print("You lost the game")
        print("The word was", word)
        break
    print(f"The word is: {w}")
    inp = input("Enter an alphabet:")
    let = get_char(inp)
    # print(f'Letters used = {alphabets_user}')
    # print(f'Correct Letters used = {correct_alph}')

    
    if let is not None:
        for j in range(len(word)):
            if word[j] == let:
                word_as_list = list(w)
                word_as_list[j] = let
                correct_alph.append(let)
                correct_alph = list(set(correct_alph))
                w = ''.join(word_as_list)
    i = len(alphabets_user) - len(correct_alph)  
    if word == w:
        print()
        print("You won the game!")
        print("The word indeed is", word)
        break
    # print(i)
    print(f"Number of turns left = {num_turns - i }")
    print()