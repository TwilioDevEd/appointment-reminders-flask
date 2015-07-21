import flask
import dotenv
import config.database
import flask.ext.sqlalchemy
from views.appointment import AppointmentResource

class Route(object):
    def __init__(self, url, resource):
        self.url = url
        self.resource = resource

class Application(object):
    def __init__(self, routes):
        self.app = flask.Flask(__name__)
        self.app.config['SQL_ALCHEMY_DATABASE_URI'] = self._connection_string()
        self.db = flask.ext.sqlalchemy.SQLAlchemy(self.app)
        self.routes = routes

    def start_app(self):
        for route in self.routes:
           self.app.add_url_rule(route.url, view_func=route.resource.as_view(''))
        self.app.run()

    def _connection_string(self):
        return config.database.DatabaseConfiguration().connection_string()

handlers = [
    Route('/appointment', AppointmentResource)
]

reminders_application = Application(handlers)
db = reminders_application.db
