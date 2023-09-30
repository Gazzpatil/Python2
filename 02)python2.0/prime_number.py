'''num =int(input("enter the number:"))

for i in range(2,num):
    if num%i==0:
        print("number is not prime")
        break
else:
    print("number is prime!!")'''

num1=int(input("enter the number:"))
gazz=0
for i in range(2,num1):
    if num1%i==0:
        gazz+=1
        break
if gazz==1:
    print("not prime")
else:
    print("prime")