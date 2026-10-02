# Represent inventory items using dictionaries and store at elast 3 products in a list
# Maintain functional design. Create add_product(), update_stock(), search_product() and display_all() in inventory dictionary
# Check if inventory.json exists. Create load_inventory() to load inventory.json if it exists. Otherwise start with
# empty inventory. Create save_inventory() to save data into json
# Menu options to Display, Add, Update,. Search, Save and Exit

def add_product():
    product = {
        "ID" : input("Product ID: "),
        "Name" : input("Product Name: "),
        "Price" : float(input("Price: ")),
        "Stock" : int(input("Stock Quantity: "))
    }
    print("Product added successfully!")

    return product

# def update_stock():

# def search_product():

# def display_all():

# def load_inventory():

# def save_inventory(inventory):

continue_run = True

print("1. Display all products")
print("2. Add product")
print("3. Update stock")
print("4. Search product")
print("5. Save inventory")
print("6. Exit")

while continue_run == True:

    choice = input("Enter your choice: ")
    print(choice)
    if choice == "1":
        print("Current Inventory")

    elif choice == "2":
        print("Add new product")
        product = add_product()     # product stored as type dictionary

    elif choice == "3":
        print("Update stock")

    elif choice == "4":
        print("Search product")
        product_id = input("Enter product ID: ")

    elif choice == "5":
        print("Save inventory")

    elif choice == "6":
        print("Saving inventory before exiting...")
        print("Thank you for using Inventory Management System.\n")
        print("Program terminated.")

        continue_run = False