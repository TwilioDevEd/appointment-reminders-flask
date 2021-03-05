<a href="https://www.twilio.com">
  <img src="https://static0.twilio.com/marketing/bundles/marketing/img/logos/wordmark-red.svg" alt="Twilio" width="250" />
</a>

# Twilio's Appointment Reminders with Flask

![](https://github.com/TwilioDevEd/appointment-reminders-flask/workflows/Flask/badge.svg)
[![Coverage Status](https://coveralls.io/repos/TwilioDevEd/appointment-reminders-flask/badge.svg?branch=master&service=github)](https://coveralls.io/github/TwilioDevEd/appointment-reminders-flask?branch=master)

Use Twilio to send SMS reminders to your customers about upcoming appointments.
Learn how appointment reminders help other companies in
[these Twilio customer stories](https://www.twilio.com/use-cases/appointment-reminders).

[Read the full tutorial here](https://www.twilio.com/docs/tutorials/walkthrough/appointment-reminders/python/flask)!

## Quickstart

### Local development

This project is built using the [Flask](http://flask.pocoo.org/) web framework. It runs on Python 2.7+ and Python 3.4+.

To run the app locally, first clone this repository and `cd` into its directory. Then:

1. Create and activate a new python3 virtual environment.

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```


1. Install the requirements using [pip](https://pip.pypa.io/en/stable/installing/).

    ```bash
    pip install -r requirements.txt
    ```

1. Copy the `.env.example` file to `.env` and add the following values. Be sure to replace the placeholders and connection string with real information.

   ```
   SECRET_KEY = 'your_authy_secret_key'
   
   TWILIO_ACCOUNT_SID = '[your_twilio_account_sid]'
   TWILIO_AUTH_TOKEN = '[your_twilio_auth_token]'
   TWILIO_NUMBER = '[your_twilio_phone_number]'
   ```

1. Create Flask application variables
   
   ```bash
   export FLASK_APP=reminders 
   export FLASK_ENV=development
   ```

1. Run the migrations.

   ```bash
   flask db upgrade
   ```

1. Start a [redis](http://redis.io/) server to be our Celery broker. 
   If on a Mac, we recommend installing redis through [homebrew](http://brew.sh/)
   If you already have docker installed in your system an easy way of get redis running is:
   ```bash
   docker run -d -p 6379:6379 redis:latest
   ```

1. Start the development server:

    ```bash
    flask run
    ```

You can now access the application at
[http://localhost:5000](http://localhost:5000). To send any reminders, however,
you must also start a separate Celery worker process.


1. Start a new terminal session, `cd` into the repository, and active your
   `appointment-reminders` virtualenv

1. Activate Flask development environment
   
   ```bash
   export FLASK_ENV=development
   ```

1. Start the Celery worker:

    ```bash
    celery -A tasks.celery worker -l info
    ```

Celery will now send SMS reminders for any new appointments you create through
the web app.

## Run the tests

You can run the tests locally. Follow the instructions in the
[Local Development](#local-development) section above, and then run:

```bash
python runtests.py
```

You can then view the results with `coverage report` or build an HTML report with `coverage html`.

## Meta

* No warranty expressed or implied. Software is as is. Diggity.
* [MIT License](LICENSE)
* Lovingly crafted by Twilio Developer Education.
