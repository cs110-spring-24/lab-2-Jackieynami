import random
num = random.randint(1, 100)

user = input("Enter your guess: ")
user = int(user)

if user > num:
    print("Too high, it was", num)
elif user < num:
    print("Too low, it was", num)
else:
    print("You got it!")

user = 0
while user != num:
    user = int(input(f" Guess a number between {low} and {high}: "))
    
    if user > num:
        print("Too high!")
        guess_count += 1
        high = user
    elif user < num:
        print("Too low!")
        guess_count += 1
        low = user
    else:
        print("You win!")
        guess_count += 1
        print(f"You guess {guess_count} times!")

startover = input("Play again? ")
if startover == "Yes":
    print("Goodbye!")


    
    
