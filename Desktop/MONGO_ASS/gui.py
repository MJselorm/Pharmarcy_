import tkinter as tk
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["UrbanPharmacy"]
medicines = db["Medicines"]

# Function to fetch and display data
def show_medicines():
    output.delete("1.0", tk.END)
    for medicine in medicines.find({"category": "Pain Relief"}):
        output.insert(tk.END, f"{medicine['name']} - {medicine['price']}\n")

# GUI setup
root = tk.Tk()
root.title("Pharmacy System")

btn = tk.Button(root, text="Show Pain Relief Medicines", command=show_medicines)
btn.pack()

output = tk.Text(root, height=10, width=40)
output.pack()

root.mainloop()