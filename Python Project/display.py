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

def display_shoes(shoes):
    print("\nAvailable Shoes:")
    if not shoes:
        print("No shoes available.")
        return
    
    # Define column widths and headers
    col_widths = [5, 20, 15, 10, 10, 15]  # ID, Type, Brand, Quantity, Rate, Origin
    headers = ["ID", "Type", "Brand", "Quantity", "Rate", "Origin"]
    
    # Prepare table data
    table_data = [
        [str(i + 1), shoe['type'], shoe['brand'], str(shoe['quantity']), f"{shoe['rate']:.2f}", shoe['origin']]
        for i, shoe in enumerate(shoes)
    ]
    
    # Print table
    print(create_table(headers, table_data, col_widths))
