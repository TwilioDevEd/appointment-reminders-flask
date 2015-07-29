from reminders import celery, db, app
from models.appointment import Appointment
from sqlalchemy.orm.exc import NoResultFound
from twilio.rest import TwilioRestClient
import arrow

twilio_account_sid = app.flask_app.config['TWILIO_ACCOUNT_SID']
twilio_auth_token = app.flask_app.config['TWILIO_AUTH_TOKEN']
twilio_number = app.flask_app.config['TWILIO_NUMBER']

client = TwilioRestClient(account=twilio_account_sid, token=twilio_auth_token)


@celery.task()
def send_sms_reminder(appointment_id):
    try:
        appointment = db.session.query(
            Appointment).filter_by(id=appointment_id).one()
    except NoResultFound:
        return

    time = arrow.get(appointment.time).to(appointment.timezone)
    body = "Hello {0}. You have an appointment at {1}!".format(
        appointment.name,
        time.format('h:mm a')
    )

    client.messages.create(
        body=body,
        to=appointment.phone_number,
        from_=twilio_number,
    )
