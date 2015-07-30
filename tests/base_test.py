import unittest
from models.appointment import Appointment


class BaseTest(unittest.TestCase):
    def setUp(self):
        from reminders import app, db
        self.app = app
        self.db = db
        self.celery = app.celery()
        self.test_client = app.flask_app.test_client()
        self.app.flask_app.config['WTF_CSRF_ENABLED'] = False

    def tearDown(self):
        self.db.session.query(Appointment).delete()
        self.db.session.commit()
        self.celery.control.purge()
        self.celery.conf.CELERY_ALWAYS_EAGER = False
