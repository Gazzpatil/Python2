import random
computer=random.randint(1,100)
user=int(input("enter the number:"))
count=0
while user!= computer:
    if user>computer:
        print("user entered input is greater than computer!!")
    else:
        print("user entered input is less than computer generated!!")
    user=int(input("enter the number:"))
  

'''print(f"The correct guess is {user}")
print(f"the number of attempts are {count}")'''