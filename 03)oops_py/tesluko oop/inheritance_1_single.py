#single level inheritance 

class A:
    def feature1(self):
        print("feature 1 is working:")
    
    def feature2(self):
        print("feature 2 is working")
class B:
    def feature3(self):
        print("feature 3 is working:")
    
    def feature4(self):
        print("feature 4 is working")

class C(A,B):
    def feature5(self):
        print("feature 5 is working:")



obj1 = A()
obj1.feature1()
obj1.feature2()
obj2 =B()
obj2.feature4()

obj3 =C()
obj3.feature5()
