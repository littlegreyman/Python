
# 定义销售记录对象（Object）类型，一种商品的购买记录作为一个对象
class Purchase_record:
    def __init__(self, pr_id, pr_name, pr_price, pr_num, pr_memo):
        self.id = pr_id
        self.name = pr_name
        self.price = pr_price
        self.num = pr_num                   #一种商品可以购买多个，或者按重量计价的重量
        self.memo = pr_memo

        self.subtotal = pr_price * pr_num   #在创建对象时自动计算每一样商品的“小计”

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
        p_r = Purchase_record(pr_id,pr_name,pr_price,pr_num,pr_memo)    # 创建对象
        total=total + p_r.subtotal
        sell_records.append(p_r)                                        # 装载对象，生成列表
        
print("------------------LIST------------------")


print("id\t product\t price\t quantity\t subtotal\t memo")
for p in sell_records:
    print(f"{str(p.id).ljust(4)}\t{p.name.ljust(8)}\t{str(p.price).rjust(5)}\t{str(p.num).rjust(8)}\t{str(round(p.subtotal,2)).rjust(8)}\t{p.memo}")

print(f"Your total is :${total}")    
