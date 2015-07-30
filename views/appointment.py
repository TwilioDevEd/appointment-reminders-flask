from flask.views import MethodView
from flask import render_template
from models.appointment import Appointment
from forms.new_appointment import NewAppointmentForm
from flask import request, redirect, url_for
import reminders
import arrow


class AppointmentResourceDelete(MethodView):

    def post(self, id):
        appt = reminders.db.session.query(Appointment).filter_by(id=id).one()
        reminders.db.session.delete(appt)
        reminders.db.session.commit()

        return redirect(url_for('appointment.index'), code=303)


class AppointmentResourceCreate(MethodView):

    def post(self):
        form = NewAppointmentForm(request.form)

        if form.validate():
            from tasks import send_sms_reminder

            appt = Appointment(**form.data)
            appt.time = arrow.get(appt.time, appt.timezone).to('utc').naive

            reminders.db.session.add(appt)
            reminders.db.session.commit()
            send_sms_reminder.apply_async(
                args=[appt.id], eta=appt.get_notification_time())

            return redirect(url_for('appointment.index'), code=303)
        else:
            return render_template('appointments/new.html', form=form), 400


class AppointmentResourceIndex(MethodView):

    def get(self):
        all_appointments = reminders.db.session.query(Appointment).all()
        return render_template('appointments/index.html',
                               appointments=all_appointments)


class AppointmentFormResource(MethodView):

    def get(self):
        form = NewAppointmentForm()
        return render_template('appointments/new.html', form=form)
