from app.database import SessionLocal
from app import models
from datetime import datetime

# Sample fitness classes
classes = [
    {
        "name": "Yoga Flow",
        "dateTime": datetime(2025, 6, 15, 7, 0),
        "instructor": "John Doe",
        "availableSlots": 20
    },
    {
        "name": "Zumba Blast",
        "dateTime": datetime(2025, 6, 15, 9, 0),
        "instructor": "Jane Smith",
        "availableSlots": 25
    },
    {
        "name": "HIIT Burn",
        "dateTime": datetime(2025, 6, 15, 18, 0),
        "instructor": "Mike Tyson",
        "availableSlots": 15
    }
]

# Insert into DB
db = SessionLocal()
for cls in classes:
    fitness_class = models.FitnessClass(**cls)
    db.add(fitness_class)

db.commit()
db.close()

print("✅ Seed data inserted.")
