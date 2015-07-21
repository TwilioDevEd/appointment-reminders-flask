from flask.views import MethodView
from models.appointment import Appointment
import datetime

class AppointmentResource(MethodView):
    def __init__(self, db):
        self.db = db

    def get(self):
        appt = Appointment('A name', '+54853435', 120, datetime.datetime.now(), 'Americas/Guayaquil')
        self.db.session.add(appt)
        self.db.session.commit()
        return "something"
