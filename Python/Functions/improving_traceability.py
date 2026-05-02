def add_vat(price, vat_rate):
    vat= price + price * ( vat_rate/100)
    return vat

orders = [100,150,200]
vat_rate = 10
for price in orders:
    final_amt = add_vat(price, vat_rate)
    print(f"The final price for order of ₹{price} is ₹{final_amt}")