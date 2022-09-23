class A :
    def feature1 (self):
        print("feature 1 is working")
    def feature2 (self):
        print ("feature 2 is working")
class B :
    def feature3(self):
        print("feature 3 is working")
        def feature4(self):
            print("feature 4 is working")

a1 =A()
B1 =B()
a1.feature1()


# multi level
class A :
    def feature1 (self):
        print("feature 1 is working")
    def feature2 (self):
        print ("feature 2 is working")
class B(A) :
    def feature3(self):
        print("feature 3 is working")
    def feature4(self):
        print("feature 4 is working")
class C(B) :
    def feature5(self):
        print("feature 5 is working")
    def feature6(self):
        print("feature 6 is working")
a1 =A()
b1 =B()
c1 =C()
a1.feature1()
c1.feature5()

# MULTIPLE LEVEL

class A :
    def feature1 (self):
        print("feature 1 is working")
    def feature2 (self):
        print ("feature 2 is working")
class B :
    def feature3(self):
        print("feature 3 is working")
    def feature4(self):
        print("feature 4 is working")
class C(A,B) :
    def feature5(self):
        print("feature 5 is working")
    def feature6(self):
        print("feature 6 is working")
a1 =A()
b1 =B()
c1 =C()
a1.feature1()
b1.feature4()
