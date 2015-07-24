import flask
import flask.ext.sqlalchemy
import views.appointment
import os
from config.database import DatabaseConfiguration
from middleware import HTTPMethodOverrideMiddleware

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



from werkzeug import Request

class MethodRewriteMiddleware(object):
    def __init__(self, app, input_name='_method'):
        self.app = app
        self.input_name = input_name

    def __call__(self, environ, start_response):
        request = Request(environ)

        if self.input_name in request.form:
            method = request.form[self.input_name].upper()

            if method in ['GET', 'POST', 'PUT', 'DELETE']:
                environ['REQUEST_METHOD'] = method

        return self.app(environ, start_response)


class Application(object):
    def __init__(self, routes):
        self.flask_app = flask.Flask(__name__)
        self.db = flask.ext.sqlalchemy.SQLAlchemy(self.flask_app)
        self.flask_app.config['SQLALCHEMY_DATABASE_URI'] = self._connection_string()
        self.flask_app.wsgi_app = MethodRewriteMiddleware(self.flask_app.wsgi_app)
        self.routes = routes

    def start_app(self):
        self.flask_app.secret_key = os.environ.get('SECRET_KEY')

        for route in self.routes:
            app_view = route.resource.as_view(route.route_name, self.db)
            self.flask_app.add_url_rule(route.url, view_func=app_view)
        self.flask_app.run(debug=True)

    def _connection_string(self):
        return DatabaseConfiguration(os.environ).connection_string()
