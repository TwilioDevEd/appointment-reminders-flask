web: gunicorn reminders:app.flask_app --log-file -
worker: celery -A reminders.celery worker -l info