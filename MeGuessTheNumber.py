print("Think of a number. I'll try to guess it.")
max = int(input("Your guess is between 0 and: "))
turns = int(input("How many chances will I get: "))
min= 0
win = 0
if max<=0 and turns<=0:
    print("Wrong input")
    
else:
    for i in range(turns):
        my_guess = min + round((max - min)/2)
        print(f"My guess is {my_guess}. Is it correct?")
        ans = input("Y/N: ")
        if ans=='Y':
            print("I ma too good ig ;)")
            win = 1
            break
        else:
            print("Is your number higher or lower than my guess")
            k = input("H/L: ")
            if k == "H":
                min = my_guess+1
            else:
                max = my_guess-1
    if not win:
        print("Oh I lost. :(")

