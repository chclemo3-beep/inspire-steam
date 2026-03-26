import tkinter as tk
from tkinter import messagebox

# Store cart items
cart = []

# Add item to receipt
def add_item():
    name = item_entry.get()
    price = price_entry.get()
    qty = qty_entry.get()

    if name == "" or price == "" or qty == "":
        messagebox.showwarning("Input Error", "Please fill all fields")
        return

    price = float(price)
    qty = int(qty)

    total = price * qty
    cart.append(total)

    receipt.insert(tk.END, f"{name}  x{qty}  =  ${total}\n")

    update_total()

    item_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)
    qty_entry.delete(0, tk.END)

# Update total price
def update_total():
    total = sum(cart)
    total_label.config(text=f"Total: ${total}")

# Clear sale
def clear_sale():
    cart.clear()
    receipt.delete(1.0, tk.END)
    total_label.config(text="Total: $0")

# Print receipt
def print_receipt():
    content = receipt.get(1.0, tk.END)

    if content.strip() == "":
        messagebox.showwarning("Print Error", "Receipt is empty")
        return

    print("------ RECEIPT ------")
    print(content)
    print(total_label.cget("text"))
    print("---------------------")

# Window
root = tk.Tk()
root.title("Simple POS System")
root.geometry("400x500")

# Item name
tk.Label(root, text="Item Name").pack()
item_entry = tk.Entry(root)
item_entry.pack()

# Price
tk.Label(root, text="Price").pack()
price_entry = tk.Entry(root)
price_entry.pack()

# Quantity
tk.Label(root, text="Quantity").pack()
qty_entry = tk.Entry(root)
qty_entry.pack()

# Buttons
tk.Button(root, text="Add Item", command=add_item).pack(pady=5)
tk.Button(root, text="Clear Sale", command=clear_sale).pack(pady=5)
tk.Button(root, text="Print Receipt", command=print_receipt).pack(pady=5)

# Receipt display
tk.Label(root, text="Receipt").pack()

receipt = tk.Text(root, height=15, width=40)
receipt.pack()

# Total label
total_label = tk.Label(root, text="Total: $0", font=("Arial", 14))
total_label.pack(pady=10)

# Run window
root.mainloop()