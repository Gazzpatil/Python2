num=int(input("enter the number:"))
binary_val=num
decimal_val=0
base=1
while num>0:
    rem=num%10
    decimal_val=decimal_val+base*base
    num=num//10
    base=base*2

print(f"binary number is {binary_val,decimal_val}")    