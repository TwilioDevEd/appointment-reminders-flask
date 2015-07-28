# Twilio's Appointment Reminders with Flask

It is recommended to use a [virtualenv](https://virtualenv.pypa.io/en/latest/)
together with
[virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/) to
manage the applications' dependencies. Assuming both are installed, the
application can be run as follows:

Create a virtualenv:

```
mkvirtualenv appointment-reminders-flask --python python3
```

Activate the virtualenv:

```
workon appointment-reminders-flask
```

Inside the cloned repo:

```
pip install -r requirements.txt
```

## Database migrations

The database schema is managed used [Alembic](https://github.com/zzzeek/alembic)

Migrate the database:

```
alembic upgrade +1
```

## Start the application

The application can be run with:

```
python runapp.py
```

## Run the tests
Customize `.env.test` to your needs, use alembic to migrate the test
database (make sure you have the right `DATABASE_URI` set) and then use pytest to run the tests:

```
py.test
```
