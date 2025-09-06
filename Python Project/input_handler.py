def get_string_input(prompt):
    while True:
        value = input(prompt)
        if value:
            return value
        print("Error: Input cannot be empty.")

def get_int_input(prompt, min_value=1):
    while True:
        try:
            value = int(input(prompt))
            if value >= min_value:
                return value
            print(f"Error: Value must be at least {min_value}.")
        except ValueError:
            print("Error: Please enter a numerical value.")

def get_action():
    while True:
        action = input("Enter action (sale, restock, exit): ").lower()
        if action in ['sale', 'restock', 'exit']:
            return action
        print("Error: Invalid action. Choose 'sale', 'restock', or 'exit'.")

def get_sale_details(shoes):
    customer_name = get_string_input("Enter customer name: ")
    items = []
    while True:
        shoe_id = get_int_input("Enter shoe ID to buy (or 0 to finish): ", min_value=0)
        if shoe_id == 0:
            break
        if shoe_id > len(shoes):
            print("Error: Invalid shoe ID.")
            continue
        qty = get_int_input("Enter quantity: ")
        available = shoes[shoe_id - 1]['quantity']
        if qty > available:
            print(f"Error: Only {available} available.")
            continue
        items.append((shoe_id - 1, qty))
    if not items:
        return None
    return customer_name, items

def get_restock_details(shoes):
    vendor_name = get_string_input("Enter vendor name: ")
    items = []
    while True:
        shoe_id = get_int_input("Enter shoe ID to restock (or 0 to finish): ", min_value=0)
        if shoe_id == 0:
            break
        if shoe_id > len(shoes):
            print("Error: Invalid shoe ID.")
            continue
        qty = get_int_input("Enter quantity to add: ")
        items.append((shoe_id - 1, qty))
    if not items:
        return None
    return vendor_name, items
