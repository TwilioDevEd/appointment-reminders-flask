from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, DateTime, String

Base = declarative_base()

class Appointment(Base):
    __tablename__ = 'appointments'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    phone_number = Column(String(50), nullable=False)
    delta = Column(Integer, nullable=False)
    time = Column(DateTime, nullable=False)
    timezone = Column(String(50), nullable=False)

    def __init__(self, name, phone_number, delta, time, timezone):
        self.name = name
        self.phone_number = phone_number
        self.delta = delta
        self.time = time
        self.timezone = timezone

    def __repr__(self):
        return '<Appointment %r>' % self.name
