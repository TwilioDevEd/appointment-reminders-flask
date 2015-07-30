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
