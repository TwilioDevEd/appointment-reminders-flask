# Twilio's Appointment Reminders with Flask

It is recommended to use a [virtualenv](https://virtualenv.pypa.io/en/latest/)
together with
[virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/) to
manage the applications' dependencies. Assuming both are installed, the
application can be run as follows:

Create a virtualenv with virtualenvwrapper:
```
mkvirtualenv appointment-reminders-flask --python python3
```
Activate the virtualenv:
```
workon appointment-reminders-flask
```
Inside the cloned repo you can install the dependencies of the
application using:
```
pip install -r requirements.txt
```
## Database migrations
You'll need to set the environment variables specified in env.example
to match your local configuration. Either set the variables manually
or source the file. The database schema is managed using
[Alembic](https://github.com/zzzeek/alembic).

Migrate the database:
```
alembic upgrade +1
```
## Start the celery worker
First you'll need to have a backend running. In this case we're going
to use [Redis](http://redis.io/). Simply execute `redis-server` to
run the server.

To start the celery worker we need to point out the module that exports
the celery app object.
```
celery -A reminders.celery worker
```
## Running the application

The application can be run with:

```
python runapp.py
```
If all environment variables specified in `env.example` are set
correctly then the application is now ready to send SMS
reminders. Open
[http://localhost:5000/appointment/new](http://localhost:5000/appointment/new)
to create a new appointment.

## Run the tests
Assuming you have configured the application for your local test
environment, you can then use Alembic to migrate the test database
(by setting the correct `DATABASE_URI`) and then use pytest
to run the tests:
```
py.test
```
