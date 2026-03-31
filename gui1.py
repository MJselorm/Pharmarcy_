import customtkinter as ctk
from tkinter import ttk, messagebox
from pymongo import MongoClient

# Appearance
ctk.set_appearance_mode("dark")  # dark mode 😎
ctk.set_default_color_theme("blue")

# MongoDB
client = MongoClient("#enter your link")
db = client["UrbanPharmacy"]
medicines = db["Medicines"]

# ---------------- FUNCTIONS ---------------- #

def clear_fields():
    entry_id.delete(0, "end")
    entry_name.delete(0, "end")
    entry_category.delete(0, "end")
    entry_price.delete(0, "end")
    entry_stock.delete(0, "end")

def refresh_table():
    for row in tree.get_children():
        tree.delete(row)

    for med in medicines.find():
        tree.insert("", "end", values=(
            med.get("medicine_id"),
            med.get("name"),
            med.get("category"),
            med.get("price"),
            med.get("stock")
        ))

def add_medicine():
    try:
        med = {
            "medicine_id": entry_id.get(),
            "name": entry_name.get(),
            "category": entry_category.get(),
            "price": float(entry_price.get()),
            "stock": int(entry_stock.get())
        }

        medicines.insert_one(med)
        refresh_table()
        clear_fields()
    except:
        messagebox.showerror("Error", "Invalid input")

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
        messagebox.showerror("Error", "Select a record")
        return

    medicines.delete_one({"medicine_id": med_id})
    refresh_table()
    clear_fields()

# ---------------- UI ---------------- #

app = ctk.CTk()
app.title("💊 Urban Pharmacy System")
app.geometry("950x600")

# Title
title = ctk.CTkLabel(app, text="Pharmacy Dashboard",
                     font=("Arial", 24, "bold"))
title.pack(pady=15)

# -------- FORM -------- #
form_frame = ctk.CTkFrame(app)
form_frame.pack(pady=10, padx=20, fill="x")

entry_id = ctk.CTkEntry(form_frame, placeholder_text="Medicine ID")
entry_id.grid(row=0, column=0, padx=10, pady=10)

entry_name = ctk.CTkEntry(form_frame, placeholder_text="Name")
entry_name.grid(row=0, column=1, padx=10, pady=10)

entry_category = ctk.CTkEntry(form_frame, placeholder_text="Category")
entry_category.grid(row=0, column=2, padx=10, pady=10)

entry_price = ctk.CTkEntry(form_frame, placeholder_text="Price")
entry_price.grid(row=1, column=0, padx=10, pady=10)

entry_stock = ctk.CTkEntry(form_frame, placeholder_text="Stock")
entry_stock.grid(row=1, column=1, padx=10, pady=10)

# -------- BUTTONS -------- #
btn_frame = ctk.CTkFrame(app)
btn_frame.pack(pady=10)

ctk.CTkButton(btn_frame, text="➕ Add", command=add_medicine).grid(row=0, column=0, padx=10)
ctk.CTkButton(btn_frame, text="✏️ Update", command=update_medicine).grid(row=0, column=1, padx=10)
ctk.CTkButton(btn_frame, text="❌ Delete", command=delete_medicine).grid(row=0, column=2, padx=10)
ctk.CTkButton(btn_frame, text="🧹 Clear", command=clear_fields).grid(row=0, column=3, padx=10)

# -------- TABLE -------- #
table_frame = ctk.CTkFrame(app)
table_frame.pack(pady=20, padx=20, fill="both", expand=True)

tree = ttk.Treeview(table_frame,
                    columns=("ID", "Name", "Category", "Price", "Stock"),
                    show="headings")

for col in ("ID", "Name", "Category", "Price", "Stock"):
    tree.heading(col, text=col)
    tree.column(col, anchor="center")

tree.pack(fill="both", expand=True)

tree.bind("<ButtonRelease-1>", select_record)

# Load data
refresh_table()

app.mainloop()
