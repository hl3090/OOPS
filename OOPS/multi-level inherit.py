"""
Muti-level Inheritance: 
          
          class A
              |
          class B
              |
           class C       
    """
    
class A:
    def displayA(self):
        print("Class A is here") 
        
class B(A):
    def displayB(self):
        print("Class B is here")
        
class C(B):
    def displayC(self):
        print("Class C is here")
        
obj = C()

obj.displayA()
obj.displayB()
obj.displayC()                           