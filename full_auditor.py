# Represent inventory items using dictionaries and store at elast 3 products in a list
# Maintain functional design. Create add_product(), update_stock(), search_product() and display_all() in inventory dictionary
# Check if inventory.json exists. Create load_inventory() to load inventory.json if it exists. Otherwise start with
# empty inventory. Create save_inventory() to save data into json
# Menu options to Display, Add, Update,. Search, Save and Exit
import json

def add_product():
    product = {
        "ID" : input("Product ID: "),
        "Name" : input("Product Name: "),
        "Price" : float(input("Price: ")),
        "Stock" : int(input("Stock Quantity: "))
    }
    return product

def update_stock(stock_list, new_stock):
    if new_stock == []:
        print("No product to update. Please add a product first.")
        return stock_list
    stock_list.append(new_stock)
    print("Stock updated successfully!")
    return stock_list

# def search_product():

def display_all(s_list):
    for item in s_list:
        print(item)
    if len(s_list) == 0:
        empty_variable = "No products in inventory."
        return empty_variable

# def load_inventory():

def save_inventory(inventory):
    with open("inventory.json", "w") as f:
        json.dump(inventory, f)

continue_run = True
stock_list = []
product = []

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
        result = display_all(stock_list)  # product stored as type dictionary
        if result == "No products in inventory.":
            print(result)

    elif choice == "2":
        print("Add new product")
        product = add_product()     # product stored as type dictionary
        print("Product added successfully!")

    elif choice == "3":
        print("Update stock")
        stock_list = update_stock(stock_list, product)  # product stored as type dictionary

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