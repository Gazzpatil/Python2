#Write a function to calculate resistance and capacitance (i.e. the function takes current and voltage as data and returns resistance and power)
#import math

'''class Electric:
    
    def __init__(self,voltage,resistance):
        self.voltage=voltage
        self.resistance=resistance

    def current(self):
        print(self.voltage/self.resistance)
    
    def power(self):
        print(self.voltage**2/(self.resistance))

obj = Electric(10,10)
obj.current()
obj.power()'''

class Electric:

    def __init__(self):
        self.voltage=int(input("enter the voltage:"))
        self.resistance=int(input("enter the resistance:"))

    def current(self):
        print("the current is:", self.voltage/self.resistance)


    def power(self):
        print("the power is:", self.voltage**2 /(self.resistance))

obj =Electric()
obj.current()
obj.power()


        