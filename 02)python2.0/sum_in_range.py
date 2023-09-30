'''low,high=1,5
sum=0
for i in range(low,high+1):
    sum+=i

print(sum)'''


num1 = int(input("enter the number 1:"))
num2 = int(input("enter the number 2:"))
sum = ((num2*(num2+1)/2)-(num1*(num1+1)/2)+num1)
print(sum)