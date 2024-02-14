class Vehicle:
    # self : It is represent current class properly 
    # it is similar like this keyword
    
    def __init__(self,wheels,vehiclename):
        self.wheels = wheels
        self.vehiclename = vehiclename
        
    def display(self):
        print(f"{self.vehiclename}")
        print("wheels: ",self.wheels)
        
car = Vehicle(4,'car')
car.display()

bike = Vehicle(2,'bike')
bike.display()

auto = Vehicle(3,'rickshaw')
auto.display()            