'''#Define a class attribute”color” with a default value white. I.e., Every Vehicle should be white.
output:Color: White, Vehicle name: School Volvo, Speed: 180, Mileage: 12
       Color: White, Vehicle name: Audi Q5, Speed: 240, Mileage: 18      '''
'''class Vehicle:
    # Class attribute
    color = "White"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass


School_bus = Bus("School Volvo", 180, 12)
print(School_bus.color, School_bus.name, "Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage)

car = Car("Audi Q5", 240, 18)
print(car.color, car.name, "Speed:", car.max_speed, "Mileage:", car.mileage)'''

class Vehicle:
    color="White"

    def __init__(self):
        self.name =input("enter the name:")
        self.max_speed=int(input("enter the max_speeed"))

        self.mileage=int(input("enter the mileage:"))

class Bus(Vehicle):
    def gazz(self):
        print(Vehicle.color,self.name,self.max_speed,self.mileage)

class Car(Vehicle):
    def ash(self):
        print(Vehicle.color,self.name,self.max_speed,self.mileage)



obj = Bus()
obj.gazz()
obj1 = Car()
