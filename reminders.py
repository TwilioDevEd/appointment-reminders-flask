from application import handlers, Application
import dotenv
import os

dotenv.load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))
app = Application(handlers, os.environ, debug=True)
db = app.db
celery = app.celery()

import tasks
