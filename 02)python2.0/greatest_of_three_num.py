# using if else condition

'''num1 = int(input("enter the number 1:"))
num2 = int(input("enter the number 2:"))
num3 = int(input("enter the number 3:"))

if num1>=num2 and num1>=num3:
    print(f"{num1} is greatest!!")
elif(num2>=num1 and num2>=num3):
    print(f"{num2} is greatest")
else:
    print(f"{num3} is greatest!!")'''

#using nested if else

'''num1 = int(input("enter the number 1:"))
num2 = int(input("enter the number 2:"))
num3 = int(input("enter the number 3:"))

if num1>=num2:
    if num1>=num3:
        print(f"{num1} is greatest")
elif num2>=num1:
    if num2>=num3:
        print(f"{num2} is greatest")
else:
    print(f"{num3} is greatest!!")'''


num1, num2, num3 = 10 , 30 , 20

if num1 >= num2:
  if num1 >= num3:
    print(num1)
elif num2 >= num1:
  if num2 >= num3:
    print(num2)
else:
  print(num3)