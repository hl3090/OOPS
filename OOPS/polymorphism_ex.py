# Inheritance example / polymorphism method overriding

class A:
    def display(self):
        print("A class is here")
class B(A):
    def display(self):
        A.display(self)
        print("B class is here")
        
obj = B()

obj.display()                