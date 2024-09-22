
# tkinter是比较成熟的窗口部件和操作的程序库，一般默认有，如果没有可以pip install tkinter

import tkinter as tk 
from tkinter import ttk
from tkinter import messagebox


# 定义一个类，把大部分应用程序包在这个类里，再用系统默认的主程序__main__启动这个类。这是Python编程常用对方法
class StoreCheckoutApp:

    def __init__(self, root):                       # __init__ 子程序（方法）是在初始化这个类的时候自动调用的子程序（方法）
        # 使用self指代程序对象自己，所有变量都限制在自己都范围内，少用或不用全局变量，在多用户同时跑很多个程序时，自己都程序崩溃了不会影响别人，更加安全。
        self.root = root
        self.root.title("Store Checkout")           
        self.root.geometry("800x600")
        self.items_in_cart = 0
        # Store inventory with item prices
        # 用了一个字典类型的变量存放货物及其价格
        self.inventory = {
            'Apple': 1.00,
            'Banana': 0.50,
            'Cereal': 3.5,
            'Durian': 3,
            'Egg' : 0.2,
            'Fish' : 2,
            'Grain' : 1.75,
            'Orange': 0.75,
            'Milk': 2.50,
            'Bread': 2.00
        }


        # Store total amount
        self.total = 0.00

        # Label: Store heading 显示一个文本标签（lable），
        # tkinter 和其他绝大多数对窗口操作对程序一样，所有部件都是从一个“根”(root）继承出来对。根 有所有对属性、功能和方法一种，可以从根里面选择类型对对象（tkinter主要是窗口部件)继承出来。
        # 下面就从 根 里继承出来一个 lable 类型对对象
        self.label = tk.Label(root, text="Welcome to the Store", font=("Helvetica", 16))
        self.label.pack(pady=10) # 相对于上面一个部件往下10个像素

        # 下面从 根 里继承出来一个 combobox (下拉菜单) 部件。
        # Combobox: Item selection dropdown
        self.item_combobox = ttk.Combobox(root, values=list(self.inventory.keys())) # 将字典变量中的数据装载进这个下拉菜单
        self.item_combobox.set("Select an item")
        self.item_combobox.pack(anchor='nw',pady=10) # 把这个下拉菜单放置到左上角，nw意思是north west，pady 指的是在y轴方向相对于上一个窗口部件（本程序中是那个label）pad（空）10个像素

        # Button: Add item to cart
        # 下面从 根 里继承出来一个 button (按钮) 部件。
        self.add_button = tk.Button(root, text="Add to Cart", command=self.add_to_cart)
        self.add_button.pack(pady=10)

        # add by mw, a scrollable listbox
        # 下面比较复杂，因为要构建一个可以滚动对列表，所以先要从root中继承出一个框架(frame），在框架中安装一个列表(listbox）和一个滚动条（scrollbar），然后把他们两个部件关联起来。
        self.cart_frame = tk.Frame(root)
        # 把这个框架放到右上角。pack只能放相对位置，而且要从上往下放，不方便。这里用了place。‘ne' 是north east, 也就是右上角
        self.cart_frame.place(relx=1.0, rely=0.0, anchor='ne', x=-10, y=60)
        # 从 self.cart_frame 的 frame 类型对象中继承一个 listbox出来，这个listbox就只能限制在self.cart_frame里面了
        self.listbox = tk.Listbox(self.cart_frame, height=10, width=30)
        # 从 self.cart_frame 中继承出一个Scrollbar对象， 同样，这个滚动条也被限制在frame里。
        self.scrollbar = tk.Scrollbar(self.cart_frame, orient=tk.VERTICAL)
        self.listbox.config(yscrollcommand=self.scrollbar.set) # Attach the Scrollbar to the Listbox
        self.scrollbar.config(command=self.listbox.yview)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH)    # Pack the Listbox and Scrollbar
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Label: Total amount display
        self.total_label = tk.Label(root, text="Total: 0 items, $0.00", font=("Helvetica", 12))
        self.total_label.pack(pady=10)

        # Button: Checkout
        self.checkout_button = tk.Button(root, text="Checkout", command=self.checkout)
        self.checkout_button.pack(pady=10)

        
    # 这个应用里的每一个功能（子程序、方法）都应该把self作为参数变量传进来。因为子程序（函数）内定义都变量只能在子程序内用，
    # add_to_cart已经不再是__init__子程序，所以如果要用到__init__里的变量信息，就必须通过self来传导。否则，即使变量名一样，数据信息是会被重制，与另外一个子程序（方法）不同
    def add_to_cart(self):
        # Get selected item from combobox
        selected_item = self.item_combobox.get()

        if selected_item in self.inventory:

            # add by mw, also add into a listbox
            self.items_in_cart += 1
            self.listbox.insert(tk.END, str(self.items_in_cart)+"\t"+(selected_item)+"\t$"+str(self.inventory[selected_item])) # 添加列表项
            self.listbox.see(self.listbox.size()-1) # 用see方法把焦点聚焦到最后一行，以便有滚动到效果，否则数量超过列表显示行数后就好像没动静了

            
            self.total += self.inventory[selected_item]
            
            # Update total label
            self.total_label.config(text=f"Total: {self.items_in_cart} items, ${self.total:.2f}")

        else:
            # Error if no item selected
            messagebox.showerror("Error", "Please select a valid item!")

    def checkout(self):
        if self.items_in_cart <= 0:
            messagebox.showerror("Error", "Your cart is empty!")
        else:
            # Show total amount in a messagebox and reset the cart
            messagebox.showinfo("Checkout", f"Your total is: ${self.total:.2f}")
            #self.cart.clear()

            # add by mw
            self.listbox.delete(0, tk.END)
            self.items_in_cart = 0
            
            self.total = 0.00

            # Reset labels
            self.total_label.config(text="Total: 0 items, $0.00")

# Main Tkinter application window
# *********注意注意，这里是程序到入口***********
# 为什么要这样设置一个if而不直接运行?
# 主要是考虑当你把上面那个StoreCheckoutApp程序作为一个文件被他人import，或者作为后台程序向前台提供服务时，不会被意外启动
# 只有在直接运行这个.py的script文件时，才会直接运行。在我们这个程序里没有区别，主要是以后养成封装应用、流程调用的好习惯。
if __name__ == "__main__":
    root = tk.Tk()
    app = StoreCheckoutApp(root)
    root.mainloop()
