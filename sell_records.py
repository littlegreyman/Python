class Purchase_record:
    def __init__(self, pr_id, pr_name, pr_price, pr_num, pr_memo):
        self.id = pr_id
        self.name = pr_name
        self.price = pr_price
        self.num = pr_num
        self.memo = pr_memo

        self.subtotal = pr_price * pr_num

sell_records = []
total = 0
pr_id = 0

while True:
    pr_name = input("Enter the name of the product(q to quit):")
    if pr_name == "q":
        break
    else:
        pr_id = pr_id + 1
        pr_price = float(input(f"Enter the price of the {pr_name}:$"))
        pr_num = int(input(f"Enter the quantity of {pr_name}:"))
        pr_memo = input(f"Enter the memo or promotion info of {pr_name}:")
        p_r = Purchase_record(pr_id,pr_name,pr_price,pr_num,pr_memo)
        total=total + p_r.subtotal
        sell_records.append(p_r)
        
print("------------------LIST------------------")


print("id\t product\t price\t quantity\t subtotal\t memo")
for p_r in sell_records:
    print(f"{str(p_r.id).ljust(4)}\t{p_r.name.ljust(8)}\t{str(p_r.price).rjust(5)}\t{str(p_r.num).rjust(8)}\t{str(round(p_r.subtotal,2)).rjust(8)}\t{p_r.memo}")

print(f"Your total is :${total}")    
