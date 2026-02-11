secret=5
guess_count=0
guess_limit=3
while guess_count<guess_limit:
    guess_number=int(input("Guess the number: "))
    guess_count+=1
    if guess_number==secret:
        print("You guessed the number")
        break
else :
    print("You failed to guess the number")
