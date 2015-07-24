from flask.views import MethodView
from flask import render_template
from models.appointment import Appointment
from forms.new_appointment import NewAppointmentForm
from flask import request, flash, redirect, url_for

class AppointmentResource(MethodView):
    def __init__(self, db):
        self.db = db

    def post(self):
        print("We get to here")
        form = NewAppointmentForm(request.form)

        if form.validate():
            appt = Appointment(**form.data)
            self.db.session.add(appt)
            self.db.session.commit()

            return redirect(url_for('appointment.index'), code=303)
        else:
            return render_template('appointments/new.html', form=form), 400

    def delete(self, id):
        appt = self.db.session.query(Appointment).filter_by(id=id).one()
        self.db.session.delete(appt)
        self.db.session.commit()

        return redirect(url_for('appointment.index'), code=303)

    def get(self):
        all_appointments = self.db.session.query(Appointment).all()
        return render_template('appointments/index.html', appointments=all_appointments)

class AppointmentFormResource(MethodView):
    def __init__(self, db):
        self.db = db

    def get(self):
        form = NewAppointmentForm()
        return render_template('appointments/new.html', form=form)
