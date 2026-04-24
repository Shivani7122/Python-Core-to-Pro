names = ["Shivani","Ali","Lisa"]
bills = [45,78,73]

#ZIP:- Iterates over several iterables in parallel, producing tuples with an item from earch one.
for name , amount in zip(names, bills):
    print(f"{name} paid Rs.{amount}/-")