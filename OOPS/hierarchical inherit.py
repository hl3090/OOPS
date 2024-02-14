"""
Hierarchical Inheritance:

                  class A
                     |
                  --------
                  |      |
             class B    class C
"""
    
class A:
    num1 = 10
    num2 = 20
    
class B(A):
    def addition(self):
        print(self.num1 + self.num2)        
        
class C(A):
    def multiplication(self):
        print(self.num1 * self.num2) 
        
objB = B()
objC = C()

objB.addition()
objC.multiplication()


