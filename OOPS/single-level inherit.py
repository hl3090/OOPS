"""
single level inherictance: 

               class A    (parent)    (super)   (base)
                  |
               class B    (child)     (sub)     (derived)

               Note -: always create object of child class
    """
    
class A:
    num1 = 10
    num2 = 20
    
class B(A):
    def addition(self):
        self.ans = self.num1 + self.num2
        
    def display(self):
        print(self.ans)
        
        
obj = B()
obj.addition()
obj.display()                    