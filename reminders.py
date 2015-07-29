from application import handlers, Application
import os

app = Application(handlers, os.environ, debug=True)
db = app.db
celery = app.celery()

import tasks
