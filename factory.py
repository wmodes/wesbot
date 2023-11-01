"""
factory.py - Chatbot App Factory

This file contains the factory function for creating the Chatbot app. The factory function creates a Flask app with the chatbot registered with it. It also configures the Flask app. The factory function is used in the 'app.py' file to create the Chatbot app.

Author: Wes Modes
Date: 2023
"""

import flask
from chatbot import Chatbot
from routes import routes
import config
import logging

# Configure the logger for the 'routes' module
routes_logger = logging.getLogger('httpd_logger')
# log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
routes_log_handler = logging.FileHandler(config.LOG)
# routes_log_handler.setFormatter(logging.Formatter(log_format))
routes_logger.addHandler(routes_log_handler)
routes_logger.setLevel(logging.INFO)

# Create a logger for the 'chatbot' module, writing to stdout
chatbot_logger = logging.getLogger('chatbot_logger')
chatbot_logger.setLevel(logging.INFO)

def create_app():
    app = flask.Flask(__name__)

    # Create a chatbot instance
    chatbot = Chatbot()

    # Register the chatbot blueprint with the Flask app
    app.register_blueprint(routes(chatbot))

    # Configure the Flask app

    return app