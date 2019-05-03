import datetime

from base_test import BaseTest
from models.appointment import Appointment


class AppointmentTest(BaseTest):

    def test_index(self):
        response = self.test_client.get('/')
        assert b"There are no appointment reminders scheduled" in response.data

    def test_new_appointment(self):
        params = {
            'name': 'Mr Praline',
            'phone_number': '+12025550170',
            'delta': '15',
            'time': '07-28-2015 12:24pm',
            'timezone': 'US/Pacific'
        }
        self.test_client.post('/appointment', data=params)

        response = self.test_client.get('/')
        assert b"Mr Praline" in response.data
        assert b"+12025550170" in response.data
        assert b"2015-07-28 19:24:00" in response.data
        assert b"US/Pacific" in response.data

    def test_new_appointment_fail(self):
        params = {}
        response = self.test_client.post('/appointment', data=params)
        self.assertEqual(response.status_code, 400)

    def test_new_appointment_empty(self):
        response = self.test_client.get('/appointment/new')
        self.assertEqual(response.status_code, 200)

    def test_delete_appointment(self):
        params = {
            'name': 'Mr Praline',
            'phone_number': '+12025550170',
            'delta': '15',
            'time': '07-28-2015 12:24pm',
            'timezone': 'US/Pacific'
        }
        self.test_client.post('/appointment', data=params)
        appt = self.db.session.query(Appointment).one()

        self.test_client.post('/appointment/{0}/delete'.format(str(appt.id)))
        all_appts = self.db.session.query(Appointment).all()

        self.assertEqual(all_appts, [])

    def test_instance(self):
        params = {
            'name': 'Mr Praline',
            'phone_number': '+12025550170',
            'delta': '15',
            'time': datetime.datetime(2015, 7, 28, 12, 24),
            'timezone': 'US/Pacific'
        }
        appt = Appointment(**params)
        self.assertEqual(repr(appt), "<Appointment 'Mr Praline'>")
