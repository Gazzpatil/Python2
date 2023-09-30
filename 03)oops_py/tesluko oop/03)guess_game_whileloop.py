#guessing game me vs the system

import random

jackpot = random.randint(1,100)
count=1
guess = int(input("enter the number:"))
while guess!=jackpot:
    if guess<jackpot:
        print("Guess little bit high!!")
    else:
        print("Guess little bit low ")
    guess = int(input("enter the number:"))
    count+=1


print(f"therefore the correct number is {guess}")
print(f"In {count} attemps you made the correct guess")