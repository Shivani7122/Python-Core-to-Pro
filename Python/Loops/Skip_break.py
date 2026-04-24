flavours = ["Ginger","Out of Stock", "Lemon","Discountinued","Tulsi"]

for flavour in flavours:
    if flavour == "Out of Stock":
        continue 
    elif flavour == "Discontinued":
        break
    print(f"{flavour} flavour found !!")

        