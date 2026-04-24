users = [
    {"id": 1,"total": 100,"coupon": "P20"},
    {"id": 2,"total": 101,"coupon": "Q20"},
    {"id": 3,"total": 130,"coupon": "S20"},
    {"id": 4,"total": 600,"coupon": "T20"}
]
discounts = {
    "P20":(0.2,0),    #(% discount, FLAT Rs. discount)
    "Q20":(0.5,0),
    "S20":(0,10),
    "T20":(0.7,7)
}
for user in users:
    percent,fixed = discounts.get(user["coupon"],(0,0))
    discount = user["total"] * percent + fixed
    print(f"id:{user["id"]} paid {user['total']} and got dicount for next visit of Rs. {discount}")