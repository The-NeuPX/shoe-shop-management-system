import datetime
import os

def calculate_discount(qty, origin):
    discount = 0.0
    if qty > 10:
        discount += 0.05  # 5% discount for > 10 items
        if origin == 'domestic':
            discount += 0.07  # Additional 7% for domestic
    return discount

def create_table(headers, rows, col_widths):
    # Create separator line
    separator = "+".join("-" * w for w in col_widths)
    
    # Format header
    header_line = "|".join(f"{h:<{w}}" for h, w in zip(headers, col_widths))
    table = [f"+{separator}+", f"|{header_line}|", f"+{separator}+"]
    
    # Format rows
    for row in rows:
        row_line = "|".join(f"{str(v):<{w}}" for v, w in zip(row, col_widths))
        table.append(f"|{row_line}|")
    
    # Add bottom border
    table.append(f"+{separator}+")
    return "\n".join(table)

def generate_sale_invoice(customer_name, items, shoes):
    try:
        now = datetime.datetime.now()
        date_str = now.strftime("%Y-%m-%d %H:%M:%S")
        file_date = now.strftime("%Y%m%d_%H%M%S")
        folder = "invoices"
        os.makedirs(folder, exist_ok=True)
        file_name = os.path.join(folder, f"sale_{customer_name.replace(' ', '_')}_{file_date}.txt")
        
        headers = ["Type", "Brand", "Qty", "Rate", "Discount", "Subtotal"]
        col_widths = [20, 15, 5, 10, 10, 10]  # Adjusted for content
        table_data = []
        total = 0.0
        for idx, qty in items:
            shoe = shoes[idx]
            price = shoe['rate'] * qty
            discount = calculate_discount(qty, shoe['origin'])
            discounted = price * (1 - discount)
            discount_amount = price * discount
            table_data.append([
                shoe['type'],
                shoe['brand'],
                str(qty),
                f"{shoe['rate']:.2f}",
                f"{discount_amount:.2f}",
                f"{discounted:.2f}"
            ])
            total += discounted
        
        with open(file_name, 'w') as f:
            f.write(f"--- Sale Invoice ---\n")
            f.write(f"Date: {date_str}\n")
            f.write(f"Customer: {customer_name}\n\n")
            f.write(create_table(headers, table_data, col_widths))
            f.write(f"\nTotal Amount: {total:.2f}\n")
            f.write("Thank you!\n")
        print(f"Sale invoice generated: {file_name}")
    except Exception as e:
        print(f"Error generating sale invoice: {e}")

def generate_restock_invoice(vendor_name, items, shoes):
    try:
        now = datetime.datetime.now()
        date_str = now.strftime("%Y-%m-%d %H:%M:%S")
        file_date = now.strftime("%Y%m%d_%H%M%S")
        folder = "invoices"
        os.makedirs(folder, exist_ok=True)
        file_name = os.path.join(folder, f"restock_{vendor_name.replace(' ', '_')}_{file_date}.txt")
        
        headers = ["Type", "Brand", "Qty", "Rate", "Subtotal"]
        col_widths = [20, 15, 5, 10, 10]  # Adjusted for content
        table_data = []
        total = 0.0
        for idx, qty in items:
            shoe = shoes[idx]
            price = shoe['rate'] * qty
            table_data.append([
                shoe['type'],
                shoe['brand'],
                str(qty),
                f"{shoe['rate']:.2f}",
                f"{price:.2f}"
            ])
            total += price
        
        with open(file_name, 'w') as f:
            f.write(f"--- Restock Invoice ---\n")
            f.write(f"Date: {date_str}\n")
            f.write(f"Vendor: {vendor_name}\n\n")
            f.write(create_table(headers, table_data, col_widths))
            f.write(f"\nTotal Amount: {total:.2f}\n")
            f.write("Restock complete.\n")
        print(f"Restock invoice generated: {file_name}")
    except Exception as e:
        print(f"Error generating restock invoice: {e}")

def display_sale_invoice(customer_name, items, shoes):
    now = datetime.datetime.now()
    date_str = now.strftime("%Y-%m-%d %H:%M:%S")
    
    headers = ["Type", "Brand", "Qty", "Rate", "Discount", "Subtotal"]
    col_widths = [20, 15, 5, 10, 10, 10]  # Adjusted for content
    table_data = []
    total = 0.0
    for idx, qty in items:
        shoe = shoes[idx]
        price = shoe['rate'] * qty
        discount = calculate_discount(qty, shoe['origin'])
        discounted = price * (1 - discount)
        discount_amount = price * discount
        table_data.append([
            shoe['type'],
            shoe['brand'],
            str(qty),
            f"{shoe['rate']:.2f}",
            f"{discount_amount:.2f}",
            f"{discounted:.2f}"
        ])
        total += discounted
    
    print(f"\n--- Sale Invoice (Preview) ---")
    print(f"Date: {date_str}")
    print(f"Customer: {customer_name}\n")
    print(create_table(headers, table_data, col_widths))
    print(f"\nTotal Amount: {total:.2f}")
    # Removed the redundant prompt here
