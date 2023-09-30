#constructors in inheritance

class A:

    def __init__(self):
        print("in A init")
    
    def feature1(self):
        print("working on feature 1")
    def feature2(self):
        print("working on feature 2")

class B(A):
    def __init__(self):
        super().__init__()  # use super() to access the parent class constructor
        print("In B init")
    def feature3(self):
        print("working on feature 1")
    def feature4(self):
        print("working on feature 2")

obj = B()

