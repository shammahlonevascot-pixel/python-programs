# Name: Shammahlon T.Evasco
# ID Number: 26-4144-869
# Lab 5: Food Ordering and Billing System

# Print the MENU
print("===== RESTAURANT MENU =====")
print("1. Burger        - ₱75")
print("2. Pizza         - ₱150")
print("3. Spaghetti     - ₱100")
print("4. Fried Chicken - ₱120")
print("5. French Fries  - ₱60")
print("===========================")

#-----------------------------------------

# Ask the customer to select a menu
item_number = int(input("Enter the item number of your order(1-5): "))

# Make the initial value of food and price
food = ""
price = 0

#-----------------------------------------

# Match-case to determine the food item and its price
match item_number:
    case 1:
        food, price = "Burger", 75 #stores "burger" in food and 75 in price
    case 2:
        food, price = "Pizza", 150
    case 3:
        food, price = "Spaghetti", 100
    case 4:
        food, price = "Fried Chicken", 120
    case 5:
        food, price = "French Fries", 60
    case _:
        print("Invalid Selection.") # Handles any selection that does not match cases 1 through 5.

# Initialize the total bill
total_bill = 0

# Using conditionals and rlational statements
if food != "": # Checks if the the input is 
    quantity = int(input("Enter quantity for " + food + ": ")
    if quantity <= 0:
        print("Invalid Quantity.")
    else:
        total_bill = price * quantity
        print("\n----- ORDER SUMMARY -----")
        print("Item: " + str(food))
        print("Quantity: " + str(quantity))
        print("Total Bill: " + "Php" + str(total_bill))

if total_bill == 0: #If only total bill is 0
    print("Total Bill: ₱0")

print("Thank you for ordering!")
