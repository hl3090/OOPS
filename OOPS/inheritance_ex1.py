"""
Inheritance: one class derived properties of another class which is represent parent and child 
            relationship...
"""
class Parent:
    num1 = 10
    num2 = 20
    
class Child(Parent):     # inherit parent class to child class 
    def display(self):
        print(self.num1)
        print(self.num2)
        
# always create object of child class
obj = Child()
obj.display()

