// Switch to (or create) the UrbanPharmacy database
use UrbanPharmacy

// Create Medicines collection
db.createCollection("Medicines")

// Insert a single medicine document
db.Medicines.insertOne({
  medicine_id: "M1",
  name: "Paracetamol",
  category: "Pain Relief",
  stock: 30,
  price: 15
})

// Insert multiple medicines at once
db.Medicines.insertMany([
  { medicine_id: "M2", name: "Amoxicillin", category: "Antibiotic", price: 40, stock: 100 },
  { medicine_id: "M3", name: "Vitamin C", category: "Supplement", price: 20, stock: 30 },
  { medicine_id: "M4", name: "Cough Syrup", category: "Cold & Flu", price: 25, stock: 45 }
])

// Retrieve all medicines
db.Medicines.find({})

// Find medicines in Pain Relief category
db.Medicines.find({ category: "Pain Relief" })

// Find medicines with price greater than 20
db.Medicines.find({ price: { $gt: 20 } })

// Find medicines with price less than 30
db.Medicines.find({ price: { $lt: 30 } })

// Find medicines with price equal to 40
db.Medicines.find({ price: { $eq: 40 } })

// Find medicines in specific categories using $in
db.Medicines.find({ category: { $in: ["Antibiotic"] } })

// Find medicines where category contains "flu" (case-insensitive)
db.Medicines.find({ category: { $regex: "flu", $options: "i" } })

// Sort all medicines (default order)
db.Medicines.find({}).sort()

// Sort medicines by price in ascending order
db.Medicines.find({}).sort({ price: 1 })

// Sort by price and limit results to 3
db.Medicines.find({}).sort({ price: 1 }).limit(3)

// Update a specific medicine (change name and stock)
db.Medicines.updateOne(
  { medicine_id: "M1" },
  { $set: { name: "Paracetamol Tablets", stock: 25 } }
)

// Find a specific medicine by ID
db.Medicines.find({ medicine_id: "M2" })

// Delete a medicine
db.Medicines.deleteOne({ medicine_id: "M4" })

// Re-insert the deleted medicine
db.Medicines.insertOne({
  medicine_id: "M4",
  name: "Cough Syrup",
  category: "Cold & Flu",
  price: 25,
  stock: 45
})

// Aggregate: calculate total stock per category
db.Medicines.aggregate([
  {
    $group: {
      _id: "$category",
      totalStock: { $sum: "$stock" }
    }
  }
])

// Insert more medicines
db.Medicines.insertMany([
  { medicine_id: "M6", name: "Insulin", category: "Hormones", price: 60, stock: 10 },
  { medicine_id: "M7", name: "Ibuprofen", category: "Pain Relief", price: 18, stock: 60 },
  { medicine_id: "M8", name: "Multivitamins", category: "Supplement", price: 35, stock: 150 },
  { medicine_id: "M9", name: "Antiseptic", category: "First Aid", price: 22, stock: 17 }
])

// Perform multiple operations in one bulk write
db.Medicines.bulkWrite([

  // Insert a new medicine
  {
    insertOne: {
      document: {
        medicine_id: "M10",
        name: "ORS Solution",
        category: "Rehydration",
        price: 12,
        stock: 100
      }
    }
  },

  // Increase stock of M1 by 70
  {
    updateOne: {
      filter: { medicine_id: "M1" },
      update: { $inc: { stock: 70 } }
    }
  },

  // Delete a medicine (Vitamin C)
  {
    deleteOne: {
      filter: { medicine_id: "M3" }
    }
  }
])

// Create Suppliers collection
db.createCollection("Suppliers")

// Insert multiple suppliers
db.Suppliers.insertMany([
  { supplier_id: "S1", name: "PharmaPlus", contact: "123-456-7890" },
  { supplier_id: "S002", name: "Health Distributors", contact: "987-654-3210" }
])

// Delete incorrect supplier entry
db.Suppliers.deleteOne({ supplier_id: "S002" })

// Insert corrected supplier
db.Suppliers.insertOne({
  supplier_id: "S2",
  name: "Health Distributors",
  contact: "987-654-3210"
})

// Insert another supplier
db.Suppliers.insertOne({
  supplier_id: "S3",
  name: "MediSupply",
  contact: "373-083-3572"
})

// Create index on category for faster queries
db.Medicines.createIndex({ category: 1 })

// Create text index on name for text search
db.Medicines.createIndex({ name: "text" })

// Find medicines in Pain Relief category
db.Medicines.find({ category: "Pain Relief" })

// Use cursor to iterate through results
var cursor = db.Medicines.find({ category: "Pain Relief" })

// Print name and price of each medicine
cursor.forEach(doc => print(doc.name, doc.price))