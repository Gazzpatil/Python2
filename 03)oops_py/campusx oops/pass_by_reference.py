class Person:
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
#outside the class function
def greet(person):
    print("Hi my name is",person.name,"and I am a",person.gender)
    