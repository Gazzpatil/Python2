# 2) Create a child class Bus that will inherit all of the variables and methods of the Vehicle class


'''class Vehicle:
    def __init__(self):
        self.name: name 
        self.color: color
        self.brand: brand_name

class Bus(Vehicle):
    pass

obj = bus("XUV500","black","Mahindra")
print(self.name,self.color,self.brand)'''

class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 180, 12)
print("Vehicle Name:", School_bus.name, "Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage)

        