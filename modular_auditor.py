# 1.Initialize the inventory to zero in the start

# 2.Run in a continuous loop asking user to enter a stock quantity, until the user types quit
# 3. If user enters valid value: a) Add delivery amt to running total b) Calculate tax for delivery c) Update counters and records
# 4. Reporting: Print Total no. of deliveries and failed attempts 

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

# Self Reflection:
# Returning tax amount allows us to easily access that value without having to do the calculations again if we need it outside the function.
# However, since we were not told to use the tax amount outside the function, I printed the tax value directly in the function.
