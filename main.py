import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from app import models, schemas, crud
from app.database import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Fitness Booking API")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/classes", response_model=schemas.FitnessClassOut)
def create_class(fitness_class: schemas.FitnessClassCreate, db: Session = Depends(get_db)):
    return crud.create_class(db, fitness_class)

@app.get("/classes", response_model=list[schemas.FitnessClassOut])
def get_classes(db: Session = Depends(get_db)):
    return crud.get_upcoming_classes(db)

@app.post("/book", response_model=schemas.BookingOut)
def book_class(booking: schemas.BookingCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_booking(db, booking)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
