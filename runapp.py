from application import handlers, Application
import dotenv
import os

if __name__ == "__main__":
    dotenv.load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))
    app = Application(handlers)
    app.start_app()
