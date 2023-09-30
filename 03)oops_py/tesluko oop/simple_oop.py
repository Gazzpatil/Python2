class Student:
    def __init__(self):
        self.name=input("enter the name:")
        self.gender=input("enter the gender:")
        self.age=int(input("enter the age:"))
    def data(self):
        print("Name:",self.name)
        print("Gender:",self.gender)
        print("Age:",self.age)






gazz=Student()

gazz.data()
