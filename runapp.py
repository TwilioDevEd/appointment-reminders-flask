import flask
import dotenv

class Route(object):
    def __init__(self, url, routeAPI):
        self.url = url
        self.routeAPI = routeAPI

class Application(object):
    def __init__(self, routes):
        self.app = flask.Flask(__name__)
        self.routes = routes

    def start_app(self):
        for route in routes:
           self.app.add_url_rule(route.url, view_func=route.routeAPI.as_view())
        self.app.run()

handlers = [
    Route('/appointment', appointment)
]

if __name__ == "__main__":
    dotenv.load_dotenv(os.join(dirname(__file__), '.env'))
    application = Application(handlers)
    application.start_app()
