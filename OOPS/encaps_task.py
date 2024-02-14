class Jaybhavani:
    def __init__(self):
        print("Hello! Welcome to Jay Bhavani!!")
        self.product_list = []
        self.qty_list = []
        self.price_list = []

    def menu(self):
        menu = """
                      Menu
            vadapav       30
            dabeli        40
            sandwich      80
            bhel          100
            
       """
        print(menu)

    def get_order(self):
        choice = input("Enter name of your product: ")
        qty = int(input("Enter the quantity you want: "))
        if choice == "vadapav":
            price = qty * 30
        elif choice == "dabeli":
            price = qty * 40
        elif choice == "sandwich":
            price = qty * 80
        elif choice == "bhel":
            price = qty * 100    
        
        self.product_list.append(choice)
        self.qty_list.append(qty)
        self.price_list.append(price)
    
    def continue_order(self):
        user_choice = input("Do you want to add more if yes press y if no press n: ")
        if user_choice == 'y':
            return True
        else:
            return False

    def display(self):
        status = True
        while status:
            self.menu()
            self.get_order()
            status = self.continue_order()

        for item in self.product_list:
            index = self.product_list.index(item)
            print(f"{item} qty: {self.qty_list[index]} price: {self.price_list[index]}")
        
order = Jaybhavani()
order.display()

