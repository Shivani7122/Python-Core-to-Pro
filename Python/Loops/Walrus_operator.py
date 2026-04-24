#Walrus Operator ----->    := (Symbol)
value = 13
remainder = 13 % 5
if remainder:
    print(f"Not divisible , remainder is {remainder}")


#Let's write this above code using Walrus Operator
value = 14
if (remainder := value % 5):
    print(f"Not divisible , remainder is {remainder}")



available_sizes = ["small","medium","Large"]
if (requested_size := input("Enter your chai cup size: ")) in available_sizes:
    print(f"Here's your {requested_size} chai !")
else:
    print(f"{requested_size} Size is unavaible")