# use volume upload if docker cannot find file

# 1. Persistence:
# At the start of the program, read the information previously saved
# in the inventory file. If the inventory file does not exist, start with an empty
# inventory and continue running without producing an error.

# 2. History Tracking:
# Use a Python list (array) to store every valid transaction amount entered.

# 3. Write-Back:
# When the user types quit, save the final total and the transaction history list to inventory.txt

# 4. Modularity:
# Maintain your functional design. Create a load_inventory() and save_inventory() function


# Commit your progress after you successfully complete each phase:
# a. After load_inventory() is working.
# b. After the list is successfully tracking history.
# c. After the final save_inventory() is verified.

# get_valid_input(): Handles prompt, input validation & returns valid integer or "quit" signal
def get_valid_input():
    end_run = 0
    Inventory = 0
    # inventory_list = []
    rejected_list= []
    while end_run != 1:
        if Inventory == 500:    # Overstock alert
            print("Inventory full!")
            end_run = 1

        stock = input("Stock value: ")

        if stock.isdigit() == True: # Checks if is number
        
            stock = int(stock)
            if stock <= 0: # Checks if stock is negative
                print("Stock cannot be a negative number or 0")
                continue
            else:   # When stock value is valid 
                # inventoryList.append(stock)
                Inventory = process_delivery(Inventory, stock)      # Keeps running total of inventory
                calculate_tax(stock)    # Calculates tax for delivery
        else:   # 4. If not number
            if stock == "quit" or stock == "Quit":
                end_run = 1
            else:
                rejected_list.append(stock)
                print("Input invalid.Please key in a valid integer.")
                continue

    return Inventory, rejected_list

# Tracks total number of deliveries in total
def process_delivery(current_total, new_value): 
    current_total += new_value
    return current_total

# calculate_tax(amount): takes delivery amt and returns tax (10% of specific delivery)
def calculate_tax(amount):
    # Assuming delivery value is $2 per item in delivery
    amount = amount * 2
    # Calculate tax on total amount
    amount += amount * 0.1

    print("Value of this delivery is: ", amount)
    # Return total value of that specific delivery
    return amount

def generate_report(total_units, failed_attempts):
    print("\nNumber of items in inventory: ", total_units)
    # print("Value of items in inventory:", total_value)
    print("Rejected item values:", failed_attempts)


Inventory, rejected_list = get_valid_input()
# calculate_tax(Inventory)

# 8. Reporting
generate_report(Inventory, rejected_list)