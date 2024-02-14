class Car:
    def __init__(self):
        self.wheels = 0
        self.color = ""
        
    def setWheels(self,num):
            self.wheels = num
            
    def getWheels(self):
        return self.wheels
    
    def setColor(self,colorname):
        self.color = colorname
        
    def getColor(self):
        return self.color
    
audi = Car()

audi.setColor("Black")
audi.setWheels(4)

print(audi.getColor())
print(audi.getWheels())                

suzuki = Car()

suzuki.setColor("Blue")
suzuki.setWheels(4)

print(suzuki.getColor())
print(suzuki.getWheels())                