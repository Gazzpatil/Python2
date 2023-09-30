'''A shop will give a discount of 10% if ṭhe cost of purchased quality is more than 1000:
a)ask user for quantity.
b)Suppose one unit will cost 100.
c)judge and print total cost for user.'''

quantity = int(input("Enter the number of quantities you have purchased:"))
total=quantity*100
if total>1000:
    print(f"the total cost after giving discount is Rs.{total-(total*.1)}")
else:
    print(f"total cost is  {total}")
