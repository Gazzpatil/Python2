#Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 50.


class Vehicle():
    def __init__(self,seating_capacity):
        self.seating_capacity=seating_capacity
    
class Bus(Vehicle):
    def info(self):
        print(f"the seating capacity of the bus is {self.seating_capacity}")

obj = Bus(50)
obj.info()