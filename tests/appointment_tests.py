from datetime import datetime

from unittest.mock import patch, Mock

from database import db
from models.appointment import Appointment

from .base import BaseTest


class AppointmentTest(BaseTest):
    def test_index(self):
        response = self.client.get('/')
        self.assertIn(b"There are no appointment reminders scheduled", response.data)

    def test_new_appointment(self):
        params = {
            'name': 'Mr Praline',
            'phone_number': '+12025550170',
            'delta': '15',
            'time': '07-28-2015 12:24pm',
            'timezone': 'US/Pacific',
        }
        with patch('tasks.send_sms_reminder') as fake_sender:
            fake_sender.apply_async = Mock()
            self.client.post('/appointment', data=params)
            fake_sender.apply_async.assert_called_once()

        response = self.client.get('/')
        self.assertIn(b"Mr Praline", response.data)
        self.assertIn(b"+12025550170", response.data)
        self.assertIn(b"2015-07-28 19:24:00", response.data)
        self.assertIn(b"US/Pacific", response.data)

    def test_new_appointment_fail(self):
        params = {}
        response = self.client.post('/appointment', data=params)
        self.assertEqual(response.status_code, 400)

    def test_new_appointment_empty(self):
        response = self.client.get('/appointment/new')
        self.assertEqual(response.status_code, 200)

    def test_delete_appointment(self):
        appt = Appointment(
            name='Mr Praline',
            phone_number='+12025550170',
            delta=15,
            time=datetime(2015, 7, 28, 12, 24),
            timezone='US/Pacific',
        )
        db.session.add(appt)
        db.session.commit()

        self.client.post('/appointment/{0}/delete'.format(str(appt.id)))
        all_appts = db.session.query(Appointment).all()

        self.assertEqual(all_appts, [])

    def test_instance(self):
        params = {
            'name': 'Mr Praline',
            'phone_number': '+12025550170',
            'delta': '15',
            'time': datetime(2015, 7, 28, 12, 24),
            'timezone': 'US/Pacific',
        }
        appt = Appointment(**params)
        self.assertEqual(repr(appt), "<Appointment 'Mr Praline'>")
