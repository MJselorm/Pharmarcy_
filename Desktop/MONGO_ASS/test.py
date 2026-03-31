from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["UrbanPharmacy"]

medicines = db["Medicines"]

for medicine in medicines.find({"category": "Pain Relief"}):
    print(medicine["name"], medicine["price"])