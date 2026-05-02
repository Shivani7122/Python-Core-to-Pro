def calculate_bill(cups, price_per_cup):
    return cups * price_per_cup

cups = int(input("Enter the number of cups: "))
price_per_cup = float(input("Enter the price per cup: "))
total_bill = calculate_bill(cups, price_per_cup)
print(f"Total bill is : ₹ {total_bill}/-")