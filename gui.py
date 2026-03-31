import tkinter as tk
from tkinter import ttk, messagebox
from pymongo import MongoClient

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["UrbanPharmacy"]
medicines = db["Medicines"]

# ---------------- FUNCTIONS ---------------- #

def clear_fields():
    entry_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_category.delete(0, tk.END)
    entry_price.delete(0, tk.END)
    entry_stock.delete(0, tk.END)

def refresh_table():
    for row in tree.get_children():
        tree.delete(row)

    for med in medicines.find():
        tree.insert("", tk.END, values=(
            med.get("medicine_id"),
            med.get("name"),
            med.get("category"),
            med.get("price"),
            med.get("stock")
        ))

def add_medicine():
    med = {
        "medicine_id": entry_id.get(),
        "name": entry_name.get(),
        "category": entry_category.get(),
        "price": float(entry_price.get()),
        "stock": int(entry_stock.get())
    }

    if med["medicine_id"] == "":
        messagebox.showerror("Error", "ID is required")
        return

    medicines.insert_one(med)
    refresh_table()
    clear_fields()

def select_record(event):
    selected = tree.focus()
    values = tree.item(selected, "values")

    if values:
        clear_fields()
        entry_id.insert(0, values[0])
        entry_name.insert(0, values[1])
        entry_category.insert(0, values[2])
        entry_price.insert(0, values[3])
        entry_stock.insert(0, values[4])

def update_medicine():
    med_id = entry_id.get()

    medicines.update_one(
        {"medicine_id": med_id},
        {"$set": {
            "name": entry_name.get(),
            "category": entry_category.get(),
            "price": float(entry_price.get()),
            "stock": int(entry_stock.get())
        }}
    )

    refresh_table()
    clear_fields()

def delete_medicine():
    med_id = entry_id.get()

    if med_id == "":
        messagebox.showerror("Error", "Select a record to delete")
        return

    medicines.delete_one({"medicine_id": med_id})
    refresh_table()
    clear_fields()

# ---------------- GUI ---------------- #

root = tk.Tk()
root.title("Urban Pharmacy Management System")
root.geometry("900x600")
root.configure(bg="#f4f6f7")

title = tk.Label(root, text="Pharmacy CRUD Dashboard",
                 font=("Arial", 18, "bold"), bg="#f4f6f7")
title.pack(pady=10)

# -------- FORM -------- #
form_frame = tk.Frame(root, bg="#f4f6f7")
form_frame.pack(pady=10)

tk.Label(form_frame, text="ID").grid(row=0, column=0)
entry_id = tk.Entry(form_frame)
entry_id.grid(row=0, column=1)

tk.Label(form_frame, text="Name").grid(row=1, column=0)
entry_name = tk.Entry(form_frame)
entry_name.grid(row=1, column=1)

tk.Label(form_frame, text="Category").grid(row=2, column=0)
entry_category = tk.Entry(form_frame)
entry_category.grid(row=2, column=1)

tk.Label(form_frame, text="Price").grid(row=0, column=2)
entry_price = tk.Entry(form_frame)
entry_price.grid(row=0, column=3)

tk.Label(form_frame, text="Stock").grid(row=1, column=2)
entry_stock = tk.Entry(form_frame)
entry_stock.grid(row=1, column=3)

# -------- BUTTONS -------- #
btn_frame = tk.Frame(root, bg="#f4f6f7")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Add", width=15, bg="#2ecc71",
          command=add_medicine).grid(row=0, column=0, padx=10)

tk.Button(btn_frame, text="Update", width=15, bg="#3498db",
          command=update_medicine).grid(row=0, column=1, padx=10)

tk.Button(btn_frame, text="Delete", width=15, bg="#e74c3c",
          command=delete_medicine).grid(row=0, column=2, padx=10)

tk.Button(btn_frame, text="Clear", width=15,
          command=clear_fields).grid(row=0, column=3, padx=10)

# -------- TABLE -------- #
table_frame = tk.Frame(root)
table_frame.pack(pady=20)

scroll_y = tk.Scrollbar(table_frame, orient=tk.VERTICAL)

tree = ttk.Treeview(table_frame,
                    columns=("ID", "Name", "Category", "Price", "Stock"),
                    yscrollcommand=scroll_y.set,
                    show="headings",
                    height=15)

scroll_y.config(command=tree.yview)
scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
tree.pack()

for col in ("ID", "Name", "Category", "Price", "Stock"):
    tree.heading(col, text=col)
    tree.column(col, width=120)

tree.bind("<ButtonRelease-1>", select_record)

# Style
style = ttk.Style()
style.configure("Treeview", rowheight=25)

# Load data initially
refresh_table()

root.mainloop()