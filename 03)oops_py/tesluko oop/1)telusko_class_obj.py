#class always consist of attributes or variable and methods


class Computer:

    def config(self):
        print("pavilion","512 gb")


gazz = Computer()     #object 1
ash = Computer()      #object 2
gazz.config()
ash.config()
    #or
Computer.config(gazz)
Computer.config(ash)
