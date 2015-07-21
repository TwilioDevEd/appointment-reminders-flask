from flask.views import MethodView
from datetime import datetime


class AppointmentResource(MethodView):

    def get(self):
        return "something"
