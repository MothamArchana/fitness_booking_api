from sqlalchemy import Column, Integer, String, DateTime
from .database import Base

class FitnessClass(Base):
    __tablename__ = "classes"  

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    dateTime = Column(DateTime, nullable=False)
    instructor = Column(String, nullable=False)
    availableSlots = Column(Integer, nullable=False)

class Booking(Base):
    __tablename__= "bookings"  
    id = Column(Integer, primary_key=True, index=True)
    class_id = Column(Integer, nullable=False)
    client_name = Column(String, nullable=False)
    client_email = Column(String, nullable=False)