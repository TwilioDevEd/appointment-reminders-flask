# Twilio's Appointment Reminders with Flask

[![Build Status](https://travis-ci.org/TwilioDevEd/appointment-reminders-flask.svg?branch=master)](https://travis-ci.org/TwilioDevEd/appointment-reminders-flask)

## Deploy to Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

After deploying make sure the worker is enabled under the application
dashboard. Otherwise the app won't be able to send SMS.

## Installing dependencies

This app runs on Python 2.7, 3.3, and 3.4.

It is recommended to use a [virtualenv](https://virtualenv.pypa.io/en/latest/)
together with
[virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/) to
manage the applications' dependencies. Assuming both are installed, the
application can be run as follows:

Create a virtualenv with virtualenvwrapper (using Python 3):
```
mkvirtualenv appointment-reminders-flask --python python3
```
Inside the cloned repo you can install the dependencies of the
application using:
```
pip install -r requirements.txt
```
## Database migrations

First, make sure [Postgres](http://www.postgresql.org/) is running on your system.

You'll need to set the environment variables specified in `.env.example`
to match your local configuration and `source` that file, or set the
environment variables manually.

The database schema is managed using [Alembic](https://github.com/zzzeek/alembic).

Migrate the database:
```
alembic upgrade +1
```
## Start the celery worker
First you'll need to have a
[message broker](http://celery.readthedocs.org/en/latest/getting-started/brokers/)
running. In this case we're going to use [Redis](http://redis.io/). Once
installed, simply execute `redis-server` to run the server.

To start the celery worker we need to use the `celery`
command with the module that exports the celery app object.
```
celery -A reminders.celery worker -l info
```
## Running the application

The application can be run with:

```
python runapp.py
```
If all environment variables specified in `.env.example` are set
correctly then the application is now ready to send SMS
reminders. Open
[http://localhost:5000/appointment/new](http://localhost:5000/appointment/new)
to create a new appointment.

## Run the tests
Assuming you have configured the application for your local test
environment, you can then use Alembic to migrate the test database
(by setting the correct `DATABASE_URL`) and then use [pytest](http://pytest.org/)
to run the tests:
```
py.test --cov .
```
