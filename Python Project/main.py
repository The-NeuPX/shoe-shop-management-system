from file_reader import read_shoes, write_shoes
from display import display_shoes
from input_handler import get_action, get_sale_details, get_restock_details
from invoice_generator import generate_sale_invoice, generate_restock_invoice, display_sale_invoice

def get_string_input(prompt):
    while True:
        value = input(prompt)
        if value:
            return value
        print("Error: Input cannot be empty.")

def main():
    file_name = "Required.txt"
    while True:
        shoes = read_shoes(file_name)
        if not shoes:
            print(f"No shoes available. Add data to {file_name}.")
            action = get_string_input("Enter 'add' to create a sample file, or 'exit' to quit: ").lower()
            if action == 'exit':
                break
            elif action == 'add':
                sample_data = [
                    {'type': 'Loafer Light', 'brand': 'GoldStar', 'quantity': 200, 'rate': 1000.0, 'origin': 'domestic'},
                    {'type': 'Inigo 732', 'brand': 'Caliber', 'quantity': 100, 'rate': 2800.0, 'origin': 'domestic'},
                    {'type': 'Lite Racer', 'brand': 'Adidas', 'quantity': 200, 'rate': 7000.0, 'origin': 'international'}
                ]
                write_shoes(sample_data, file_name)
                print(f"Sample data written to {file_name}.")
                continue
        display_shoes(shoes)
        action = get_action()
        if action == 'exit':
            break
        elif action == 'sale':
            details = get_sale_details(shoes)
            if details is None:
                continue
            customer_name, items = details
            # Display invoice preview
            display_sale_invoice(customer_name, items, shoes)
            # Single confirmation prompt
            confirmation = get_string_input("Please confirm (yes/no): ").lower()
            if confirmation == 'yes':
                for idx, qty in items:
                    shoes[idx]['quantity'] -= qty
                generate_sale_invoice(customer_name, items, shoes)
                write_shoes(shoes, file_name)
                print("Sale completed.")
            else:
                print("Sale cancelled.")
        elif action == 'restock':
            details = get_restock_details(shoes)
            if details is None:
                continue
            vendor_name, items = details
            for idx, qty in items:
                shoes[idx]['quantity'] += qty
            generate_restock_invoice(vendor_name, items, shoes)
            write_shoes(shoes, file_name)

if __name__ == "__main__":
    main()
