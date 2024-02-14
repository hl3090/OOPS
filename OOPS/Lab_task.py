# using of multiple Inheritance
class SBI:
    def diplaysbi(self):
        print("SBI: Rate of Interest 8%")
class BOB:
    def displaybob(self):
        print("Bank of Baroda: Rate of Interest 7.5%")
class HDFC:
    def diplayhdfc(self):
        print("HDFC: Rate of Interest 6%")
class RBI(SBI,BOB,HDFC):
    def display(self):
        print("Presenting Rate of Interest of following Banks-:")
    
obj = RBI()

obj.display()
obj.diplaysbi()
obj.displaybob()
obj.diplayhdfc()                            