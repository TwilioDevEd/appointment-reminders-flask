from flask.views import MethodView
from flask import render_template
from models.appointment import Appointment
from sqlalchemy import select
from forms.new_appointment import NewAppointmentForm
import os
import datetime

class AppointmentResource(MethodView):
    def __init__(self, db):
        self.db = db

    def get(self):
        all_appointments = self.db.session.query(Appointment).all()
        return render_template('appointments/index.html', appointments=all_appointments)

class AppointmentFormResource(MethodView):
    def __init__(self, db):
        self.db = db

    def get(self):
        form = NewAppointmentForm(secret_key=os.environ.get('SECRET_KEY'))
        return render_template('appointments/new.html', form=form)
