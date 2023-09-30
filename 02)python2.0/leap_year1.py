year =int(input("enter the year:"))

'''if year%4==0 & year%100==0 & year%400==0:
    print( f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")'''

if year%4==0 & year%100!=0 & year%400!=0:
    print("its  a leap year ")
else:
    print("its not a leap year")