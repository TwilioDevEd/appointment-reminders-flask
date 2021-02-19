import flask
from flask_migrate import Migrate

from flask_sqlalchemy import SQLAlchemy

from celery import Celery

from config import config_classes
from views.appointment import (
    AppointmentFormResource,
    AppointmentResourceCreate,
    AppointmentResourceDelete,
    AppointmentResourceIndex,
)


class Route(object):
    def __init__(self, url, route_name, resource):
        self.url = url
        self.route_name = route_name
        self.resource = resource


handlers = [
    Route('/', 'appointment.index', AppointmentResourceIndex),
    Route('/appointment', 'appointment.create', AppointmentResourceCreate),
    Route(
        '/appointment/<int:id>/delete', 'appointment.delete', AppointmentResourceDelete
    ),
    Route('/appointment/new', 'appointment.new', AppointmentFormResource),
]


class Application(object):
    def __init__(self, routes, environment):
        self.flask_app = flask.Flask(__name__)
        self.routes = routes
        self._configure_app(environment)
        self._set_routes()

    def celery(self):
        celery = Celery(
            self.flask_app.import_name, broker=self.flask_app.config['CELERY_BROKER_URL']
        )
        celery.conf.update(self.flask_app.config)

        TaskBase = celery.Task

        class ContextTask(TaskBase):
            abstract = True

            def __call__(self, *args, **kwargs):
                with self.flask_app.app_context():
                    return TaskBase.__call__(self, *args, **kwargs)

        celery.Task = ContextTask

        return celery

    def _set_routes(self):
        for route in self.routes:
            app_view = route.resource.as_view(route.route_name)
            self.flask_app.add_url_rule(route.url, view_func=app_view)

    def _configure_app(self, env):
        self.flask_app.config.from_object(config_classes[env])
        self.db = SQLAlchemy(self.flask_app)
        self.migrate = Migrate()
        self.migrate.init_app(self.flask_app, self.db)
