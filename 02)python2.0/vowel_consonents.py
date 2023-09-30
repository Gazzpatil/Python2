# WAP to know vowel or consonant

gazz = input("enter the character")

if len(gazz)>1:
    print("invalid character")
elif gazz=="a" or gazz=="e" or gazz=="i" or gazz=="o" or gazz=="u":
    print(gazz,"its a vowel")    
else:
    print(gazz,"its a consonent")    