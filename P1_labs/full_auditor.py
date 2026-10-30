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

def search_product(loaded_inventory, product_id):
    loaded_list = []
    for list_item in loaded_inventory:
        if list_item["ID"] == product_id:
            # print(f"Product found: ID: {list_item['ID']}, Name: {list_item['Name']}, Price: {list_item['Price']}, Stock: {list_item['Stock']}")
            loaded_list.append(list_item)
    return loaded_list

def display_all(s_list):
    for item in s_list:
        print (f"ID: {item['ID']}, Name: {item['Name']}, Price: {item['Price']}, Stock: {item['Stock']}")
    if len(s_list) == 0:
        print("No products in inventory.")

def load_inventory():
    with open("inventory.json", "r") as f:
        loaded_inventory = json.load(f)
    return loaded_inventory

def save_inventory(inventory):
    with open("inventory.json", "w") as f:
        json.dump(inventory, f, indent=4)

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

    if choice == "1":
        print("\nCurrent Inventory")
        print("=================")
        display_all(stock_list)  # product stored as type dictionary

    elif choice == "2":
        print("\nAdding new product")
        product = add_product()     # product stored as type dictionary
        print("Product added successfully!")

    elif choice == "3":
        print("\nUpdating stock")
        stock_list = update_stock(stock_list, product)  # product stored as type dictionary

    elif choice == "4":
        print("\nSearching product")
        product_id = input("Enter product ID: ")
        loaded_inventory = load_inventory()
        loaded_list = search_product(loaded_inventory, product_id)

        for item in loaded_list:
            if len(loaded_list) == 0:
                print("Product not found.")
            else:
                print (f"ID: {item['ID']}, Name: {item['Name']}, Price: {item['Price']}, Stock: {item['Stock']}")

    elif choice == "5":
        print("\nSaving inventory")
        save_inventory(stock_list)  # product stored as type dictionary

    elif choice == "6":
        if len(stock_list) > 0:     # Only saves if there are products in the stock list
            print("\nSaving inventory before exiting...")
            save_inventory(stock_list)
        print("Thank you for using Inventory Management System.\n")
        print("Program terminated.")

        continue_run = False