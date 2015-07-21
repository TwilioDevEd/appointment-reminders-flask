import sys
import os
from application import db


class Appointment(db.Model):
    __tablename__ = 'appointments'

    appointment_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.String(50), nullable=False)
    delta = db.Column(db.Integer, nullable=False)
    time = db.Column(db.DateTime, nullable=False)
    timezone = db.Column(db.String(50), nullable=False)

    def __init__(self, name, phone_number, delta, time, timezone):
        self.name = name
        self.phone_number = phone_number
        self.delta = delta
        self.time = time
        self.timezone = timezone

    def __repr__(self):
        return '<Appointment %r>' % self.name
