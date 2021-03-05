from database import db

import arrow


class Appointment(db.Model):
    __tablename__ = 'appointments'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.String(50), nullable=False)
    delta = db.Column(db.Integer, nullable=False)
    time = db.Column(db.DateTime, nullable=False)
    timezone = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Appointment %r>' % self.name

    def get_notification_time(self):
        appointment_time = arrow.get(self.time)
        reminder_time = appointment_time.shift(minutes=-self.delta)
        return reminder_time
