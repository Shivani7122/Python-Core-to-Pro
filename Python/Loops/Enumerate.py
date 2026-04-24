menu = ["green tea","masala tea","Mint tea","Lemon tea","Black tea"]
for m in menu:
    print(f"Menu item is {m}")

    #for printing with numbering orders we use Enumerate() function
# print(list(enumerate(menu)))
# print(list(enumerate(menu, start=2)))

for idx , item in enumerate(menu, start = 1):
    print(f"{idx} Menu Item is {item}")