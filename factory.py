# factory.py
# This file contains the factory function for creating the Chatbot app.

# The factory function creates a Flask app with the chatbot registered with it.
# It also configures the Flask app.

# The factory function is used in the `app.py` file to create the Chatbot app.

import flask
from chatbot import Chatbot
from routes import routes

def create_app():
    app = flask.Flask(__name__)

    # Create a chatbot instance
    chatbot = Chatbot()

    # Register the chatbot blueprint with the Flask app
    app.register_blueprint(routes(chatbot))

    # Configure the Flask app

    return app