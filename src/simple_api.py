"""Simple Python Flask API to support CS7319 Homework 1."""

from flask import Flask


class WelcomeController:
    """Rest Controller to provide hello world and welcome messages."""

    def __init__(self, port=5000):
        """Initialize rest controller class."""
        self.app = Flask(__name__)
        self.port = port
        self.setup_routes()

    def setup_routes(self):
        """Set up flask routes (equivalent to @GetMapping in java-spring)."""
        @self.app.route("/")
        def hello_world():
            """Return a HTTP greeting when localhost:<port> is visted."""
            return "Hello, World!"

        @self.app.route("/welcome")
        def welcome():
            """Return a welcome message."""
            return "Welcome to CS 7319!"

    def run(self):
        """Run the Flask application."""
        self.app.run(host="0.0.0.0", port=self.port, debug=False)


if __name__ == "__main__":
    controller = WelcomeController()
    controller.run()
