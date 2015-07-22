import flask
import dotenv
import flask.ext.sqlalchemy
import views.appointment
from config.database import DatabaseConfiguration

class Route(object):
    def __init__(self, url, resource):
        self.url = url
        self.resource = resource

handlers = [
    Route('/appointment', views.appointment.AppointmentResource)
]

class Application(object):
    def __init__(self, routes):
        self.flask_app = flask.Flask(__name__)
        self.db = flask.ext.sqlalchemy.SQLAlchemy(self.flask_app)
        self.flask_app.config['SQLALCHEMY_DATABASE_URI'] = self._connection_string()
        self.routes = routes

    def start_app(self):
        for route in self.routes:
           self.flask_app.add_url_rule(route.url, view_func=route.resource.as_view('', self.db))
        self.flask_app.run(debug=True)

    def _connection_string(self):
        return DatabaseConfiguration(os.environ).connection_string()
