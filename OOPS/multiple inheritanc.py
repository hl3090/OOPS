"""
Multiple Inheritance : 

                  A         B
                  |         |
                  -----------
                       |
                      C class
                      
   multiple inheritance which is contain 2 parent class and one child class...
   
   Note : in java multiple inheritance not supported becoz multiple inheritance provide 2 parents 
         so, in real world 2 parents are not possible                    
    """
    
class A:
    def displayA(self):
        print("Class A")
class B:
    def displayB(self):
        print("Class B")
class C(A,B):
    def displayC(self):
        print("Class C")

#always create object of child class        
obj = C()

obj.displayA()
obj.displayB()
obj.displayC()                            