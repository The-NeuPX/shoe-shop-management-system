import os

def remove_leading_trailing_spaces(s):
    start = 0
    while start < len(s) and s[start] == ' ':
        start += 1
    end = len(s)
    while end > start and s[end-1] == ' ':
        end -= 1
    return s[start:end]

def read_shoes(file_name="Required.txt"):
    shoes = []
    if not os.path.exists(file_name):
        return shoes
    with open(file_name, 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            if line.endswith('\n'):
                line = line[:-1]
            fields = line.split(',')
            
            shoe_type = remove_leading_trailing_spaces(fields[0])
            brand = remove_leading_trailing_spaces(fields[1])
            quantity_str = remove_leading_trailing_spaces(fields[2])
            rate_str = remove_leading_trailing_spaces(fields[3])
            origin = remove_leading_trailing_spaces(fields[4])
            try:
                quantity = int(quantity_str)
                rate = float(rate_str)
            except ValueError:
                continue
            shoes.append({
                'type': shoe_type,
                'brand': brand,
                'quantity': quantity,
                'rate': rate,
                'origin': origin.lower()
            })
    return shoes

def write_shoes(shoes, file_name="Required.txt"):
    with open(file_name, 'w') as f:
        for shoe in shoes:
            line = f"{shoe['type']}, {shoe['brand']}, {shoe['quantity']}, {shoe['rate']}, {shoe['origin']}\n"
            f.write(line)

