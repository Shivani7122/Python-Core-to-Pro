staff = [("Amit",16),("Zara",23),("Laksh",25)]
for name , age in staff:
    if age >=18:
        print(f"{name} is eligible for hiring!")
        break
else:
    print("No one is eligible for hiring :(")