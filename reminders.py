from flask import Flask

from config import config_classes
from database import db, migrate

from views import init_views


app = Flask(__name__, instance_relative_config=True)

# load the instance config, if it exists, when not testing
env = app.config.get("ENV", "production")
app.config.from_object(config_classes[env])

db.init_app(app)
migrate.init_app(app, db)

import tasks  # noqa E402
import models  # noqa E402

init_views(app)
