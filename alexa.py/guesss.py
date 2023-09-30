import random

jackpot=random.randint(1,100)

guess = int(input("enter the number"))

count = 0
while guess!=jackpot:
    if guess<jackpot:
        print("guess little bit high")
        
    else:
        print("guess little bit low")    
        
    guess = int(input("enter the number"))

    count+=1


print(f"the correct guess is {guess}")
print(f"the number of attempts are {count}")