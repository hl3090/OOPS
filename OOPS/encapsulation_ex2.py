class Mobile():
    def __init__(self):
        self.mobile = 15000   # public 
        self.__laptop = 25000    # private data
        
    def display(self):
        print("Mobile: ",self.mobile)
        print("Laptop: ",self.__laptop)
      
    # creating a function to change price outside the class    
    def changePrice(self,mobileprice,laptopprice):
        self.mobile = mobileprice
        self.__laptop = laptopprice
            
        
obj = Mobile()
obj.display()

obj.mobile = 20000  # changed price
obj.__laptop = 30000  

# print(obj.mobile)
# print(obj.__laptop)
        
obj.changePrice(30000,40000)
obj.display()        
            