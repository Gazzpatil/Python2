class gazz:
    
    def gass(self):
        self.name=input("enter the name:")
        self.age=int(input("enter the age:"))
        self.gender=input("enter the gender")

    def ga(self):
        print("the name is {} and his age is {} and he is {}".format(self.name,self.age,self.gender))
    
class ash(gazz):
    def __init__(self):
        self.name=input("Enter your crush name")
    
    def ashu(self):
        print("your crush name is".format(self.name))
        
obj = ash()
obj.ashu()
