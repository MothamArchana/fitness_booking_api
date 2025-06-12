from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from . import models, schemas

def create_class(db: Session, fitness_class: schemas.FitnessClassCreate):
    new_class = models.FitnessClass(**fitness_class.dict())
    db.add(new_class)
    db.commit()
    db.refresh(new_class)
    return new_class

def get_upcoming_classes(db: Session):
    return db.query(models.FitnessClass).all()

def create_booking(db: Session, booking: schemas.BookingCreate):
    fitness_class = db.query(models.FitnessClass).filter(models.FitnessClass.id == booking.class_id).first()

    if not fitness_class:
        raise ValueError("Fitness class not found")

    if fitness_class.availableSlots <= 0:
        raise ValueError("No slots available")

    new_booking = models.Booking(
        class_id=booking.class_id,
        client_name=booking.client_name,
        client_email=booking.client_email
    )

    fitness_class.availableSlots -= 1
    db.add(new_booking)
    db.commit()
    db.refresh(new_booking)
    return new_booking

def get_bookings_by_email(db: Session, email: str):
    return db.query(models.Booking).filter(models.Booking.client_email == email).all()