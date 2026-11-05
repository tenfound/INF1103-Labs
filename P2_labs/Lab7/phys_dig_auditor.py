from class_PhysicalProduct import PhysicalProduct
from class_DigitalProduct import DigitalProduct
from class_Inventory import Inventory
def main():
    inventory = Inventory()
    # product = Product()

    while True:
        print("1. Display all products")    # Display all products in inventory2.json
        print("2. Add product")     # Add to new product of class Product
        print("3. Update stock")    # Update inventory
        print("4. Search product")  # Search for product id in inventory2.json
        print("5. Save inventory")  # Write to json
        print("6. Exit")
        
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

            print("Product added successfully!\n")

        elif choice == "3":
            print("\nUpdating stock")
            inventory.add_product(product)

        elif choice == "4":
            print("\nSearching product")
            search_id = input("Enter product ID: ")
            found_product = inventory.search_product(search_id)
            print(found_product)

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