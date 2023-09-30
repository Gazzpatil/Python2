gazz=input("Enter the character")
'''if len(gazz)>1:
    print("the entered character is not a alphabet!!")
elif('a'<=gazz <= 'z' or 'A'<=gazz<='Z'):
    print("It is an alphabet!!")
else:
    print("It is not an alphabet!!!")'''

if(len(gazz)>1):
    print("invalid input")
elif (ord(gazz)>=97 and ord(gazz)<=122) or (ord(gazz)>=65 and ord(gazz)<=90):
    print("Alphabet")
else:
    print("Not Alphabet")
