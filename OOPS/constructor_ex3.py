class Book:
    def input(self,bookname,bookprice):
        self.bookname = bookname
        self.bookprice = bookprice
        
    def display(self):
        print(f"Bookname: {self.bookname}")
        print(f"Bookprice: {self.bookprice}")
        
shop = Book()

book_name = input("Enter nameof book: ")
book_price = int(input("Enter price of your book: "))

shop.input(bookname=book_name,bookprice=book_price)
shop.display()            