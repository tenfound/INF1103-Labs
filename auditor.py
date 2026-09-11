# 1.Initialize the inventory to zero in the start
Inventory = 0
inventoryList = []
rejectedList= []

# 2.Run in a continuous loop asking user to enter a stock quantity, until the user types quit. (Think of which loop might be helpful here: for or while)
while 1:

    if Inventory == 500:    # 7. Overstock alert
        print("Inventory full!")
        break
    
    # 3.Accept stock values as integers.
    print(Inventory)
    stock = input("Stock value: ")

    if stock.isdigit() == True: # Checks if is number

        stock = int(stock)
        if stock < 0: # 5. Checks if stock is negative
            print("Stock cannot be a negative number")
            continue
        else:
            inventoryList.append(stock)
            Inventory += 1      # 6. Keeps running total of inventory
    
    else:   # 4. If not number
        if stock == "quit" or stock == "Quit":
            break
        else:
            rejectedList.append(stock)
            print("Input invalid.Please key in a valid integer.")
            continue

# 8. Reporting
print("\nNumber of items in inventory: ", Inventory)
print("Items in inventory:", inventoryList)
print("Rejected items:", rejectedList)