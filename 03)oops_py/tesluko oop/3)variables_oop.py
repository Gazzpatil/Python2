# Variables in python

class Car:
    wheels=10    #class or static variable

    def __init__(self) :
        self.mil=40          #instance variable
        self.name="BMW"

obj1=Car()
obj2=Car()
obj1.mil=20
obj2.mil=30
obj1.wheels=8
print(obj1.mil,obj2.name,obj1.wheels)
print(obj2.mil,obj2.name,Car.wheels)
