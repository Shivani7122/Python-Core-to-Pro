def update_order():
    chai_type ="Elaichi"
    def kitchen():
        nonlocal chai_type     #nonlocal means inside to inside function, it works on just above the function 
        chai_type = "Kesar"
    kitchen()
    print("After kitchen update",chai_type)

update_order()
    