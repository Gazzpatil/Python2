class Person:
    def __init__(self,name_input,country_input):
        self.name=name_input                      #attribute
        self.country=country_input                #attribute

    def greet(self):
        if self.country == "india":
            print("Namaste",self.name)
        else:
            print("Hello",self.name)
        
#How to access attributes
p = Person("gazz","india")
print(p.country)  #attribute
print(p.name)
#How to access methods
p.greet()

#How to access non-existing attributes
p.gender ="male"
print(p.gender)
