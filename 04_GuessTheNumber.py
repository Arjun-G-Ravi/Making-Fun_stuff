import random
num_turns = 10
print(f"I will guess a number between 1 and 100. You have to guess it in {num_turns} turns.")
num = random.randint(1,100)
turns = num_turns
while turns:
    guess = int(input("Enter a number: "))
    if guess == num:
        print("The guess is correct\nYou won!")
        break
    else:
        turns-=1
        if not turns:
            print(f"You lost.\nThe number was {num}.\n")
            break
        print(f"Wrong guess. You have {turns} more chance(s)")
        if guess > num:
            print(f"The number is lower than {guess}")
        else:
            print(f"The number is higher than {guess}")