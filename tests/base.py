from unittest import TestCase

from reminders import app, db


class BaseTest(TestCase):
    def setUp(self):
        self.client = app.test_client()
        app.app_context().push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
