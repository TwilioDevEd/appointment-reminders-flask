import arrow

from celery import Celery
from sqlalchemy.orm.exc import NoResultFound
from twilio.rest import Client

from reminders import db, app
from models.appointment import Appointment

twilio_account_sid = app.config['TWILIO_ACCOUNT_SID']
twilio_auth_token = app.config['TWILIO_AUTH_TOKEN']
twilio_number = app.config['TWILIO_NUMBER']
client = Client(twilio_account_sid, twilio_auth_token)

celery = Celery(app.import_name)
celery.conf.update(app.config)


class ContextTask(celery.Task):
    def __call__(self, *args, **kwargs):
        with app.app_context():
            return self.run(*args, **kwargs)


celery.Task = ContextTask


@celery.task()
def send_sms_reminder(appointment_id):
    try:
        appointment = db.session.query(Appointment).filter_by(id=appointment_id).one()
    except NoResultFound:
        return

    time = arrow.get(appointment.time).to(appointment.timezone)
    body = "Hello {0}. You have an appointment at {1}!".format(
        appointment.name, time.format('h:mm a')
    )
    to = appointment.phone_number
    client.messages.create(to, from_=twilio_number, body=body)
