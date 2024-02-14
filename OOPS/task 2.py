# # menu="""
# #             JAY BHAVANI
               
# #                MENU
# #         vapapav       Rs.40
# #         dabeli        Rs.30
# #         bhel          Rs.75
# #         sandwich      Rs.130

# #         Press 1 to Add The Product 
# #         Press 2 to Remove The Product

# # """
# # cart=[] 
# # qty_list=[]
# # price_list=[]

# # status=True
# # addStatus = True 
# # removeStatus = True 
# # while status:
# #     print(menu)
# #     choice=int(input("Enter your choice:"))
# #     if choice==1:
# #         while addStatus:
# #             product_name=input("Enter the product you want to add :").lower()
# #             qty=int(input("Enter the number of quantity you want :"))
# #             price=0

# #             if product_name=="vadapav":
# #                 price=40
# #             elif product_name=="dabeli":
# #                 price=30
# #             elif product_name=="bhel":
# #                 price=75
# #             elif product_name=="sandwich":
# #                 price==130
            
# #             cart.append(product_name)
# #             qty_list.append(qty)
# #             price_list.append(price)

# #             choice=input("Do you want to cpurchase more produt: Press Y for yes and N for no:")
# #             if choice=="y":
# #                 addStatus=True
# #             else:
# #                 addStatus=False
# #     else: 
# #      while removeStatus:

# #         remove_product_name=input("Enter the product you want to remove :")
# #         r_index_value=cart.index(remove_product_name)
# #         cart.pop(r_index_value) 
# #         qty_list.pop(r_index_value)
# #         price_list.pop(r_index_value)

# #         choice=input("Do you want to cpurchase more produt: Press Y for yes and N for no:")
# #         if choice=="y":
# #             addStatus=True
# #         else:
# #             addStatus=False

# #     choice=input("Do you want to perform more operations: Press Y for yes and N for no:")
# #     if choice=="y":
# #         status=True
# #     else:
# #         status=False


# # print("--------------------")

# # for product in cart:

# #     index_value=cart.index(product)

# #     qty_value=qty_list[index_value]

# #     price_value=qty_value * price_list [index_value]

# #     print(f"{product} Qty: {qty_value} = Rs. {price_value}")



# class Cart:
#     def __init__(self):
#         self.cart = []
#         self.qty_list = []
#         self.price_list = []

#     def add_product(self):
#         product_name = input("Enter the product you want to add: ").lower()
#         qty = int(input("Enter the number of quantity you want: "))
#         price = 0

#         if product_name == "vadapav":
#             price = 40
#         elif product_name == "dabeli":
#             price = 30
#         elif product_name == "bhel":
#             price = 75
#         elif product_name == "sandwich":
#             price = 130

#         self.cart.append(product_name)
#         self.qty_list.append(qty)
#         self.price_list.append(price)

#     def remove_product(self):
#         remove_product_name = input("Enter the product you want to remove: ")
#         r_index_value = self.cart.index(remove_product_name)
#         self.cart.pop(r_index_value)
#         self.qty_list.pop(r_index_value)
#         self.price_list.pop(r_index_value)

#     def perform_operations(self):
#         status = True
#         while status:
#             print("\n--------------------")
#             print("JAY BHAVANI")
#             print("MENU")
#             print("vapapav       Rs.40")
#             print("dabeli        Rs.30")
#             print("bhel          Rs.75")
#             print("sandwich      Rs.130")
#             print("\n")
#             print("Press 1 to Add The Product")
#             print("Press 2 to Remove The Product")
#             print("Press 3 to Exit")

#             choice = int(input("Enter your choice: "))

#             if choice == 1:
#                 self.add_product()
#             elif choice == 2:
#                 self.remove_product()
#             elif choice == 3:
#                 status = False
#             else:
#                 print("Invalid choice. Please try again.")

#             choice = input("Do you want to perform more operations: Press Y for yes and N for no: ")
#             if choice.lower() == "y":
#                 status = True
#             else:
#                 status = False

#     def display_cart(self):
#         print("\n--------------------")
#         for product in self.cart:
#             index_value = self.cart.index(product)
#             qty_value = self.qty_list[index_value]
#             price_value = qty_value * self.price_list[index_value]
#             print(f"{product} Qty: {qty_value} = Rs. {price_value}")


# if __name__ == "__main__":
#     cart = Cart()
#     cart.perform_operations()
#     cart.display_cart()

