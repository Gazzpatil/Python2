'''#Define a class attribute”color” with a default value white. I.e., Every Vehicle should be white.
output:Color: White, Vehicle name: School Volvo, Speed: 180, Mileage: 12
       Color: White, Vehicle name: Audi Q5, Speed: 240, Mileage: 18      '''

class Vehicle:
    color="white"

    def __init__(self):
        self.vehicle_name=input("enter the name of the vehicle:")
        self.speed=int(input("enter the speed:"))
        self.mileage=int(input("enter the mileage:"))
    def gazz(self):
        print("Vehicle name: {},Speed:{} ,Mileage:{}".format(self.Vehicle,self.speed,self.mileage))

class Vehicle2(Vehicle):
    def ash(self):
        print("Vehicle name: {},Speed:{} ,Mileage:{}".format(self.Vehicle,self.speed,self.mileage))

obj= Vehicle2()
obj.gazz()
obj.ash()



