from application import handlers, reminders_application, db
import dotenv
import os

if __name__ == "__main__":
    dotenv.load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))
    reminders_application.start_app()
