from pydantic import BaseModel, EmailStr
from datetime import datetime

class FitnessClassCreate(BaseModel):
    name: str
    dateTime: datetime
    instructor: str
    availableSlots: int

class FitnessClassOut(BaseModel):
    id: int
    name: str
    dateTime: datetime
    instructor: str
    availableSlots: int

    class Config:
        from_attributes = True  # Pydantic v2 compliant

class BookingCreate(BaseModel):
    class_id: int
    client_name: str
    client_email: EmailStr

class BookingOut(BaseModel):
    id: int
    class_id: int
    client_name: str
    client_email: EmailStr

    class Config:
        from_attributes = True  
