class Computer:
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram



    def config(self):
        print("config:", self.cpu,self.ram)


obj1= Computer('intel',8)
obj2=Computer('ryzon',5400)

obj1.config()
obj2.config()
        