import json
class Product():
    def __init__(self, product_id: str, name: str, price: float, stock: int):
        self.__productid = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock
        
    def get_name():
        product_id = input("Prodcut ID: ")
        name = input("Product Name: ")
        return product_id, name
    
    def get_price():
        price = input("Product Price: ")
        return price

    def get_stock():
        stock = input("Stock Quantity: ")
        return stock

    def get_product_id(self):
        return self.__productid
    
class Inventory():
    def __init__(self):
        self.__products = []

    def add_product(self, product):
        self.__products.append(product)
        
    def search_product(self, searched_product_id):
        for product in self.__products:
            if product.get_product_id == searched_product_id:
                return product
            else:
                print("Product not found")
    def display_all(self):
        for p in self.__products:
            print(p)
    def save_inventory(self):
        with open("storage.json", "w") as f:
                json.dump(self.__products, f, indent=4)

    def inventory_length(self):
        if len(self.__products) == 0:
            return "empty"


def main():
    inventory = Inventory()
    # product = Product()
    
    print("1. Display all products")    # Display all products in current session
    print("2. Add product")     # Add to new product of class Product
    print("3. Update stock")    # Update inventory
    print("4. Search product")  # Search for product id in records
    print("5. Save inventory")  # Write to json
    print("6. Exit")

    while True:
        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nCurrent Inventory")
            print("=================")
            inventory.display_all()

        elif choice == "2":
            print("\nAdding new product")
            id, name = Product.get_name()
            price = Product.get_price()
            stock = Product.get_stock()
            product = Product(id, name, price, stock)

            print("Product added successfully!")

        elif choice == "3":
            print("\nUpdating stock")
            inventory.add_product(product)

        elif choice == "4":
            print("\nSearching product")
            search_id = input("Enter product ID: ")
            found_product = inventory.search_product(search_id)

        elif choice == "5":
            print("\nSaving inventory")
            inventory.save_inventory()

        elif choice == "6":
            if inventory.inventory_length() == "empty":     # Only saves if there are products in the stock list
                print("\nNothing to save.")
            else:
                inventory.save_inventory()
                print("Saving inventory...")

            print("Thank you for using Inventory Management System.\n")
            print("Program terminated.")

            return False

if __name__ == "__main__":
    main()