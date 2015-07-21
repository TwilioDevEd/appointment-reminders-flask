from flask.views import MethodView

class AppointmentResource(MethodView):

    def get(self):
        return "something"
