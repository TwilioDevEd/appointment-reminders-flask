import six
import datetime

from base_test import BaseTest
from models.appointment import Appointment
from tasks import send_sms_reminder

if six.PY3:
    from unittest.mock import patch
else:
    from mock import patch


class TasksTest(BaseTest):
    params = {
        'name': 'Mr Praline',
        'phone_number': '+12025550170',
        'delta': '15',
        'time': datetime.datetime(2015, 7, 28, 12, 24),
        'timezone': 'US/Pacific'
    }

    def setUp(self):
        super(TasksTest, self).setUp()
        self.celery.conf.CELERY_ALWAYS_EAGER = True
        self.newAppt = Appointment(**self.params)

    def tearDown(self):
        super(TasksTest, self).tearDown()
        self.celery.conf.CELERY_ALWAYS_EAGER = False

    def test_send_sms_reminder_valid(self):
        self.db.session.add(self.newAppt)
        self.db.session.commit()

        with patch('twilio.rest.api.v2010.account.message.MessageList.create') as create_mock:  # noqa: E501
            send_sms_reminder(self.newAppt.id)
            self.assertTrue(create_mock.called)

    def test_delete_appointment(self):
        self.db.session.add(self.newAppt)
        self.db.session.commit()

        idToDelete = self.newAppt.id

        self.db.session.delete(self.newAppt)
        self.db.session.commit()

        with patch('twilio.rest.api.v2010.account.message.MessageList.create') as create_mock:  # noqa: E501
            send_sms_reminder(idToDelete)
            self.assertFalse(create_mock.called)
