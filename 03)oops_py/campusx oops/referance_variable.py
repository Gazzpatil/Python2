''''Reference Variable'''
#Reference variable holda the object
#We can create objects without reference variable as well
#An object can have multiple reference variable
#Assigning a new reference variable to an existing object does not create a new object

class Person:
    def __init__(self):
        self.name="nitish"
        self.gender="male"

p = Person()
q=p    #new reference variable
