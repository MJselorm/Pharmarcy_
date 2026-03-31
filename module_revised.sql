// ==============================
// DATABASE PROJECT: URBAN PHARMACY
// ==============================

// 10. CONNECTING TO MONGODB
use UrbanPharmacy

// 7. COLLECTIONS AND DOCUMENTS
// Create Medicines collection
db.createCollection("Medicines")

// Insert initial medicine (document structure design)
db.Medicines.insertOne({
  medicine_id: "M1",
  name: "Paracetamol",
  category: "Pain Relief",
  stock: 30,
  price: 15
})

// 1. INSERTION (multiple documents)
db.Medicines.insertMany([
  { medicine_id: "M2", name: "Amoxicillin", category: "Antibiotic", price: 40, stock: 100 },
  { medicine_id: "M3", name: "Vitamin C", category: "Supplement", price: 20, stock: 30 },
  { medicine_id: "M4", name: "Cough Syrup", category: "Cold & Flu", price: 25, stock: 45 }
])

// ==============================
// 2. DIFFERENT APPROACHES OF FINDING DOCUMENTS
// ==============================

// Get all medicines
db.Medicines.find({})

// Filter by category
db.Medicines.find({ category: "Pain Relief" })

// ==============================
// 3. OPERATORS AND COMPLEX QUERIES
// ==============================

// Greater than
db.Medicines.find({ price: { $gt: 20 } })

// Less than
db.Medicines.find({ price: { $lt: 30 } })

// Equal
db.Medicines.find({ price: { $eq: 40 } })

// IN operator
db.Medicines.find({ category: { $in: ["Antibiotic"] } })

// REGEX search
db.Medicines.find({ category: { $regex: "flu", $options: "i" } })

// ==============================
// 5. SORTING AND LIMITING
// ==============================

// Sort ascending
db.Medicines.find({}).sort({ price: 1 })

// Limit results
db.Medicines.find({}).sort({ price: 1 }).limit(3)

// ==============================
// 1. UPDATING DOCUMENTS
// ==============================

db.Medicines.updateOne(
  { medicine_id: "M1" },
  { $set: { name: "Paracetamol Tablets", stock: 25 } }
)

// ==============================
// 1. DELETING DOCUMENTS
// ==============================

db.Medicines.deleteOne({ medicine_id: "M4" })

// Reinsert deleted document
db.Medicines.insertOne({
  medicine_id: "M4",
  name: "Cough Syrup",
  category: "Cold & Flu",
  price: 25,
  stock: 45
})

// ==============================
// 4. AGGREGATION
// ==============================

// Total stock per category
db.Medicines.aggregate([
  {
    $group: {
      _id: "$category",
      totalStock: { $sum: "$stock" }
    }
  }
])

// Average price per category
db.Medicines.aggregate([
  {
    $group: {
      _id: "$category",
      avgPrice: { $avg: "$price" }
    }
  }
])

// ==============================
// 6. BULK WRITING
// ==============================

db.Medicines.bulkWrite([

  // Insert
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

  // Update
  {
    updateOne: {
      filter: { medicine_id: "M1" },
      update: { $inc: { stock: 70 } }
    }
  },

  // Delete
  {
    deleteOne: {
      filter: { medicine_id: "M3" }
    }
  }
])

// ==============================
// 7. ADDITIONAL COLLECTION (SUPPLIERS)
// ==============================

db.createCollection("Suppliers")

db.Suppliers.insertMany([
  { supplier_id: "S1", name: "PharmaPlus", contact: "123-456-7890" },
  { supplier_id: "S2", name: "Health Distributors", contact: "987-654-3210" }
])

// ==============================
// 8. INDEXING
// ==============================

// Improve query performance
db.Medicines.createIndex({ category: 1 })

// Text search index
db.Medicines.createIndex({ name: "text" })

// ==============================
// 9. CURSOR AND FETCHING
// ==============================

var cursor = db.Medicines.find({ category: "Pain Relief" })

cursor.forEach(doc => print(doc.name, doc.price))

// ==============================
// 13. PAGINATION
// ==============================

// Skip first 2, limit 3
db.Medicines.find().skip(2).limit(3)