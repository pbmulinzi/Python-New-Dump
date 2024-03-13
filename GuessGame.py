Secret_Number = 9
Guess_Count = 0
Guess_limit = 3
while Guess_Count < Guess_limit:
    Guess = int(input("Guess:"))
    Guess_Count += 1
    if Guess == Secret_Number:
        print('You win!')
        break
else:
    print("Sorry, try again..")