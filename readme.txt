# Fitness Booking API

A FastAPI-based web application for booking fitness classes like Yoga, Zumba, and HIIT. Uses SQLite for data storage and allows users to view and book available classes.

---

## Features

- View all fitness classes
- Book a class
- View all bookings
- Simple SQLite database
- Clean API endpoints

---

## Project Structure

fitness-booking-api/
│
├── app/
│ ├── main.py # FastAPI app code
│ └── models.py # Database models
│
├── seed.py # Preloads the database
├── fitness.db # SQLite database
├── requirements.txt # Python dependencies
├── README.md # Project instructions
└── venv/ # Python virtual environment (not uploaded)


---

## 🛠 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/MothamArchana/fitness_booking_api
cd fitness_booking_api

2. Create and Activate Virtual Environment

python -m venv venv
venv\Scripts\activate  # For Windows
# OR
source venv/bin/activate  # For macOS/Linux

3. Install Dependencies
pip install -r requirements.txt

4. Run Database Seeder
python seed.py

5. Start the API Server
uvicorn app.main:app --reload

6.API Endpoints
Method	Endpoint	Description
GET	/classes	List all available classes
POST	/book	        Book a class
GET	/bookings	View all bookings

Example: Booking a Class
curl -X POST http://127.0.0.1:8000/book \
-H "Content-Type: application/json" \
-d '{
  "class_id": 1,
  "client_name": "John Doe",
  "client_email": "john@example.com"
}'

Requirements
Python 3.8+
FastAPI
SQLite

Author
Archana Motham
GitHub: @MothamArchana


