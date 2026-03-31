from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from bson.objectid import ObjectId
from pydantic import BaseModel

# Connect to MongoDB
client = MongoClient("mongodb+srv://selorm:sD6CxbirGD5s5pLV@cluster0.dxelfwg.mongodb.net/?appName=Cluster0")
db = client["UrbanPharmacy"]
medicines_collection = db["Medicines"]

app = FastAPI(title="Urban Pharmacy API")

# Pydantic model for medicine
class Medicine(BaseModel):
    medicine_id: str
    name: str
    category: str
    stock: int
    price: float
    
    
    
@app.get("/medicines")
def get_medicines():
    medicines = list(medicines_collection.find({}, {"_id": 0}))
    return medicines

@app.get("/medicines/{medicine_id}")
def get_medicine(medicine_id: str):
    medicine = medicines_collection.find_one({"medicine_id": medicine_id}, {"_id": 0})
    if medicine:
        return medicine
    raise HTTPException(status_code=404, detail="Medicine not found")

@app.post("/medicines")
def add_medicine(med: Medicine):
    if medicines_collection.find_one({"medicine_id": med.medicine_id}):
        raise HTTPException(status_code=400, detail="Medicine ID already exists")
    medicines_collection.insert_one(med.dict())
    return {"message": "Medicine added successfully"}

@app.put("/medicines/{medicine_id}")
def update_medicine(medicine_id: str, med: Medicine):
    result = medicines_collection.update_one(
        {"medicine_id": medicine_id},
        {"$set": med.dict()}
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Medicine not found")
    return {"message": "Medicine updated successfully"}

@app.delete("/medicines/{medicine_id}")
def delete_medicine(medicine_id: str):
    result = medicines_collection.delete_one({"medicine_id": medicine_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Medicine not found")
    return {"message": "Medicine deleted successfully"}


#uvicorn main:app --reload