import datetime
from unittest.mock import patch

from database import db
from models.appointment import Appointment
from tasks import send_sms_reminder, celery

from .base import BaseTest


class TasksTest(BaseTest):
    params = {
        'name': 'Mr Praline',
        'phone_number': '+12025550170',
        'delta': '15',
        'time': datetime.datetime(2015, 7, 28, 12, 24),
        'timezone': 'US/Pacific',
    }

    def setUp(self):
        super(TasksTest, self).setUp()
        celery.conf.CELERY_ALWAYS_EAGER = True
        self.new_appointment = Appointment(**self.params)

    def tearDown(self):
        celery.conf.CELERY_ALWAYS_EAGER = False
        super(TasksTest, self).tearDown()

    def test_send_sms_reminder_valid(self):
        db.session.add(self.new_appointment)
        db.session.commit()

        with patch(
            'twilio.rest.api.v2010.account.message.MessageList.create'
        ) as create_mock:  # noqa: E501
            send_sms_reminder(self.new_appointment.id)
            self.assertTrue(create_mock.called)

    def test_delete_appointment(self):
        db.session.add(self.new_appointment)
        db.session.commit()

        id_to_delete = self.new_appointment.id

        db.session.delete(self.new_appointment)
        db.session.commit()

        with patch(
            'twilio.rest.api.v2010.account.message.MessageList.create'
        ) as create_mock:  # noqa: E501
            send_sms_reminder(id_to_delete)
            self.assertFalse(create_mock.called)
