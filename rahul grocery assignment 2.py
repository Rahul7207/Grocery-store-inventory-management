# Initialize an empty inventory dictionary to store items
inventory = {}

# Function to add an item to the inventory
def add_item():
    item_name = input("Enter the item name: ")
    quantity = int(input("Enter the quantity: "))
    price = float(input("Enter the price per item: "))
    inventory[item_name] = {'quantity': quantity, 'price': price}
    print(f"{item_name} has been added to the inventory.")

# Function to update item quantities
def update_quantity():
    item_name = input("Enter the item name to update quantity: ")
    if item_name in inventory:
        new_quantity = int(input("Enter the new quantity: "))
        inventory[item_name]['quantity'] = new_quantity
        print(f"{item_name} quantity has been updated to {new_quantity}.")
    else:
        print(f"{item_name} is not in the inventory.")

# Function to view the current inventory
def view_inventory():
    print("Current Inventory:")
    for item, details in inventory.items():
        print(f"{item}: Quantity - {details['quantity']}, Price - ${details['price']}")

# Function to remove an item from the inventory
def remove_item():
    item_name = input("Enter the item name to remove: ")
    if item_name in inventory:
        del inventory[item_name]
        print(f"{item_name} has been removed from the inventory.")
    else:
        print(f"{item_name} is not in the inventory.")

# Main program loop
while True:
    print("\nMenu:")
    print("1. Add an item to the inventory")
    print("2. Update item quantity")
    print("3. View current inventory")
    print("4. Remove an item from the inventory")
    print("5. Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        add_item()
    elif choice == '2':
        update_quantity()
    elif choice == '3':
        view_inventory()
    elif choice == '4':
        remove_item()
    elif choice == '5':
        print("Exiting the inventory management program.")
        break
    else:
        print("Invalid choice. Please select a valid option.")