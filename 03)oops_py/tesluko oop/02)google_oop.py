#Inheritance
class Employee:
    def __init__(self,name,salary):
        self.name=name 
        self.salary=salary

    def tim(self):
        print(f"the name of the employee is{self.name} and his salary is {self.salary}")
class programmer(Employee):
    def showdetails(self):
        print("the default job is backend devloper")

obj1=programmer("gazz",500)

obj1.showdetails()



