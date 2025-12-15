# Shopping Cart

# Create a Product class with name, price.

# Create a Cart class to hold products.

# Methods: add_product(), remove_product(), total_price().

# Use loops to let the user add/remove multiple products.

# Use if statements to handle invalid inputs.



class Shopping_list:
    def __init__(self):
        self.products = {
            "Potato" : 1.99 ,
            "Carrot" : 2.49,
            "Onion" : 4,
        }       

    def menu(self):
        print ("Available Products")
        for i, (product,price) in enumerate (self.products.items(), 1):
            print(f"{i}.{product} - ${price}")

class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product_name, product_price):
        self.items.append((product_name , product_price))
        print (f"{product_name}, has been added to your cart")

    def remove_product(self, product_name):
        for item in self.items:
            if item[0] == product_name:
                self.items.remove(item)
                print(f"{product_name}, has been removed from your cart.")
                return
        print("Item not found")
    
    def total_price(self):
        total = 0
        for item in self.items:
            total += item[1]
        print (f"Total price : ${total:.2f}")

shopping_list = Shopping_list()
cart = Cart()

while True:
    print("\nMenu:")
    print("1. Show Products")
    print("2. Add Product to Cart")
    print("3. Remove Product from Cart")
    print("4. Show Total Price")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        shopping_list.menu()
    elif choice == "2":
        name = input("Enter product name to add: ")
        if name in shopping_list.products:
            cart.add_product(name, shopping_list.products[name])
        else:
            print("Product not found!")
    elif choice == "3":
        name = input("Enter product name to remove: ")
        cart.remove_product(name)
    elif choice == "4":
        cart.total_price()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice!")