import flask
import flask.ext.sqlalchemy
import views.appointment
import os
from config.database import DatabaseConfiguration

class Route(object):
    def __init__(self, url, route_name, resource):
        self.url = url
        self.route_name = route_name
        self.resource = resource

handlers = [
    Route('/appointment', 'appointment.index', views.appointment.AppointmentResource),
    Route('/appointment/<int:id>/', 'appointment.delete', views.appointment.AppointmentResource),
    Route('/appointment/new', 'appointment.new', views.appointment.AppointmentFormResource)
]

class Application(object):
    def __init__(self, routes):
        self.flask_app = flask.Flask(__name__)
        self.db = flask.ext.sqlalchemy.SQLAlchemy(self.flask_app)
        self.flask_app.config['SQLALCHEMY_DATABASE_URI'] = self._connection_string()
        self.routes = routes

    def start_app(self):
        self.flask_app.secret_key = os.environ.get('SECRET_KEY')

        for route in self.routes:
            app_view = route.resource.as_view(route.route_name, self.db)
            self.flask_app.add_url_rule(route.url, view_func=app_view)
        self.flask_app.run(debug=True)

    def _connection_string(self):
        return DatabaseConfiguration(os.environ).connection_string()
