Secret_number = 8
GuessCount = 0
GuessLimit = 3
while GuessCount < GuessLimit:
    Guess = int(input("Guess:"))
    GuessCount += 1
    if Guess == Secret_number:
        print('You win!')
else:
    print('You failed. Try again.')